import numpy as nmp 
import matplotlib.pyplot as plt 

x  =nmp.random.uniform(10,20,250)

plt.hist(x,10)
plt.show()