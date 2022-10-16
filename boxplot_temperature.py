from statistics import median
import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd

#Use celsium insted of far. Then add far => cel

a = np.random.randint(-15,38, size=(30,12))
# q = np.zeros(5)
# w = np.random.randint(1,5,size=5)
# b = np.stack((q,w))
#print(b)

january=np.random.randint(45,68,size=31) #mode, mediana, mean

#Max, min, quartile
january_sorted = np.sort(january) 
january_min = np.amin(january)
january_max = np.amax(january)
if (len(january)%2!=0): m_c=january[(len(january)+1)//2]
january_q= np.quantile(january,[0.25,0.5,0.75])

print(january)
# print(january_sorted)
# print(january_min)
# print(january_max)
# print(m_c)
# print(january_q)

#moda for temperatura 
valuesoftem = np.arange(january_min, january_max)
january_abfreq = np.zeros(len(valuesoftem), dtype=np.int64)
for i in range(len(january)):
    for j in range (len(valuesoftem)):
        if (january[i] == valuesoftem[j]): january_abfreq[valuesoftem[j]-45]+=1

print(valuesoftem)
print(january_abfreq)
plt.boxplot(a)
#plt.show()