'''Важно уметь отобразить данные уравнения на графике.
В качестве уравнения мы будем использовать очень известное уравнение: **$$E=mc^2$$**

С помощью Ваших знаний Numpy создайте два массива:


E и m:
значения m - это 11 равноотстоящих друг от друга чисел от 0 граммов до 10 граммов
значения E должны быть равны энергии для этих масс.

Вам нужно будет указать значение для c, приведя его в нужные единицы измерения -
в метрах в секунду, построить график, где ось X - масса в граммах, ось Y - энергия в Дж.
Также добавьте сетку для графика и сохраните изображение в формате svg.'''

import matplotlib.pyplot as plt
import numpy as np


m = np.arange(12)
C = 299792458
E = m*C**2
np.around(E, decimals=3, out=None)

print(E)

fig, axes= plt.subplots()

axes.plot(m, E)
axes.plot(m + 1, E + 1, color='g', label='2 grafic')

# С помощью методов set_ указываем атрибуты для осей
axes.set_xlabel('Ось X грамм')
axes.set_ylabel('Ось Y энергия ДЖ')
axes.set_title('Зависимость энергии от массы')

axes.legend()
axes.plot(m, E)
plt.savefig('grafic_energy.svg')
plt.show()