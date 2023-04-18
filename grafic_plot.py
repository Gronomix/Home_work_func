'''С помощью объектно-ориентированного подхода создайте 4 графика (разместите их в рамках одного изображения)
установите сетку и легенду для каждого из графиков.
для первых 2 графиков(графики А и B) используйте рандомно сгенерированные массивы Numpy в качестве данных для осей X и Y.
Графики С и D должны демонстрировать обратную пропорциональность графикам A и B.
'''

import matplotlib.pyplot as plt
import numpy as np
import math
import plotly


X = np.arange(0, math.pi * 2, 0.05)


y = np.sin(X)
z = np.cos(X)
k = np.exp(y)
j = np.exp(z)
fig, xy = plt.subplots()

xy.plot(X, y, color='r', label='sin')
xy.plot(X, z, color='g', label='cos')
xy.plot(X, k, color='b', label='sin.transpose')
xy.plot(X, j, color='c', label='cos.transpose')

xy.set_xlabel("Angle")
xy.set_ylabel("Magnitude")
xy.set_title("Sine and Cosine functions")


xy.legend()
plt.savefig('grafic.png')
plt.show()