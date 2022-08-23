import pandas as pnd 
import matplotlib.pyplot as mp 

ds  =  pnd.read_csv("dummydataset.cvs")

ds.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
# mp.scatter(x="Duation", y="Maxpulse")
mp.show()