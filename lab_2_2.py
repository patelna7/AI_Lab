import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 

fig = plt.figure(figsize = (4,4))
ax = fig.add_subplot()
plt.xlim(0,1)
plt.ylim(0,1)

sx = np.arange(0,5,0.1)
sy = np.array([np.sin(a) for a in sx])

n = 1000
x_min, x_max = 0.0, 1.0
y_min, y_max = 0.0, 1.0

x = np.arange(0.00, float(n), 1)
y = np.arange(0.00, float(n), 1)
count = 0
for i in range(0,int(n)):
    x[i] = random.uniform(x_min, x_max)
    y[i] = random.uniform(y_min, y_max)

    if np.sin(x[i]) > y[i]:
        count += 1
        ax.scatter(x[i],y[i],color='red')
    else:   
        ax.scatter(x[i],y[i],color='blue')
ax.grid()
plt.plot(sx,sy,'r')
integral_value = (count / float(n))
print ('Площа = '+str(integral_value))
print ('Абсолютна похибка = '+str(np.abs(0.45969769413186-integral_value)))

plt.show()
integral_value = count / float(n)
