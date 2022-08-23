import  pandas

mydataset = {
"car" : ["BMW","BharatBenz","ODI"],
"passing" : [7,2,7]
}

pns  = pandas.DataFrame(mydataset)
print(pns)

print("")
print("one value:")
pns1 = pandas.DataFrame(mydataset)
print(pns1.loc[1])
print("")
mydataset2 ={
"Activity" :["reading","hicking","listing","dancing"],
"hours"  :[3 , 1 , 1,2]
}

mydata = pandas.DataFrame(mydataset2 , index  = ["day1","day2","day3","day4"])
print(mydata)
print("")
print("you have folling activity : ")
print(mydata.loc["day1"])