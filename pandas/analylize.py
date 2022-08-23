import pandas as pn

ds = pn.read_csv("dummydataset.cvs")
print("")
print(ds.head(3)) # print fisrt 3 rowa only
print("")
print(ds.head()) # print fisrt 5 rows
print("")
print(ds.tail(2)) # print last 2 rows  
print("")
print(ds.tail()) # print last 5 rows


