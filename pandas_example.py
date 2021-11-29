import pandas as pd
import matplotlib.pyplot as plt
#%pylab inline

data = pd.read_csv("hubble_data.csv")
data.head()
data.set_index("distance", inplace=True)
data.head()
data.plot()
plt.show()
