import pandas as pns

ds = pns.read_csv("dummydataset2.cvs")

new_cvs = ds.dropna()

print(new_cvs)
