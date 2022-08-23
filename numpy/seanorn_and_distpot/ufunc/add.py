import numpy as np 
x  = [1,2,3,4,5]
y = [6,7,8,9,10]
z =np.add(x,y)
print(z)
print("")
newarr =np.subtract(x,y)
print(newarr)
print("")
newarr2 =  np.multiply(x,y)
print(newarr2)
print("")
# also do remainer

newarr2 =  np.power(x,y)
print(newarr2)
print("")
if type(np.add) == np.ufunc:
    print("its universal function")

else:
    print("its not universal function")


print("")
newarr3 = np.cumsum(x)
# 1 1+2 3+3 6+4 10+5
print(newarr3)
print("")
p= np.prod(x)
# 1*2*3*4*5
print(p)

print("")
l = np.lcm.reduce(x)
g = np.gcd.reduce(x)
print(l)
print(g)