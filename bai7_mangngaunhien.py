import numpy as np

print("numpy.random.rand")
a = np.random.rand()
b = np.random.rand(4)
c = np.random.rand(2, 3)
print("a = ", a)
print("b = ", b)
print("c = ", c)
print()
print("numpy.random.seed")
g = np.random
g.seed(10)
print("g rand: ", g.rand())
print()
print("numpy.random.normal ")
mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, size=5)
print(s)
print()
print("numpy.random.randn ")
s = np.random.randn(3,3)
print(s)