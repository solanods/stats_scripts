import pandas as pd
import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt


hotel = np.array(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10'])
peso_total = np.array([10.47, 19.85, 21.25, 24.36, 27.38, 28.09, 33.61, 35.73, 38.33, 49.14])
peso_papel = np.array([2.43, 5.12, 6.88, 6.22, 8.84, 8.76, 7.54, 8.47, 9.55, 11.43])
produto_pesos = peso_total * peso_papel
quadrados_pt = peso_total**2
quadrados_pp = peso_papel**2
n = len(hotel)

#calculate by the hand
coef_correl = (n * sum(produto_pesos) - sum(peso_total) * sum(peso_papel)) / (np.sqrt((n * sum(quadrados_pt) - (sum(peso_total)**2)) * (n * sum(quadrados_pp) - sum(peso_papel)**2)))

#the same but using scypy function
coef_pearson = sps.pearsonr(peso_total, peso_papel)

print('Coeficiente de correlação e P-Valor' , coef_pearson)

if abs(coef_pearson[0]) > 0.9:
    print('Correlação muito forte')
if 0.7 < abs(coef_pearson[0]) < 0.9:
    print('Correlação forte')
if 0.5 < abs(coef_pearson[0]) < 0.7:
    print('Correlação moderada')
if 0.3 < abs(coef_pearson[0]) < 0.5:
    print('Correlação fraca')
if 0 < abs(coef_pearson[0]) < 0.3:
    print('Correlação desprezível')

#linear regression y = ax + b  y=variavel dependente  x = variavel independente

a = (n * sum(produto_pesos) - sum(peso_total) * sum(peso_papel)) / (n * sum(quadrados_pt) - (sum(peso_total)**2))

x_ = sum(peso_total) / n
y_ = sum(peso_papel) / n

b = y_ - a * x_

print(a)
print(b)

#linear regression function
#estime o peso de papel para um peso total de 30
# y = ax +b
x = 30
y = a * x + b
print('Peso de papel estimado: ', y)

#the same using scipy

regress = sps.stats.linregress(peso_total,peso_papel)
print(regress)
print('(a, b, coeficiente de correl, p-valor e erro padrão)')

#plot
plt.plot(peso_total, peso_papel, 'o', label='original data')
plt.plot(peso_total, regress.intercept + regress.slope*peso_total, 'r', label='fitted line')
plt.legend()
plt.show()






















