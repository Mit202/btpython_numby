import numpy as np

X = [1, 2, 3, 4, 5,1000,2000]
print("Mean X = ", np.mean(X))
print()

print("tính mean theo từng trục nếu là mảng nhiều chiều:")
print()
X = np.array([[1, 2], [3, 4]])
print("Mean X = ", np.mean(X))
print("Mean X với axis = 0: ", np.mean(X, axis=0))
print("Mean X với axis = 1: ", np.mean(X, axis=1))
print()
print("định dạng single precision (float32), mean có thể không chính xác với các mảng lớn:")
print()
a = np.zeros((2, 512 * 512), dtype=np.float32)
a[0, :] = 1.0
a[1, :] = 0.1

print("a.shape: ", a.shape)
print("mean a = ", np.mean(a))
print("mean a = ", np.mean(a, dtype=np.float64))