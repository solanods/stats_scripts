# PRACTICAL METHOD FOR BUILDING A FREQUENCY DISTRIBUTION AT CLASS INTERVALS
# THIS MODEL USES DATA GROUPED IN SEVEN CLASSES
# FOR A GREATER DISTRIBUTION THE CODE MUST BE CONTINUED

# step 1: the db variable will be the receiver of raw data

import random
import pandas as pd
import numpy as np
import math
import statistics

db = random.sample(range(300, 1000), 100)
print('Raw data:', db)

# step 2: - put the raw data in ascending order and make mean, fashion, median and standard deviation
dbo = sorted(db)
print('ROL:', dbo)
print('Lower value:', min(db))
print('Highest value:', max(db))
print('MEAN', statistics.mean(dbo))
print('MODE:', statistics.mode(dbo))
print('MEDIAN', statistics.median_grouped(dbo))
print('STANDARD DEVIATION', statistics.stdev(dbo))

# step 3 - calculate the sample span
aa = (max(db)) - (min(db))
print('Sample span:', aa)

# step 4: - Sturges rule  i = 1 + 3.3*log(n) n = sample size

import math

i = 1 + (3.3 * math.log(len(db), 10))
print('Number of classes:', i)

# step 5: class range amplitude rounded up h = AA/i
h = aa / i
print('Class range amplitude', math.ceil(h))

# step 6: build the table starting with the lowest value and adding (h) to each new class (i)
# classes
i1 = min(db) + math.ceil(h)
i2 = i1 + math.ceil(h)
i3 = i2 + math.ceil(h)
i4 = i3 + math.ceil(h)
i5 = i4 + math.ceil(h)
i6 = i5 + math.ceil(h)
i7 = i6 + math.ceil(h)

# step 7 - count the frequency of each class
f1 = []
f2 = []
f3 = []
f4 = []
f5 = []
f6 = []
f7 = []
for element in dbo:
    if element >= min(dbo) and element < i1:
        f1.append(element)
    if element >= i1 and element < i2:
        f2.append(element)
    if element >= i2 and element < i3:
        f3.append(element)
    if element >= i3 and element < i4:
        f4.append(element)
    if element >= i4 and element < i5:
        f5.append(element)
    if element >= i5 and element < i6:
        f6.append(element)
    if element >= i6 and element < i7:
        f7.append(element)

# step 8: build a data frame with the data above
print('xi = Grade midpoint')
print('fi = Frequency')
print('fa = Cumulative Frequency')
print('--------------------------------------------------------')
df = pd.DataFrame({'inferior limit': [min(dbo), i1, i2, i3, i4, i5, i6],
                   'upper limit': [i1, i2, i3, i4, i5, i6, i7],
                   'xi': [(min(dbo) + i1) / 2, (i1 + i2) / 2, (i2 + i3) / 2, (i3 + i4) / 2, (i4 + i5) / 2,
                          (i5 + i6) / 2, (i6 + i7) / 2],
                   'fi': [len(f1), len(f2), len(f3), len(f4), len(f5), len(f6), len(f7)],
                   'fa': [len(f1), len(f1 + f2), len(f1 + f2 + f3), len(f1 + f2 + f3 + f4), len(f1 + f2 + f3 + f4 + f5),
                          len(f1 + f2 + f3 + f4 + f5 + f6), len(f1 + f2 + f3 + f4 + f5 + f6 + f7)]})

df2 = pd.DataFrame({'xi*fi': df['xi'] * df['fi']})

# step 9: concatenate the data into a final data frame
df_result = pd.concat([df, df2], axis=1)
print(df_result)




































































