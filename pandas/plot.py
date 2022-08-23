import pandas as pd 
import matplotlib.pyplot as pp 

ds = pd.read_csv("dummydataset.cvs")

pp.plot(ds)

pp.show()