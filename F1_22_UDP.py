import socket
import struct
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import mplcyberpunk
import concurrent.futures
import random
#import f1_22_telemetry.listener
import pandas as pd
import threading
import time

import UDP_Formats
import Megadata
import Computations

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

udp=UDP_Formats.UDP()
for i in udp.codes:
    if not callable(udp.codes[i]):
        if '<' not in udp.codes[i]:
            udp.codes[i]="<"+udp.codes[i]
mega=Megadata.Megadata()
compute=Computations.Computations()

class Interface():
    def __init__(self):
        self.mode="Normal"

interface=Interface()
print(interface.mode)
plt.style.use("cyberpunk")

def get_packet():
    while True:
        packet,address=UDPServerSocket.recvfrom(bufferSize)
        data=udp.codes[struct.unpack(data_format,packet[:24])[4]]
        string_code="Nothing"
        if callable(data):
            data,string_code=data(packet)
        data=struct.unpack(data,packet[:struct.calcsize(data)])
        if data[4]!=3:
            mega.insert(data)
        elif string_code in udp.event_formattable:
            mega.iterate(data,mega.data["EventDataDetails"][udp.event_formattable[string_code]],14) #14 is where after the index of stringcodes
        #print(data)
        #print(data)

def check_player_count():
    while type(mega.data["PacketParticipantsData"]["m_numActiveCars"])==str:
        time.sleep(1)
        #"STANDBY"
    original_number_of_players=mega.number_of_drivers
    mega.number_of_drivers=mega.data["PacketParticipantsData"]["m_numActiveCars"]
    for i,j in mega.graph_data.items():
        for k in range(mega.number_of_drivers,original_number_of_players):
            mega.graph_data[i].pop(k)
    mega.player_index=mega.data["PacketParticipantsData"]["m_header"]["m_playerCarIndex"] #struct.unpack(data_format,packet[:24])[8]
    for i in mega.graph_data["Driver_Names"]:
        try:
            mega.graph_data["Driver_Names"][i]="".join(j.decode("utf-8") for j in mega.data["PacketParticipantsData"]["m_participants"][i]["m_name"][:
                                                                                                                                    mega.data["PacketParticipantsData"]["m_participants"][i]["m_name"].index(b'\x00')])
        except: #FUCKING PEREZ HAS A BUGGY TELEMETRY NAME
            print([j for j in mega.data["PacketParticipantsData"]["m_participants"][i]["m_name"]])
            mega.graph_data["Driver_Names"][i]="PEREZ"
thread1=threading.Thread(target=get_packet)
thread1.daemon=True
#thread1.setDaemon(True)
thread1.start()
thread2=threading.Thread(target=check_player_count)
thread2.start()



fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(nrows=2,ncols=2)
fig.canvas.manager.window.wm_geometry('1920x1080+1920+0')

def animate(m):

    #Primary Data
    mega.lap_times()
    lap_times=pd.DataFrame(mega.graph_data["Lap_Times"])
    mega.fuel_loads_per_lap()
    fuel_loads_per_lap=pd.DataFrame(mega.graph_data["Fuel_Loads_Per_Lap"])
    mega.tyre_wear()
    tyre_wear=pd.DataFrame(mega.graph_data["Tyre_Wear"]).mean().to_dict()
    #print(tyre_wear.to_dict())
    #tyre_wear=pd.DataFrame(compute.get_total_wear(mega.graph_data["Tyre_Wear"]))
    #print(mega.graph_data["Tyre_Wear"])
    #print(tyre_wear)

    #Secondary Data
    mega.race_distance()
    #print(mega.graph_data["Race_Distance"])
    race_distance=pd.Series(mega.graph_data["Race_Distance"])
    drivers_pace=(race_distance/lap_times.sum()).to_dict()
    drivers_progress=race_distance/(mega.data["PacketSessionData"]["m_trackLength"]*mega.data["PacketSessionData"]["m_totalLaps"])
    driver_order=[i for i,_ in sorted(drivers_pace.items(),key=lambda x:x[1])]
    fuel_burn_per_lap=fuel_loads_per_lap.diff()
    fuel_burn_max,fuel_burn_avg=fuel_burn_per_lap.max(),fuel_burn_per_lap.mean()
    thread2.join()

    ax1.cla()
    ax2.cla()
    ax3.cla()
    ax4.cla()
    ax1.plot(lap_times.iloc[:int(lap_times.shape[1]/2)],marker='s')
    #ax1.scatter(lap_times.iloc[:int(lap_times.shape[1])],marker='o')
    ax1.plot(lap_times.iloc[int(lap_times.shape[1]/2):],marker='^')
    ax1.legend([mega.graph_data["Driver_Names"][i][:3] for i in mega.graph_data["Driver_Names"]])

    ax2.plot(fuel_loads_per_lap)
    
    ax3.barh([mega.graph_data["Driver_Names"][i][:3] for i in mega.graph_data["Driver_Names"]],tyre_wear.values())
    #ax3.barh(*zip(*tyre_wear.items()))
    #ax3.barh(tyre_wear.values(),width=1)
    
    ax4.bar([mega.graph_data["Driver_Names"][i][:3] for i in driver_order],[drivers_pace[i] for i in driver_order])
    #ax4.bar(drivers_pace,height=0.5)

ani = animation.FuncAnimation(plt.gcf(), animate, interval=100)

#ax1.legend()
plt.show()