import numpy as np
import pandas as pd

from pandas_datareader import data, wb

ip = data.DataReader("5_Industry_Portfolios", "famafrench")
df = ip[0]
df.head(5)



