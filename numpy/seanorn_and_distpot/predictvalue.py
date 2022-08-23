from scipy import stats

car_age =   [10,20,25,11,12,12,13]
car_speed = [100,52,45,62,45,48,101]

slope, intercept,r,p ,std_err = stats.linregress(car_age,car_speed)

def myfunc(x):
  return slope * x + intercept

speed = myfunc(10)

print(speed)
