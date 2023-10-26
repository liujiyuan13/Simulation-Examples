from scipy import stats
import random

random.seed(12345)

boundary = [
    [-400,-30,315,500,500,250,-125,-400,-400],
    [200,530,530,400,-200,-425,-425,-100,200]]

deltaXs = []
deltaYs = []
a = []
for i in range(len(boundary[0])):
    print(i)
    if(i > 0):
        deltaXs.append(boundary[0][i] - boundary[0][i - 1])
        deltaYs.append(boundary[1][i] - boundary[1][i - 1])
        a.append(deltaXs[i - 1] * boundary[1][i] - deltaYs[i - 1] * boundary[0][i])

print(deltaXs)
print(deltaYs)
print(a)

def Missed(x,y):
    for i in range(len(a)):
        if(deltaXs[i] * y > deltaYs[i] * x + a[i]):
            return True
    return False

deltaX = 400
deltaY = 200

def Bomb():
    hits = 0
    misses = 0
    Xs = []
    Ys = []
    for i in range(10):
        x = random.normalvariate(0,deltaX)
        y = random.normalvariate(0,deltaY) 
        Xs.append(x)
        Ys.append(y)
        if(Missed(x,y)):
            misses += 1
        else:
            hits += 1
    #print("Misses = " + str(misses))
    #print("hits = " + str(hits))
    return [Xs,Ys,hits]

def Bombs():
    hits = 0
    misses = 0
    for i in range(10):
        x = random.normalvariate(0,deltaX)
        y = random.normalvariate(0,deltaY) 
        if(Missed(x,y)):
            misses += 1
        else:
            hits += 1
    #print("Misses = " + str(misses))
    #print("hits = " + str(hits))
    return hits
