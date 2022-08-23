# normal data disturbance 

import numpy as nmp 
import matplotlib.pyplot as plt 

x  =  nmp.random.normal(5.0,1.0,500)
plt.hist(x,100)
plt.show()
# 5.0 = mean
# 1.0 =  sd 
#100 = bars