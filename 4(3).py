import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy

#тут определяем функцию
#эта функция на вывод этих значений 0,1,2,5,10
#мы передаём функцию f на вход
#далее она вызывается
def prin(f):
    print('---')
    print('f(0)= ' + str(f(0)))
    print('f(1)= ' + str(f(1)))
    print('f(2)= ' + str(f(2)))
    print('f(5)= ' + str(f(5)))
    print('f(10)= ' + str(f(10)))
    print('---')

#1.1
#тут мы определяем функцию графика
    #
def f1(x):
    if x > 1:
        return 0.5*(x-1)
    return 0
#определяем значения x и y
x = []
y = []
for i in range(101):
    x.append(i/10)
    y.append(f1(x[-1]))
    #выводим значения 0,1,2,5,10
prin(f1)
#выводим графики
#далее всё аналогично
plt.plot(x,y, '-')
plt.show()

#1.2
def f2(x):
    if x>2:
        return -0.3*(x-2)+1
    return 1

x = []
y = []
for i in range(101):
    x.append(i/10)
    y.append(f2(x[-1]))
prin(f2)
plt.plot(x,y, '-')
plt.show()


#1.3
def f3(x):
    if x > 1 and x < 3:
        return 0.5*(x-1)
    else: return 0

x = []
y = []
for i in range(101):
    x.append(i/10)
    y.append(f3(x[-1]))
prin(f3)
plt.plot(x,y, '-')
plt.show()


#1.4
x1 = []
y1 = []
for i in range(101):
    x1.append(i/10)
    y1.append(f2(x1[-1]))

x2 = []
y2 = []
for i in range(101):
    x2.append(i/10)
    y2.append(f3(x2[-1]))
plt.plot(x1, y1, '-', x2, y2, '-')
plt.show()

#1.5
def f5(x):
    n1 = f2(x)
    n2 = f3(x)
    if n1<n2:
        return n1
    else:
        return n2

x = []
y = []
for i in range(101):
    x.append(i/10)
    y.append(f5(x[-1]))
prin(f5)
plt.plot(x,y, '-')
plt.show()

#1.6
def f6(x):
    n1 = f2(x)
    n2 = f3(x)
    if n1>n2:
        return n1
    else:
        return n2
    
x = []
y = []
for i in range(101):
    x.append(i/10)
    y.append(f6(x[-1]))
prin(f6)
plt.plot(x,y, '-')
plt.show()



#2.6
#тут мы забиваем значения наблюдей за погодой: тепература, осадки, скорость ветра
temp = [-17.8, -14.4, -6.4, 2.5, 10.2, 15.4, 18.3, 15.8, 9.1, 1.8, -7.6, -15.3]
osad = [13, 8, 12, 18, 37, 78, 114, 91, 52, 21, 20, 16]
wind = [1.8, 1.9, 2.2, 2.6, 2.5, 2.1, 1.7, 1.8, 2.0, 2.1, 1.9, 1.6]


e1_t = [17, 30, 3, 20, -20, 7]
e1_t_o = [] #эксперт 1. температура
e2_t = [13, 30, 6, 16, -20, 8]
e2_t_o = []
e3_t = [14, 30, 6, 18, -20, 10]
e3_t_o = []
e4_t = [15, 30, 4, 17, -20, 6]
e4_t_o = []

e1_o = [50, 120, 30, 65, 0, 40]
e1_o_o = []
e2_o = [60, 120, 35, 70, 0, 40]
e2_o_o = [] #эксперт 2 осадки
e3_o = [65, 120, 38, 80, 0, 50]
e3_o_o = []
e4_o = [70, 120, 45, 85, 0, 55]
e4_o_o = []

e1_w = [1.2, 3.0, 0.6, 1.3, 0.0, 0.8]
e1_w_o = []
e2_w = [1.0, 3.0, 0.5, 1.2, 0.0, 0.6]
e2_w_o = []
e3_w = [1.1, 3.0, 0.6, 1.4, 0.0, 0.9]
e3_w_o = []
e4_w = [0.9, 3.0, 0.3, 1.5, 0.0, 0.8]
e4_w_o = []

#тут мы вычисляем оценки: если находится в промежутке, то ставим единичку. Затем возвращаем результат, например, [1, 0, 0]
def ocenki(x, beetwen):
    result = [0, 0, 0]
    if x > beetwen[0] and x <beetwen[1]:
        result[0] = 1
    if x > beetwen[2] and x <beetwen[3]:
        result[1] = 1
    if x > beetwen[4] and x <beetwen[5]:
        result[2] = 1
    return result
#тут вычисляем уже оценки, забиваем их в массивы
for i in temp:
    e1_t_o.append(ocenki(i,e1_t))
    e2_t_o.append(ocenki(i,e2_t))
    e3_t_o.append(ocenki(i,e3_t))
    e4_t_o.append(ocenki(i,e4_t))

for i in osad:
    e1_o_o.append(ocenki(i,e1_o))
    e2_o_o.append(ocenki(i,e2_o))
    e3_o_o.append(ocenki(i,e3_o))
    e4_o_o.append(ocenki(i,e4_o))

for i in wind:
    e1_w_o.append(ocenki(i,e1_w))
    e2_w_o.append(ocenki(i,e2_w))
    e3_w_o.append(ocenki(i,e3_w))
    e4_w_o.append(ocenki(i,e4_w))

n_t = []
nu_t = []
n_o = []
nu_o = []
n_w = []
nu_w = []
#суммируем оценки. затем находим среднее. Там в документе 3/5. И так для всех находим
for i in range(len(temp)):
    n_t.append([e1_t_o[i][0] + e2_t_o[i][0] + e3_t_o[i][0] + e4_t_o[i][0], e1_t_o[i][1] + e2_t_o[i][1] + e3_t_o[i][1] + e4_t_o[i][1], e1_t_o[i][2] + e2_t_o[i][2] + e3_t_o[i][2] + e4_t_o[i][2]])
    nu_t.append([n_t[-1][0]/4, n_t[-1][1]/4, n_t[-1][2]/4])
for i in range(len(osad)):
    n_o.append([e1_o_o[i][0] + e2_o_o[i][0] + e3_o_o[i][0] + e4_o_o[i][0], e1_o_o[i][1] + e2_o_o[i][1] + e3_o_o[i][1] + e4_o_o[i][1], e1_o_o[i][2] + e2_o_o[i][2] + e3_o_o[i][2] + e4_o_o[i][2]])
    nu_o.append([n_o[-1][0]/4, n_o[-1][1]/4, n_o[-1][2]/4])
for i in range(len(wind)):
    n_w.append([e1_w_o[i][0] + e2_w_o[i][0] + e3_w_o[i][0] + e4_w_o[i][0], e1_w_o[i][1] + e2_w_o[i][1] + e3_w_o[i][1] + e4_w_o[i][1], e1_w_o[i][2] + e2_w_o[i][2] + e3_w_o[i][2] + e4_w_o[i][2]])
    nu_w.append([n_w[-1][0]/4, n_w[-1][1]/4, n_w[-1][2]/4])

x = []
y1 = []
y2 = []
y3 = []
#12 месяцев в году. 12 элементов в исходных массивах
for i in range(12):
    x.append(i+1)
    y1.append(nu_t[i][0])
    y2.append(nu_t[i][1])
    y3.append(nu_t[i][2])
    #добавить в массив. у нас массивы пустые. мы в них добавляем элементы. там хз, я где-то ошибся)
xx = numpy.array(temp)
yy1 = numpy.array(y1)
yy2 = numpy.array(y2)
yy3 = numpy.array(y3)
#аппроксимируем
t = numpy.polyfit(xx, yy1, 3)
f1 = numpy.poly1d(t)
t = numpy.polyfit(xx, yy2, 3)
f2 = numpy.poly1d(t)
t = numpy.polyfit(xx, yy3, 5)
f3 = numpy.poly1d(t)
#строим
plt.plot(f1(xx), '-', f2(xx), '-', f3(xx), '-')
plt.show()
