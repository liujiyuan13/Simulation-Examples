'''
Created on 2019年12月19日

@author: liqun
'''
import Output

Losts = [4.0,9.0,5.0,9.0,11.0]

R = Output.GetNR(Losts, 0.1,1.5)
print("N R = %g"%(R))

R = Output.GetR(Losts, 0.1,1.5,R)

print("Lost R = %g"%(R))