import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataframe1 = pd.read_excel('testfile.xlsx')
 
plt.boxplot(dataframe1)
plt.show()