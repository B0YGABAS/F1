import socket
import struct
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import mplcyberpunk
import concurrent.futures
import random
import f1_22_telemetry.listener
import pandas as pd

import UDP_Formats
import Megadata



#print(UDP_Formats.abc.codes)

udp=UDP_Formats.UDP()
for i in udp.codes:
    if not callable(udp.codes[i]):
        if '<' not in udp.codes[i]:
            udp.codes[i]="<"+udp.codes[i]
localIP="127.0.0.1"
localPort=20777
bufferSize=57460#1024

UDPServerSocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP,localPort))

data_format='<H4BQfI2B'
print(data_format)

Buttons={'Cross or A': 1,
 'Triangle or Y': 2,
 'Circle or B': 4,
 'Square or X': 8,
 'D-pad Left': 16,
 'D-pad Right': 32,
 'D-pad Up': 64,
 'D-pad Down': 128,
 'Options or Menu': 256,
 'L1 or LB': 512,
 'R1 or RB': 1024,
 'L2 or LT': 2048,
 'R2 or RT': 4096,
 'Left Stick Click': 8192,
 'Right Stick Click': 16384,
 'Right Stick Left': 32768,
 'Right Stick Right': 65536,
 'Right Stick Up': 131072,
 'Right Stick Down': 262144,
 'Special': 524288,
 'UDP Action 1': 1048576,
 'UDP Action 2': 2097152,
 'UDP Action 3': 4194304,
 'UDP Action 4': 8388608,
 'UDP Action 5': 16777216,
 'UDP Action 6': 33554432,
 'UDP Action 7': 67108864,
 'UDP Action 8': 134217728,
 'UDP Action 9': 268435456,
 'UDP Action 10': 536870912,
 'UDP Action 11': 1073741824,
 'UDP Action 12': 2147483648}


mega=Megadata.Megadata()

class Interface():
    def __init__(self):
        self.mode="Normal"

interface=Interface()
print(interface.mode)
plt.style.use("cyberpunk")

pool= concurrent.futures.ThreadPoolExecutor(3)
def get_packet():
    packet,address=UDPServerSocket.recvfrom(bufferSize)
    data=udp.codes[struct.unpack(data_format,packet[:24])[4]]
    if callable(data):
        data,string_code=data(packet)
    data=struct.unpack(data,packet[:struct.calcsize(data)])
    return data

work1=pool.submit(get_packet)

fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(nrows=2,ncols=2)

# line1=ax1.plot([], [], label='Channel 1') #NON CLA() REFRESH
# line2=ax1.plot([], [], label='Channel 2')

def animate(m):

    # #global UDPServerSocket   #GET UDP SINGLE THREAD
    # #print(UDPServerSocket.recv(bufferSize))
    # packet,address=UDPServerSocket.recvfrom(bufferSize)
    # data=udp.codes[struct.unpack(data_format,packet[:24])[4]]
    # if callable(data):
    #     data,string_code=data(packet)
    # data=struct.unpack(data,packet[:struct.calcsize(data)])
    # if string_code=="BUTN":
    #     for i in Buttons:
    #         if Buttons[i] & data[-1]:
    #             print(i)
    
    global work1
    if work1.done():
        #print(work1.result())
        #print(work1.result(),len(work1.result()))
        scratch=work1.result()
        if scratch[4]!=3:
            mega.insert(scratch)
        #mega.insert(work1.result())
        work1=pool.submit(get_packet)

    # try:
    #     mega.lap_times()
    # except:
    #     pass
    mega.lap_times()
    lap_times=pd.DataFrame(mega.graph_data["Lap_Times"])
    #print(lap_times)

    # line1,line2=ax1.lines #NON CLA() REFRESH
    # print(type(line1))
    # ax2.plot(lap_times)
    # #print(line1)
    # #line1.set_data([0,1,2,3,4,5], [6,7,8,9,10,11])
    # #line2.set_data([0,1,2,3,4,5], [0,1,2,3,4,5])
    # line1.set_data([i for i in range(100)], [random.randrange(100) for i in range(100)])
    # line2.set_data([i for i in range(100)], [random.randrange(100) for i in range(100)])
    # #line1.set_data(lap_times)
    # #line2.set_data([i for i in range(100)], [random.randrange(100) for i in range(100)])
    # ax1.set_xlim(0, 120)
    # ax1.set_ylim(0, 120)

    ax1.cla()
    ax1.plot(lap_times)

ani = animation.FuncAnimation(plt.gcf(), animate, interval=1)

ax1.legend()
#fig.canvas.manager.window.move(0)
#plt.tight_layout()
plt.show()

# while True:
#     packet,address=UDPServerSocket.recvfrom(bufferSize)
#     data=udp.codes[struct.unpack(data_format,packet[:24])[4]]
#     if callable(data):
#         data,string_code=data(packet)
    
#     data=struct.unpack(data,packet[:struct.calcsize(data)])
#     if string_code=="BUTN":
#         for i in Buttons:
#             if Buttons[i] & data[-1]:
#                 print(i)