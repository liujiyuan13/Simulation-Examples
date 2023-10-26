import numpy as np

import Rand

TotalCallers = 100
CallerIDs = np.linspace(1,TotalCallers,TotalCallers)
InterarrivalTimes = np.linspace(1,TotalCallers,TotalCallers)
ArrivalTimes = np.linspace(1,TotalCallers,TotalCallers)
AbleAvailableTimes = np.linspace(1,TotalCallers,TotalCallers)
BakerAvailableTimes = np.linspace(1,TotalCallers,TotalCallers)
ServerChosens = np.linspace(1,TotalCallers,TotalCallers)
ServiceTimes = np.linspace(1,TotalCallers,TotalCallers)
TimeServiceBegins = np.linspace(1,TotalCallers,TotalCallers)
AbleTimeServiceEnds = np.linspace(1,TotalCallers,TotalCallers)
BakerTimeServiceEnds = np.linspace(1,TotalCallers,TotalCallers)
CallerDelay = np.linspace(1,TotalCallers,TotalCallers)
TimeInSystem = np.linspace(1,TotalCallers,TotalCallers)
IdleTimeOfAble = np.linspace(1,TotalCallers,TotalCallers)
IdleTimeOfBaker = np.linspace(1,TotalCallers,TotalCallers)

InterarrivalTimeSamples = [1,2,3,4] # Minutes
InterarrivalTimesProb = [0.25,0.40,0.20,0.15]

AbleServiceTimeSamples = [2,3,4,5] # Minutes
AbleServiceTimesProb = [0.30,0.28,0.25,0.17]

BakerServiceTimeSamples = [3,4,5,6] # Minutes
BakerServiceTimesProb = [0.35,0.25,0.20,0.20]

def Init():
    for i in range(TotalCallers):
        InterarrivalTimes[i] = Rand.uniformDiscrete(InterarrivalTimeSamples,InterarrivalTimesProb,4)
        ArrivalTimes[i] = -1
        AbleAvailableTimes[i] = -1
        BakerAvailableTimes[i] = -1   
        ServerChosens[i] = -1
        ServiceTimes[i] = -1
        TimeServiceBegins[i] = -1
        AbleTimeServiceEnds[i] = -1
        BakerTimeServiceEnds[i] = -1
        CallerDelay[i] = -1
        TimeInSystem[i] = -1
        IdleTimeOfAble[i] = -1
        IdleTimeOfBaker[i] = -1
def Trial():
    Init()
    for i in range(TotalCallers):
        if(i == 0):
            ArrivalTimes[0] = 0
            AbleAvailableTimes[0] = 0
            BakerAvailableTimes[0] = 0   
            ServerChosens[0] = 0
            ServiceTimes[0] = Rand.uniformDiscrete(AbleServiceTimeSamples,AbleServiceTimesProb,4)
            TimeServiceBegins[0] = 0
            AbleTimeServiceEnds[0] = ServiceTimes[0]
            CallerDelay[0] = 0
            TimeInSystem[0] = ServiceTimes[0]
            IdleTimeOfAble[0] = 0
            IdleTimeOfBaker[0] = 0
        else:
            ArrivalTimes[i] = ArrivalTimes[i - 1] + InterarrivalTimes[i]
            AbleAvailableTimes[i] = max(AbleTimeServiceEnds)
            BakerAvailableTimes[i] = max(BakerTimeServiceEnds)  
            if(AbleAvailableTimes[i] <= ArrivalTimes[i] or AbleAvailableTimes[i] <= BakerAvailableTimes[i]):
                ServerChosens[i] = 0
            else:
                ServerChosens[i] = 1
            if(ServerChosens[i] == 0):
                ServiceTimes[i] = Rand.uniformDiscrete(AbleServiceTimeSamples,AbleServiceTimesProb,4)
                TimeServiceBegins[i] = max(ArrivalTimes[i],AbleAvailableTimes[i])
                AbleTimeServiceEnds[i] = TimeServiceBegins[i] + ServiceTimes[i]
                TimeInSystem[i] = AbleTimeServiceEnds[i] - ArrivalTimes[i]
                IdleTimeOfAble[i] = TimeServiceBegins[i] - AbleAvailableTimes[i]
            else:
                ServiceTimes[i] = Rand.uniformDiscrete(BakerServiceTimeSamples,BakerServiceTimesProb,4)
                TimeServiceBegins[i] = max(ArrivalTimes[i],BakerAvailableTimes[i])    
                BakerTimeServiceEnds[i] = TimeServiceBegins[i] + ServiceTimes[i]  
                TimeInSystem[i] = BakerTimeServiceEnds[i] - ArrivalTimes[i]  
                IdleTimeOfBaker[i] = TimeServiceBegins[i] - BakerAvailableTimes[i]
            CallerDelay[i] = TimeServiceBegins[i] - ArrivalTimes[i]

    AbleIdleTime = 0
    for i in range(TotalCallers):
        if(IdleTimeOfAble[i] >= 0):
            AbleIdleTime += IdleTimeOfAble[i]

    BakerIdleTime = 0
    for i in range(TotalCallers):
        if(IdleTimeOfBaker[i] >= 0):
            BakerIdleTime += IdleTimeOfBaker[i]

#    print("AbleIdleTime = " + str(AbleIdleTime))
#    print("BakerIdleTime = " + str(BakerIdleTime))
    
    return CallerDelay
