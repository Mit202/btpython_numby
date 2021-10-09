import numpy as np

print("random.randint")
np.random.randint(0, 2)
coins = np.random.randint(2, size=1000)
print(coins.shape)
print("tính phần trăm ")
print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)
print()
print("random.choice")
coins = np.random.choice([0, 1], size=1000, p=[0.2, 0.8]) # random.choice sẽ lấy ngẫu nhiên các phần tử trong mảng ở tham số đầu tiên với xác suất ở tham số p
print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)
print()
print("random.binomial")
np.random.binomial(20, 0.5,10)
print("Trung bình số mặt ngửa nhận được khi tung đồng xu 20 lần trong vòng 10 lần lặp: ", np.random.binomial(20, 0.5, 10).mean())
print()
print("random.binomial cách 2")
n = 10
p = 0.2  
l = 1000
b = np.random.binomial(n, p, l)
print("Trung bình số mặt ngửa nhận được: ", b.mean())
