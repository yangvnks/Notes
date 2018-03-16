import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()
ts = ts.to_frame()
ts_plt=ts.plot()
ts_plt.set(xlabel=" t", ylabel="y(t)")
plt.show()
