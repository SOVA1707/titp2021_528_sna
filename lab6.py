import numpy as np
import matplotlib.pyplot as plt

class Fuzzy:
    def __init__(self, scale=0, val=0):
        self.val = np.array(val) if isinstance(val, (list, np.ndarray)) else np.array([val])
        self.scale = np.array(scale) if isinstance(scale, (list, np.ndarray)) else np.array([scale])

    def __invert__(self):
        return Fuzzy(1-self.val)

    def __and__(self, other):
        return Fuzzy(np.minimum(self.val, other.val))

    def __or__(self, other):
        return Fuzzy(np.maximum(self.val, other.val))

    def __str__(self):
        return f"{self.val[0]}" if len(self.val)==1 else f"{self.val}"

    def __getitem__(self, key):
        return (self.scale[key], self.val[key])

def tramf(min_X, x1, x2, x3, x4, max_X, num=100):
    X = np.linspace(min_X, max_X, num, dtype = 'float32')
    Y = np.zeros_like(X)
    idx = (X >= x1) & (X <= x2); Y[idx] = (X[idx]-x1)/(x2-x1)
    idx = (X >  x2) & (X <= x3); Y[idx] = 1
    idx = (X >  x3) & (X <= x4); Y[idx] = (x4-X[idx])/(x4-x3)

    return X,Y
#Исходные данные к работе
#x = [1, 1.5, 2, 2.5, 3]
#y = [5, 5.5, 6, 7, 8]
#Обучающая выборка
xTrain = [1.00, 1.50, 2.00, 2.50, 3.00]
yTrain = [1.84, 2.04, 0.83, -2.58, -8.95]
#Тестовая выборка
xTest = [1.25, 1.75, 2.25, 2.75]
yTest = [2.10, 1.70, -0.55, -5.31]

#Этап 1. Фаззификация
(x1, y1) = tramf(1, 0.6, 0.8, 1.2, 1.4, 3, num = 210)
first = Fuzzy(x1, y1)

(x2, y2) = tramf(1, 1.1, 1.3, 1.7, 1.9, 3, num = 210)
second = Fuzzy(x2, y2)

(x3, y3) = tramf(1, 1.6, 1.8, 2.2, 2.4, 3, num = 210)
third = Fuzzy(x3, y3)

(x4, y4) = tramf(1, 2.1, 2.3, 2.7, 2.9, 3, num = 210)
four = Fuzzy(x4, y4)

(x5, y5) = tramf(1, 2.6, 2.8, 3.2, 3.4, 3, num = 210)
five = Fuzzy(x5, y5)

plt.plot(first.scale, first.val, '-', second.scale, second.val, '-', third.scale, third.val, '-', four.scale, four.val, '-', five.scale, five.val, '-')
plt.show()

#Этап 2. Вычисление выходов отдельных правил
#Правило 1: first -> 1.84
rule1 = first.val
P1=1.84
#Правило 2: second -> 2.04
rule2 = second.val
P2=2.04
#Правило 3: third -> 0.83
rule3 = third.val
P3=0.83
#Правило 4: third -> -2.58
rule4 = four.val
P4=-2.58
#Правило 5: third -> -8.95
rule5 = five.val
P5=-8.95

#Этап 3. Аккумуляция и композиция результатов
P = (P1 * rule1 + P2 * rule2 + P3 * rule3 + P4 * rule4 + P5 * rule5)/(rule1 + rule2 + rule3 + rule4 + rule5)
plt.plot(first.scale, P, '-')
plt.show()



 
