import pandas

ds  =  pandas.read_csv("dummydataset.cvs")

ds.corr()
print(ds.corr())