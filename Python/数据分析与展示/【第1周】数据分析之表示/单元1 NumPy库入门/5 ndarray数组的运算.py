import numpy as np
#计算a与元素平均值的商
a = np.arange(24).reshape((2,3,4))
print("array:\n",a)
print("平均数:\n",a.mean())
a = a / a.mean()
print("运算商:\n",a)
#Numpy一元函数实例
a = np.arange(24).reshape((2,3,4))
a = np.square(a)
print("Square:\n",a)
a = np.sqrt(a)
print("Sqrt:\n",a)
a = np.rint(a)
print("rint:\n",a)
a = np.modf(a)
print("Modf:\n",a)
#Numpy二元函数实例
a = np.arange(24).reshape((2,3,4))
b = np.sqrt(a)
print("a:\n",a)
print("b:\n",b)
c = np.maximum(a,b)
print("c:\n",c)
print("a > b\n",b>b)
