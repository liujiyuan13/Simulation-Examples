import numpy as np
import Rand

TotalCustomers = 100
CustomerIDs = np.linspace(1,TotalCustomers,TotalCustomers)
InterarrivalTimes = np.linspace(1,TotalCustomers,TotalCustomers)
ArrivalTimes = np.linspace(1,TotalCustomers,TotalCustomers)
ServiceTimes = np.linspace(1,TotalCustomers,TotalCustomers)
TimeServiceBegins = np.linspace(1,TotalCustomers,TotalCustomers)
WaitingTimeInQueue = np.linspace(1,TotalCustomers,TotalCustomers)
TimeServiceEnds = np.linspace(1,TotalCustomers,TotalCustomers)
TimeCustomerSpendsInSystem = np.linspace(1,TotalCustomers,TotalCustomers)
IdleTimeOfServer = np.linspace(1,TotalCustomers,TotalCustomers)

InterarrivalTimeSamples = [1,2,3,4,5,6,7,8] # Minutes
InterarrivalTimesProb = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

ServiceTimeSamples = [1,2,3,4,5,6] # Minutes
ServiceTimesProb = [0.10,0.20,0.30,0.25,0.10,0.05]

def Init():
    for i in range(TotalCustomers):
        InterarrivalTimes[i] = Rand.uniformDiscrete(InterarrivalTimeSamples,InterarrivalTimesProb,8)
        ServiceTimes[i] = Rand.uniformDiscrete(ServiceTimeSamples,ServiceTimesProb,6) 
        ArrivalTimes[i] = -1
        TimeServiceBegins[i] = -1
        WaitingTimeInQueue[i] = -1
        TimeServiceEnds[i] = -1
        TimeCustomerSpendsInSystem[i] = -1
        IdleTimeOfServer[i] = -1

def Trial():
    Init()
    for i in range(TotalCustomers):
        if(i == 0):
            ArrivalTimes[0] = 0
            TimeServiceBegins[0] = 0
            WaitingTimeInQueue[0] = 0
            TimeServiceEnds[0] = ServiceTimes[0]
            TimeCustomerSpendsInSystem[0] = ServiceTimes[0]
            IdleTimeOfServer[0] = 0
        else:
            ArrivalTimes[i] = ArrivalTimes[i - 1] + InterarrivalTimes[i]
            TimeServiceBegins[i] = max(ArrivalTimes[i],TimeServiceEnds[i - 1])
            WaitingTimeInQueue[i] = TimeServiceBegins[i] - ArrivalTimes[i]
            TimeServiceEnds[i] = TimeServiceBegins[i] + ServiceTimes[i]
            TimeCustomerSpendsInSystem[i] = TimeServiceEnds[i] - ArrivalTimes[i]
            if(ArrivalTimes[i] - TimeServiceEnds[i - 1] > 0):
                IdleTimeOfServer[i] = ArrivalTimes[i] - TimeServiceEnds[i - 1]
            else:
                IdleTimeOfServer[i] = 0
    return WaitingTimeInQueue
