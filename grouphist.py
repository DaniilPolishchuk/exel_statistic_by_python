import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

n_bins = 'auto'
date_range = (1,5)
x = np.random.randint(1,6, size=(100,2) )

#print (x)

fig, (ax0) = plt.subplots(nrows=1, ncols=1)  #, ax1), (ax2, ax3)

colors = ['red', 'lime'] #, 'lime']
names = ['Restaurant 1',' Restaurant 2']
ax0.hist(x, n_bins,date_range, density=True, histtype='bar', color=colors, label=names)
ax0.legend(prop={'size': 10})
ax0.set_title('Rate of the restaurans')


fig.tight_layout()
plt.show()