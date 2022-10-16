# import numpy as np 
# import matplotlib.pyplot as mpl


# a = np.array([1,2,3,4,5])
# b= np.array([10,20,30,40,50])
# c = np.array([12.3,14.3,1.2,9.2,20.9,12.3,14.3,10,10,10,10])
# names = np.array([])
# #mpl.scatter(a,b)
# #mpl.pie(c)
# #mpl.boxplot(c)
# #mpl.bar(a,b)


# mpl.show()
# #print(a)
import matplotlib.pyplot as plt
import numpy as np


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
print (x)
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
