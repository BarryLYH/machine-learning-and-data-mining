import pandas as pd

p = pd.read_csv('/users/barry/desktop/sampling.csv', encoding = "ISO-8859-1")

num = [949, 1312, 1149, 1212, 979, 1153, 1361, 1478, 1425, 1233, 1307, 1557, 1412, 996, 1500, 991, 1234, 926, 1159, 803, 1036, 1285, 1542, 1548, 1030, 1474, 1015, 1463, 784, 975, 1355, 1427, 1032, 1521, 1124, 1358, 1259, 1034, 995, 1040, 792, 1367, 1485, 1063, 1430, 1456, 893, 790, 798, 1202, 1365, 1530, 1089, 1253, 1337, 1495, 1099, 1445, 1560, 845, 1482]


list = []

wp = p.to_dict(orient="list")

for i in range(len(num)):
    list.append(wp['Name'][num[i]])

print(list)