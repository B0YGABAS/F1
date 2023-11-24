import socket
import struct
import time
import UDP_Formats

udp=UDP_Formats.UDP()
for i in udp.codes:
    if not callable(udp.codes[i]):
        if '<' not in udp.codes[i]:
            udp.codes[i]="<"+udp.codes[i]
#print(udp.codes)
#print(udp.codes[3])
localIP="127.0.0.1"
localPort=20777
bufferSize=57460#1024

UDPServerSocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP,localPort))

data_format='<H4BQfI2B'
#data_format='<H4BQfIB'
# data_format='<ffffffhhhhhhffffff'
print(data_format)
#data_format='<HBBBBQfIBBBBBB'
#print(struct.calcsize(data_format))

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

while True:
    packet,address=UDPServerSocket.recvfrom(bufferSize)
    #data=struct.unpack(data_format,packet[:24])[4]
    data=udp.codes[struct.unpack(data_format,packet[:24])[4]]
    if callable(data):
        data,string_code=data(packet)
        #print(data,packet)
        #print("TT")
        # data=struct.unpack(data,packet[:struct.calcsize(data)])
        # print(data)
        #print(data[14:])
    
    data=struct.unpack(data,packet[:struct.calcsize(data)])
    if string_code=="BUTN":
        for i in Buttons:
            if Buttons[i] & data[-1]:
                print(i)



    # x=struct.unpack(data_format,packet[:24])
    # print(x)
    # #print(struct.unpack(data_format,packet[:24]))
    #print("---")