import numpy as np

freetuts_ages = [19, 33, 51, 22, 18, 13, 45, 24, 58, 11, 25, 27, 26, 29]

print("Phương sai: ", np.var(freetuts_ages))
print("Độ lệch chuẩn: ", np.std(freetuts_ages))
print()
print("Xử lý nan trong var và std")
print()
a = np.array([1, np.nan, 3, 4])
print("var = ", np.var(a))
print("std = ", np.std(a))
print("nanvar = ", np.nanvar(a))
print("nanstd = ", np.nanstd(a))