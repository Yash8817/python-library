import pandas as pd


name = ["yash","ravi","ak"]
print("without lable")
srs = pd.Series(name)
print(srs)

print("")
print("with lable")
srs1 = pd.Series(name , index =["A","B","C"])
print(srs1)
