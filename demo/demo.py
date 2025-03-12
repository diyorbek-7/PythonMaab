# from matplotlib import pyplot as plt
# import numpy as np

# x = [1,2,3,4]
# y = [10,20,25,30]
# plt.plot(x,y)
# plt.show()

# a = [5,4,6,5,3,1]
# b = [4,5,69,8,7,4]
# c = [2,3,5,48]
# plt.plot(a,b,linestyle = '-.')
# plt.show()

# x = np.arange(-5,5,0.2)
# y = x**2
# plt.plot(x,y)
# plt.plot(x,x**3)
# plt.show()

# a = np.arange(50)
# b = np.random.randint(5,65,50)
# sizes = np.abs(np.random.randn(50))*100
# plt.scatter(a,b,s=sizes,c=b,cmap='cool')
# plt.colorbar()
# plt.show()

# categories = ['A','B','C','D']
# values1 = [10,15,7,12]
# values2 = [12,18,10,15]
# x = np.arange(len(categories))
#
# w = 0.4
# plt.bar(x-w/2,values1,width=w,label='Dataset 1',color = 'blue')
# plt.bar(x+w/2,values2,width=w,label='Dataset 2',color ='green')
# plt.xticks(x,categories)
# plt.yticks(x,categories)
# plt.title('Grouped Bar Chart')
# plt.xlabel('categories')
# plt.ylabel('values')
# plt.legend()
# plt.show()

# data = [1,1,1,2,2,3,3,4,4,4,4,4,5,6,9,9]
# plt.hist(data,bins = [1,2,3,4,5,6,7,10],color = 'orange',edgecolor = 'black')
# plt.show()

# import matplotlib.image as mpimg
# image = mpimg.imread('download.jpg')
# plt.imshow(image)
# plt.title('Car')
# # plt.axis('off')
# plt.show()

# image = np.random.random((10,10))
# plt.imshow(image)
# plt.colorbar()
# plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Define x values from 0 to 2π
x = np.linspace(0, 2 * np.pi, 1000)

# Compute sine and cosine values
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot sine function
plt.plot(x, y_sin, linestyle='-', marker='o', color='b', label=r'$\sin(x)$')

# Plot cosine function
plt.plot(x, y_cos, linestyle='--', marker='s', color='r', label=r'$\cos(x)$')

# Customize the plot
plt.title('Sine and Cosine Functions')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

