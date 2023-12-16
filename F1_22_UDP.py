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
        self.mode="Booting"

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
            if string_code=="BUTN":
                if data[14] & Buttons["UDP Action 6"]:
                    if interface.mode=="Lap":
                        interface.mode="Self"
                    elif interface.mode=="Self":
                        interface.mode="Lap"
                if data[14] & Buttons["UDP Action 9"]:
                    if interface.mode=="Lap":
                        interface.mode="Push"
                    elif interface.mode=="Push":
                        interface.mode="Lap"
        #print(data)
        # print(data)

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
        mega.graph_data["Driver_Colors"][i]=mega.team_colors[mega.data["PacketParticipantsData"]["m_participants"][i]["m_teamId"]]
        try:
            mega.graph_data["Driver_Names"][i]="".join(j.decode("utf-8") for j in mega.data["PacketParticipantsData"]["m_participants"][i]["m_name"][:
                                                                                                                                    mega.data["PacketParticipantsData"]["m_participants"][i]["m_name"].index(b'\x00')])
        except: #FUCKING PEREZ HAS A BUGGY TELEMETRY NAME
            print([j for j in mega.data["PacketParticipantsData"]["m_participants"][i]["m_name"]])
            mega.graph_data["Driver_Names"][i]="PEREZ"
    time.sleep(1)
    interface.mode="Lap"
thread1=threading.Thread(target=get_packet)
thread1.daemon=True
#thread1.setDaemon(True)
thread1.start()
thread2=threading.Thread(target=check_player_count)
thread2.start()



fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(nrows=2,ncols=2)
fig.canvas.manager.window.wm_geometry('1920x1080+1920+0')
pit_offset=30*1000


def animate(m):

    #thread2.join()
    #Primary Data
    mega.lap_times()
    lap_times=pd.DataFrame(mega.graph_data["Lap_Times"])
    mega.fuel_loads_per_lap()
    fuel_loads_per_lap=pd.DataFrame(mega.graph_data["Fuel_Loads_Per_Lap"])
    mega.tyre_wear()
    tyre_wear=(100-pd.DataFrame(mega.graph_data["Tyre_Wear"]).mean()).to_dict()
    mega.race_distance()
    race_distance=pd.Series(mega.graph_data["Race_Distance"])
    #print(tyre_wear.to_dict())
    #tyre_wear=pd.DataFrame(compute.get_total_wear(mega.graph_data["Tyre_Wear"]))
    #print(mega.graph_data["Tyre_Wear"])
    #print(tyre_wear)

    #Secondary Data
    drivers_pace=(race_distance/lap_times.sum()).to_dict()
    drivers_pace_with_pit=(race_distance/(pit_offset+lap_times.sum())).to_dict()
    drivers_progress=race_distance/(mega.data["PacketSessionData"]["m_trackLength"]*mega.data["PacketSessionData"]["m_totalLaps"])
    driver_order=[i for i,_ in sorted(drivers_pace.items(),key=lambda x:x[1])]
    fuel_burn_per_lap=fuel_loads_per_lap.loc[:,fuel_loads_per_lap.columns==mega.player_index].diff()
    #print(fuel_burn_per_lap)
    #print(fuel_burn_per_lap.index)
    fuel_burn_max,fuel_burn_avg=fuel_burn_per_lap.min().iloc[0],fuel_burn_per_lap.mean().iloc[0]

    llr=fuel_burn_per_lap[mega.player_index][
        fuel_burn_per_lap.index[-1]] #Last Lap Reference
    llr=fuel_loads_per_lap[mega.player_index][fuel_loads_per_lap.index[-1]]
    extrapolate_fuel_burn=pd.DataFrame(
        {
            "Average":{i:llr+fuel_burn_avg*(i-fuel_burn_per_lap.index[-1]) for i in range(fuel_burn_per_lap.index[-1],mega.data["PacketSessionData"]["m_totalLaps"])},
            "Max":{i:llr+fuel_burn_max*(i-fuel_burn_per_lap.index[-1]) for i in range(fuel_burn_per_lap.index[-1],mega.data["PacketSessionData"]["m_totalLaps"])},
            "Actual":fuel_loads_per_lap[mega.player_index]#fuel_loads_per_lap.loc[:,fuel_loads_per_lap.columns==mega.player_index].columns[0]
        }
    )
    self_vs_opponent_average_lap_time=pd.DataFrame(
        {
            "Self":lap_times[mega.player_index],
            "Opponents":lap_times.loc[:,lap_times.columns!=mega.player_index].mean(1)
        }
    )
    #print(fuel_burn_max)
    
    #print(fuel_burn_per_lap.iloc[-1,-1])
    # extrapolate_fuel_burn=pd.DataFrame(
    #                         {"Average":{i:fuel_burn_per_lap.iloc[-1,-1]-fuel_burn_avg*(i-fuel_burn_per_lap.iloc[-1,-1]) for i in range(fuel_burn_per_lap.iloc[-1,-1],mega.data["PacketSessionData"]["m_totalLaps"])},
    #                        "Max":{i:fuel_burn_per_lap.iloc[-1,-1]-fuel_burn_max*(i-fuel_burn_per_lap.iloc[-1,-1]) for i in range(fuel_burn_per_lap.iloc[-1,-1],mega.data["PacketSessionData"]["m_totalLaps"])},
    #                        #"Actual":fuel_loads_per_lap.loc[:,fuel_loads_per_lap.columns==mega.player_index]
    #                        }
    #                         )
    # self_vs_opponent_average_lap_time=pd.DataFrame({"Opponent":lap_times.loc[:,lap_times.columns!=mega.player_index].mean(1),
    #                                                   "Self":lap_times.loc[:,lap_times.columns==mega.player_index],})

    ax1.cla()
    ax2.cla()
    ax3.cla()
    ax4.cla()
    if interface.mode=="Lap":
        lap_times.plot(ax=ax1,color=mega.graph_data["Driver_Colors"])
        ax1.legend([mega.graph_data["Driver_Names"][i][:3] for i in range(mega.number_of_drivers)])

        fuel_loads_per_lap.plot(ax=ax2,color=mega.graph_data["Driver_Colors"],legend=False)
        
        ax3.barh([mega.graph_data["Driver_Names"][i][:3] for i in range(mega.number_of_drivers)],tyre_wear.values(),color=[i for i in mega.graph_data["Driver_Colors"].values()])
        ax3.set_xlim(min(tyre_wear.values())-1,min(tyre_wear.values())+1)
        
        bars=ax4.bar([mega.graph_data["Driver_Names"][i][:3] for i in driver_order],[drivers_pace[i] for i in driver_order],color=[mega.graph_data["Driver_Colors"][i] for i in driver_order],alpha=0.5)
        ax4.bar([mega.graph_data["Driver_Names"][i][:3] for i in driver_order],[drivers_pace_with_pit[i] for i in driver_order],color=[mega.graph_data["Driver_Colors"][i] for i in driver_order])
        #mplcyberpunk.add_bar_gradient(bars=bars)
    elif interface.mode=="Self":
        #print(extrapolate_fuel_burn)
        #print(mega.data["EventDataDetails"]["FastestLap"]["lapTime"])

        #print(extrapolate_fuel_burn.columns)
        # self_vs_opponent_average_lap_time=pd.DataFrame({"Opponent":lap_times.loc[:,lap_times.columns!=mega.player_index].mean(1),
        #                                                 "Self":lap_times.loc[:,lap_times.columns==mega.player_index],})

        self_vs_opponent_average_lap_time.plot(ax=ax1,color=["green","red"])
        ax1.legend([i for i in self_vs_opponent_average_lap_time.columns])
        fastest_lap=ax1.plot(pd.Series({i:mega.data["EventDataDetails"]["FastestLap"]["lapTime"]*1000 for i in range(1,lap_times.shape[0])}),color="C11")#lap_times.min().min().item()
        mplcyberpunk.add_underglow(ax1)

        extrapolate_fuel_burn.plot(ax=ax2,color=["red","green","blue"],legend=False,marker="s")
        ax2.legend([i for i in extrapolate_fuel_burn.columns])
        fuel_cutoff=ax2.plot(pd.Series({i:fuel_loads_per_lap[mega.player_index].max().item() if i<extrapolate_fuel_burn.shape[0]-1 else 0 for i in range(extrapolate_fuel_burn.shape[0])}),color="C11")
        mplcyberpunk.add_underglow(ax2)
        
        ax3.barh([mega.graph_data["Driver_Names"][i][:3] for i in range(mega.number_of_drivers)],tyre_wear.values(),color=[i for i in mega.graph_data["Driver_Colors"].values()])
        ax3.set_xlim(min(tyre_wear.values())-1,min(tyre_wear.values())+1)
        
        bars=ax4.bar([mega.graph_data["Driver_Names"][i][:3] for i in driver_order],[drivers_pace[i] for i in driver_order],color=[mega.graph_data["Driver_Colors"][i] for i in driver_order],alpha=0.5)
        ax4.bar([mega.graph_data["Driver_Names"][i][:3] for i in driver_order],[drivers_pace_with_pit[i] for i in driver_order],color=[mega.graph_data["Driver_Colors"][i] for i in driver_order])
        ax4.set_ylim(drivers_pace_with_pit[mega.player_index]-0.05,drivers_pace[mega.player_index]+0.05)
        #mplcyberpunk.add_bar

ani = animation.FuncAnimation(plt.gcf(), animate, interval=10)

#ax1.legend()
plt.show()