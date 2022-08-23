import numpy
from  scipy  import stats
from numpy.lib.function_base import median

dataset = [1,2,3,4,5,6,7,8,9,10,20,30,10]

mean = numpy.mean(dataset)
print("mean=",mean)

median = numpy.median(dataset)
print("median=" , median)

mode  =  stats.mode(dataset)
print("mode=",mode)
# ANS of mode
# mode= ModeResult(mode=array([10]), count=array([2]))
# mode=array([10]) -> mode 
# count=array([2]) -> no of repeating 