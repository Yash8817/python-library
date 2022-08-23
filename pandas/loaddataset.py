import pandas 
ds = pandas.read_csv("dummydataset.cvs")
# load only staring and ending data if data is too big
print(ds)
print("")
# load full data no matter how long data is
print(ds.to_string())


