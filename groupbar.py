import matplotlib.pyplot as plt
import numpy as np


#data 
nameofgroups= ["Restaurant 1", 'Restaurant 2']
labels = [1, 2, 3, 4, 5]
rest1_values = np.random.randint(1,6,size=100)
rest2_values = np.random.randint(1,6,size=100)

#amount of element in data sets 
total_amount1 = len(rest1_values)
total_amount2 = len(rest2_values)

# generic levels of variabls 
levofvar = len(labels)




#Count absoulute frequency 
# n_i
rest1_abfreq = np.zeros(5, dtype=np.int64)
rest2_abfreq = np.zeros(5, dtype=np.int64)
for i in range (len(rest1_values)):
    for j in range (levofvar):
        if (rest1_values[i] == labels[j]): rest1_abfreq[labels[j]-1]+=1
        if (rest2_values[i] == labels[j]): rest2_abfreq[labels[j]-1]+=1
    
print (rest1_abfreq)
print (rest2_abfreq)

#Count  cumulative frequency 
# N_i
rest1_cumfreq = np.zeros(5, dtype=np.int64)
rest2_cumfreq = np.zeros(5, dtype=np.int64)
for i in range (levofvar):
    if (i == 0): 
        rest1_cumfreq[i] = rest1_abfreq[i] 
        rest2_cumfreq[i] = rest2_abfreq[i]
    else: 
        rest1_cumfreq[i] = rest1_abfreq[i] + rest1_cumfreq[i-1]
        rest2_cumfreq[i] = rest2_abfreq[i] + rest2_cumfreq[i-1]

# print(rest1_cumfreq)
# print(rest2_cumfreq)


# Count relative frequence 
# f_i 
rest1_relfreq = np.zeros(5)
rest2_relfreq = np.zeros(5)
for i in range(levofvar):
    rest1_relfreq[i] = rest1_abfreq[i]/total_amount1
    rest2_relfreq[i] = rest2_abfreq[i]/total_amount2

# print (rest1_relfreq)
# print(rest2_relfreq)


x = np.arange(levofvar)  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, rest1_relfreq, width, label=nameofgroups[0])
rects2 = ax.bar(x + width/2, rest2_relfreq, width, label=nameofgroups[1])

# Add some text for labels, title and custom x-axis tick labels, etc.
#ax.set_ylabel('Scores')
ax.set_title('Rates of the restautant')
ax.set_xticks(x, labels)
ax.legend()


fig.tight_layout()
plt.show()