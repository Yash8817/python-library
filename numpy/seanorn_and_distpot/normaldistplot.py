from numpy import random
import displot.pyplot as plt
import seaborn as srn

srn.distplot(random.normal(size=1000),hist=False)
plt.show()