import struct
class UDP():
    def __init__(self) -> None:
        self.super={"PacketHeader":
        {
        "m_packetFormat":"H",
        "m_gameMajorVersion":"B",
        "m_gameMinorVersion":"B",
        "m_packetVersion":"B",
        "m_packetId":"B",
        "m_sessionUID":"Q",
        "m_sessionTime":"f",
        "m_frameIdentifier":"I",
        "m_playerCarIndex":"B",
        "m_secondaryPlayerCarIndex":"B",
        },

        "CarMotionData":
        {
        "m_worldPositionX":"f",
        "m_worldPositionY":"f",
        "m_worldPositionZ":"f",
        "m_worldVelocityX":"f",
        "m_worldVelocityY":"f",
        "m_worldVelocityZ":"f",
        "m_worldForwardDirX":"h",
        "m_worldForwardDirY":"h",
        "m_worldForwardDirZ":"h",
        "m_worldRightDirX":"h",
        "m_worldRightDirY":"h",
        "m_worldRightDirZ":"h",
        "m_gForceLateral":"f",
        "m_gForceLongitudinal":"f",
        "m_gForceVertical":"f",
        "m_yaw":"f",
        "m_pitch":"f",
        "m_roll":"f",
        },

        "PacketMotionData":
        {
        "m_header":"PacketHeader",

        "m_carMotionData[22]":"CarMotionData",

        "m_suspensionPosition[4]":"f",
        "m_suspensionVelocity[4]":"f",
        "m_suspensionAcceleration[4]":"f",
        "m_wheelSpeed[4]":"f",
        "m_wheelSlip[4]":"f",
        "m_localVelocityX":"f",
        "m_localVelocityY":"f",
        "m_localVelocityZ":"f",
        "m_angularVelocityX":"f",
        "m_angularVelocityY":"f",
        "m_angularVelocityZ":"f",
        "m_angularAccelerationX":"f",
        "m_angularAccelerationY":"f",
        "m_angularAccelerationZ":"f",
        "m_frontWheelsAngle":"f",
        },

        "MarshalZone":
        {
        "m_zoneStart":"f",
        "m_zoneFlag":"b",
        },

        "WeatherForecastSample":
        {
        "m_sessionType":"B",
        "m_timeOffset":"B",
        "m_weather":"B",
        "m_trackTemperature":"b",
        "m_trackTemperatureChange":"b",
        "m_airTemperature":"b",
        "m_airTemperatureChange":"b",
        "m_rainPercentage":"B",
        },

        "PacketSessionData":
        {
        "m_header":"PacketHeader",

        "m_weather":"B",
        "m_trackTemperature":"b",
        "m_airTemperature":"b",
        "m_totalLaps":"B",
        "m_trackLength":"H",
        "m_sessionType":"B",
        "m_trackId":"b",
        "m_formula":"B",
        "m_sessionTimeLeft":"H",
        "m_sessionDuration":"H",
        "m_pitSpeedLimit":"B",
        "m_gamePaused":"B",
        "m_isSpectating":"B",
        "m_spectatorCarIndex":"B",
        "m_sliProNativeSupport":"B",
        "m_numMarshalZones":"B",
        "m_marshalZones[21]":"MarshalZone",
        "m_safetyCarStatus":"B",
        "m_networkGame":"B",
        "m_numWeatherForecastSamples":"B",
        "m_weatherForecastSamples[56]":"WeatherForecastSample",
        "m_forecastAccuracy":"B",
        "m_aiDifficulty":"B",
        "m_seasonLinkIdentifier":"I",
        "m_weekendLinkIdentifier":"I",
        "m_sessionLinkIdentifier":"I",
        "m_pitStopWindowIdealLap":"B",
        "m_pitStopWindowLatestLap":"B",
        "m_pitStopRejoinPosition":"B",
        "m_steeringAssist":"B",
        "m_brakingAssist":"B",
        "m_gearboxAssist":"B",
        "m_pitAssist":"B",
        "m_pitReleaseAssist":"B",
        "m_ERSAssist":"B",
        "m_DRSAssist":"B",
        "m_dynamicRacingLine":"B",
        "m_dynamicRacingLineType":"B",
        "m_gameMode":"B",
        "m_ruleSet":"B",
        "m_timeOfDay":"I",
        "m_sessionLength":"B",
        },

        "LapData":
        {
        "m_lastLapTimeInMS":"I",
        "m_currentLapTimeInMS":"I",
        "m_sector1TimeInMS":"H",
        "m_sector2TimeInMS":"H",
        "m_lapDistance":"f",
        "m_totalDistance":"f",
        "m_safetyCarDelta":"f",
        "m_carPosition":"B",
        "m_currentLapNum":"B",
        "m_pitStatus":"B",
        "m_numPitStops":"B",
        "m_sector":"B",
        "m_currentLapInvalid":"B",
        "m_penalties":"B",
        "m_warnings":"B",
        "m_numUnservedDriveThroughPens":"B",
        "m_numUnservedStopGoPens":"B",
        "m_gridPosition":"B",
        "m_driverStatus":"B",
        "m_resultStatus":"B",
        "m_pitLaneTimerActive":"B",
        "m_pitLaneTimeInLaneInMS":"H",
        "m_pitStopTimerInMS":"H",
        "m_pitStopShouldServePen":"B",
        },


        "PacketLapData":
        {
        "m_header":"PacketHeader",

        "m_lapData[22]":"LapData",

        "m_timeTrialPBCarIdx":"B",
        "m_timeTrialRivalCarIdx":"B",
        },

        "EventDataDetails":
        {
        "FastestLap":
        {
        "vehicleIdx":"B",
        "lapTime":"f",
        },

        "Retirement":
        {
        "vehicleIdx":"B",
        },

        "TeamMateInPits":
        {
        "vehicleIdx":"B",
        },

        "RaceWinner":
        {
        "vehicleIdx":"B",
        },

        "Penalty":
        {
        "penaltyType":"B",
        "infringementType":"B",
        "vehicleIdx":"B",
        "otherVehicleIdx":"B",
        "time":"B",
        "lapNum":"B",
        "placesGained":"B",
        },

        "SpeedTrap":
        {
        "vehicleIdx":"B",
        "speed":"f",
        "isOverallFastestInSession":"B",
        "isDriverFastestInSession":"B",
        "fastestVehicleIdxInSession":"B",
        "fastestSpeedInSession":"f",
        },

        "StartLIghts":
        {
        "numLights":"B",
        },

        "DriveThroughPenaltyServed":
        {
        "vehicleIdx":"B",
        },

        "StopGoPenaltyServed":
        {
        "vehicleIdx":"B",
        },

        "Flashback":
        {
        "flashbackFrameIdentifier":"I",
        "flashbackSessionTime":"f",
        },

        "Buttons":
        {
        "m_buttonStatus":"I",
        },
        },

        "PacketEventData":
        {
        "m_header":"PacketHeader",

        "m_eventStringCode[4]":"B",
        "m_eventDetails":"EventDataDetails",
        },

        "ParticipantData":
        {
        "m_aiControlled":"B",
        "m_driverId":"B",
        "m_networkId":"B",
        "m_teamId":"B",
        "m_myTeam":"B",
        "m_raceNumber":"B",
        "m_nationality":"B",
        "m_name[48]":"c",
        "m_yourTelemetry":"B",
        },

        "PacketParticipantsData":
        {
        "m_header":"PacketHeader",

        "m_numActiveCars":"B",
        "m_participants[22]":"ParticipantData",
        },

        "CarSetupData":
        {
        "m_frontWing":"B",
        "m_rearWing":"B",
        "m_onThrottle":"B",
        "m_offThrottle":"B",
        "m_frontCamber":"f",
        "m_rearCamber":"f",
        "m_frontToe":"f",
        "m_rearToe":"f",
        "m_frontSuspension":"B",
        "m_rearSuspension":"B",
        "m_frontAntiRollBar":"B",
        "m_rearAntiRollBar":"B",
        "m_frontSuspensionHeight":"B",
        "m_rearSuspensionHeight":"B",
        "m_brakePressure":"B",
        "m_brakeBias":"B",
        "m_rearLeftTyrePressure":"f",
        "m_rearRightTyrePressure":"f",
        "m_frontLeftTyrePressure":"f",
        "m_frontRightTyrePressure":"f",
        "m_ballast":"B",
        "m_fuelLoad":"f",
        },

        "PacketCarSetupData":
        {
        "m_header":"PacketHeader",

        "m_carSetups[22]":"CarSetupData",
        },
        "CarTelemetryData":
        {
        "m_speed":"H",
        "m_throttle":"f",
        "m_steer":"f",
        "m_brake":"f",
        "m_clutch":"B",
        "m_gear":"b",
        "m_engineRPM":"H",
        "m_drs":"B",
        "m_revLightsPercent":"B",
        "m_revLightsBitValue":"H",
        "m_brakesTemperature[4]":"H",
        "m_tyresSurfaceTemperature[4]":"B",
        "m_tyresInnerTemperature[4]":"B",
        "m_engineTemperature":"H",
        "m_tyresPressure[4]":"f",
        "m_surfaceType[4]":"B",
        },

        "PacketCarTelemetryData":
        {
        "m_header":"PacketHeader",

        "m_carTelemetryData[22]":"CarTelemetryData",

        "m_mfdPanelIndex":"B",
        "m_mfdPanelIndexSecondaryPlayer":"B",
        "m_suggestedGear":"b",
        },

        "CarStatusData":
        {
        "m_tractionControl":"B",
        "m_antiLockBrakes":"B",
        "m_fuelMix":"B",
        "m_frontBrakeBias":"B",
        "m_pitLimiterStatus":"B",
        "m_fuelInTank":"f",
        "m_fuelCapacity":"f",
        "m_fuelRemainingLaps":"f",
        "m_maxRPM":"H",
        "m_idleRPM":"H",
        "m_maxGears":"B",
        "m_drsAllowed":"B",
        "m_drsActivationDistance":"H",
        "m_actualTyreCompound":"B",
        "m_visualTyreCompound":"B",
        "m_tyresAgeLaps":"B",
        "m_vehicleFiaFlags":"b",
        "m_ersStoreEnergy":"f",
        "m_ersDeployMode":"B",
        "m_ersHarvestedThisLapMGUK":"f",
        "m_ersHarvestedThisLapMGUH":"f",
        "m_ersDeployedThisLap":"f",
        "m_networkPaused":"B",
        },

        "PacketCarStatusData":
        {
        "m_header":"PacketHeader",

        "m_carStatusData[22]":"CarStatusData",
        },

        "FinalClassificationData":
        {
        "m_position":"B",
        "m_numLaps":"B",
        "m_gridPosition":"B",
        "m_points":"B",
        "m_numPitStops":"B",
        "m_resultStatus":"B",
        "m_bestLapTimeInMS":"I",
        "m_totalRaceTime":"d",
        "m_penaltiesTime":"B",
        "m_numPenalties":"B",
        "m_numTyreStints":"B",
        "m_tyreStintsActual[8]":"B",
        "m_tyreStintsVisual[8]":"B",
        "m_tyreStintsEndLaps[8]":"B",
        },

        "PacketFinalClassificationData":
        {
        "m_header":"PacketHeader",

        "m_numCars":"B",
        "m_classificationData[22]":"FinalClassificationData",
        },

        "LobbyInfoData":
        {
        "m_aiControlled":"B",
        "m_teamId":"B",
        "m_nationality":"B",
        "m_name[48]":"c",
        "m_carNumber":"B",
        "m_readyStatus":"B",
        },

        "PacketLobbyInfoData":
        {
        "m_header":"PacketHeader",

        "m_numPlayers":"B",
        "m_lobbyPlayers[22]":"LobbyInfoData",
        },

        "CarDamageData":
        {
        "m_tyresWear[4]":"f",
        "m_tyresDamage[4]":"B",
        "m_brakesDamage[4]":"B",
        "m_frontLeftWingDamage":"B",
        "m_frontRightWingDamage":"B",
        "m_rearWingDamage":"B",
        "m_floorDamage":"B",
        "m_diffuserDamage":"B",
        "m_sidepodDamage":"B",
        "m_drsFault":"B",
        "m_ersFault":"B",
        "m_gearBoxDamage":"B",
        "m_engineDamage":"B",
        "m_engineMGUHWear":"B",
        "m_engineESWear":"B",
        "m_engineCEWear":"B",
        "m_engineICEWear":"B",
        "m_engineMGUKWear":"B",
        "m_engineTCWear":"B",
        "m_engineBlown":"B",
        "m_engineSeized":"B",
        },

        "PacketCarDamageData":
        {
        "m_header":"PacketHeader",

        "m_carDamageData[22]":"CarDamageData",
        },

        "LapHistoryData":
        {
        "m_lapTimeInMS":"I",
        "m_sector1TimeInMS":"H",
        "m_sector2TimeInMS":"H",
        "m_sector3TimeInMS":"H",
        "m_lapValidBitFlags":"B",
        },

        "TyreStintHistoryData":
        {
        "m_endLap":"B",
        "m_tyreActualCompound":"B",
        "m_tyreVisualCompound":"B",
        },

        "PacketSessionHistoryData":
        {
        "m_header":"PacketHeader",

        "m_carIdx":"B",
        "m_numLaps":"B",
        "m_numTyreStints":"B",

        "m_bestLapTimeLapNum":"B",
        "m_bestSector1LapNum":"B",
        "m_bestSector2LapNum":"B",
        "m_bestSector3LapNum":"B",

        "m_lapHistoryData[100]":"LapHistoryData",
        "m_tyreStintsHistoryData[8]":"TyreStintHistoryData",
        },
        }
        self.general_table={0:"PacketMotionData",
        1:"PacketSessionData",
        2:"PacketLapData",
        3:"PacketEventData",
        4:"PacketParticipantsData",
        5:"PacketCarSetupData",#"PacketCarSetupsData",
        6:"PacketCarTelemetryData",
        7:"PacketCarStatusData",
        8:"PacketFinalClassificationData",
        9:"PacketLobbyInfoData",
        10:"PacketCarDamageData",
        11:"PacketSessionHistoryData"}
        self.events={"SSTA":"SessionStarted",
        "SEND":"SessionEnded",
        "FTLP":"FastestLap",#
        "RTMT":"Retirement",#
        "DRSE":"DRSenabled",
        "DRSD":"DRSdisabled",
        "TMPT":"TeamMateInPits",#
        "CHQF":"Chequeredflag",
        "RCWN":"RaceWinner",#
        "PENA":"Penalty",#
        "SPTP":"SpeedTrap",#
        "STLG":"StartLIghts",#
        "LGOT":"Lightsout",
        "DTSV":"DriveThroughPenaltyServed",#
        "SGSV":"StopGoPenaltyServed",#
        "FLBK":"Flashback",#
        "BUTN":"Buttons",#
        }
        self.event_formattable={
        "FTLP":"FastestLap",#
        "RTMT":"Retirement",#
        "TMPT":"TeamMateInPits",#
        "RCWN":"RaceWinner",#
        "PENA":"Penalty",#
        "SPTP":"SpeedTrap",#
        "STLG":"StartLIghts",#
        "DTSV":"DriveThroughPenaltyServed",#
        "SGSV":"StopGoPenaltyServed",#
        "FLBK":"Flashback",#
        "BUTN":"Buttons",#
        }
        
        #self.packet=b"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
        self.codes={}
        for i in range(3):
            self.codes[i]=self.extract_format(self.super[self.general_table[i]])
        self.codes[3]=lambda x: self.event_format(x)
        #self.event=lambda x: self.event_format(x)
        # self.event=lambda : self.event_format(self.packet)
        # self.codes[3]=lambda x: struct.unpack(self.event(),self.packet)     #event(self.packet)
        for i in range(4,12):
            self.codes[i]=self.extract_format(self.super[self.general_table[i]])
            #self.codes.append(self.extract_format(self.super[self.general_table[i]]))

    def extract_format(self,dicts,super=super):
        code=""
        for i,j in dicts.items():
            count=1
            if "[" in i and "]" in i:
                count=int(i[i.index("[")+1:i.index("]")])
            #print(j)
            if len(j)>1:
                j=self.extract_format(self.super[j])
            code=code+j*count
        return code
    
    def event_format(self,bits,offset_bits='<H4BQfI2B',bits_selected='BBBB'):
        offset,length=struct.calcsize(offset_bits),struct.calcsize(bits_selected)
        #print(offset,length,bits[offset:offset+length])
        string_code=struct.unpack(bits_selected,bits[offset:offset+length])
        string_code="".join(chr(i) for i in string_code)
        #print(string_code)
        if string_code in self.event_formattable:
            #returning=offset_bits+bits_selected+self.extract_format(self.super["EventDataDetails"][self.event_formattable[string_code]])
            return offset_bits+bits_selected+self.extract_format(self.super["EventDataDetails"][self.event_formattable[string_code]]),string_code
        # else:
        #     returning=offset_bits+bits_selected
        #print(struct.calcsize(offset_bits+bits_selected))
        # if b"b" in bits[-3:]:
        #     return "b"
        # if b"h" in bits[-3:]:
        #     return "h"
        # if b"B" in bits[-3:]:
        #     return "B"
        # if b"d" in bits[-3:]:
        #     return "d"
        # for i in range(struct.calcsize(returning),40):
        #         returning=returning+"B"
        #return returning
        return offset_bits+bits_selected,string_code

    # def event_format(self,bits,offset_bits='<H4BQfI2B',bits_selected='BBBB'):
    #     return "<BBBBB"+"BfBBBBBBfBBBfBIfI"#"BfBBBBBBBBBBBfBBBfBBBIfI"
    #     return offset_bits+bits_selected+"BfBBBBBBfBBBfBIfI"#"BfBBBBBBBBBBBfBBBfBBBIfI"
    
#abc=UDP()
# udp=UDP()
# print(udp.event_format(1))
# print(struct.calcsize(udp.event_format(1)))
# print(udp.codes)
# for i in udp.codes:
#     print(callable(udp.codes[i]))