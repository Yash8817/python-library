from numpy import random

import displot.pyplot as plt
import seaborn as srn


srn.displot(random.binomial(n=10,p=0.5,size=1000),hist=False,kde= false)
plt.show()
