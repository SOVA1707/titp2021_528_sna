import matplotlib.pyplot as plt
import numpy
            
###main###
x = []
y = []

f = open('lab2.txt')
xy = f.read().split('\n')
f.close()
sx = xy[0].split(', ')
sy = xy[1].split(', ')
for i in sx:
    x.append(float(i))
for i in sy:
    y.append(float(i))

#1
X = []
for i in range(659):
    X.append(i/100)
X = numpy.array(X)
#2
t = numpy.polyfit(x, y, 2)
Y = numpy.poly1d(t)
#3
plt.plot(x, y, 'o', X, Y(X), '-')
plt.show()
#4
ff = open('lab2_out.txt', 'w')

for i in X:
    ff.write(str(i) + ' ')
ff.write('\n')
for i in Y(X):
    ff.write(str(i) + ' ')

ff.close()
