from matplotlib import pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

# task1
x = np.linspace(-10,10,100000)
def f(x):
    return x**2-4*x+4
y=f(x)
plt.plot(x,y,label='$f(x) = x^2 - 4x + 4$')
plt.title('Parabola')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

#task2
x = np.linspace(0,2*np.pi,10000)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.plot(x,y_sin,linestyle = '-',marker = 'o',color = 'r',label=r'$\sin(x)$')
plt.plot(x,y_cos,linestyle = '-',marker = 'o',color = 'b',label=r'$\cos(x)$')
plt.title('Sine and cosine functions')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()


#task3
x= np.linspace(0,10,1000)
def f(x):
    return x**3
def f2(x):
    return np.sin(x)
def f3(x):
    return np.exp(x)
def f4(x):
    return np.log(x+1)
y1 = f(x)
y2 = f2(x)
y3 = f3(x)
y4=f4(x)

plt.subplot(2, 2, 1)

plt.plot(x, y1, color='b')
plt.title(r'$f(x) = x^3$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(x, y2, color='r')
plt.title(r'$f(x) = \sin(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(x, y3, color='g')
plt.title(r'$f(x) = e^x$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(x, y4, color='m')
plt.title(r'$f(x) = \log(x+1)$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

#task4
x = np.random.uniform(0,10,100)
y = np.random.uniform(0,10,100)
plt.scatter(x, y, c=np.random.rand(100), marker='o', cmap='viridis', edgecolors='black')
plt.title('some random satter')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#task5
data = np.random.normal(0,1,1000)
plt.hist(data,bins = 30,color = 'blue',alpha = 0.5,edgecolor = 'black')
plt.title('some histogram')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


#task6
fig = plt.figure()
ax = plt.axes(projection = '3d')
x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
z = np.cos(x**2 + y**2)
ax.plot3D(x, y, z, color='b')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Line Plot of f(x, y) = cos(x² + y²)')

plt.show()

#task7
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = [200, 150, 250, 175, 225]
colors = ['red','black','blue','yellow','green']
plt.bar(products,values,color = colors)
plt.title('Sales Data')
plt.xlabel('Products')
plt.ylabel('sales')
plt.show()

#task8
categories = ['Product A', 'Product B', 'Product C']
time_periods = ['T1', 'T2', 'T3', 'T4']

category_A = [3, 5, 7, 6]
category_B = [4, 6, 5, 7]
category_C = [5, 3, 6, 8]

plt.bar(time_periods, category_A, label='Category A', color='red')
plt.bar(time_periods, category_B, bottom=category_A, label='Category B', color='blue')
plt.bar(time_periods, category_C, bottom=np.array(category_A) + np.array(category_B), label='Category C', color='green')

plt.xlabel("Time Periods")
plt.ylabel("Values")
plt.title("Stacked Bar Chart of Categories Over Time")
plt.legend()

plt.show()



