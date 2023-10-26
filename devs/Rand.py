import random

random.seed(12345)

def uniformDiscrete(valuelist, problist,count):
    """基于离散概率分布产生随机变量样本"""
    if count <= 0:
        raise RuntimeError("uniformDiscrete：count 小于0！")
    cdflist= list()
    lastProb = 0
    for prob in problist:
        lastProb = lastProb + prob
        cdflist.append(lastProb)
    if cdflist[count-1] < 0.999 or cdflist[count-1] > 1.0:
        raise RuntimeError("uniformDiscrete:累积分布不等于1！" + str(cdflist[count-1]))
    u = random.uniform(0,1)
    i = 0
    for prob in cdflist:
        if u <= prob:
            return valuelist[i]
        i = i + 1
    return valuelist[count-1]