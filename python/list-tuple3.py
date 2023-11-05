# 可變動列表 List
grades = [12, 60, 15, 70, 90]
grades[1:4] = []  # 連續刪除列表中從索引1~4(不包含編號4的資料)
print(grades)
grades = grades+[12, 33]
print(grades)
length = len(grades)
print(length)
data = [[3, 4, 5], [6, 7, 8]]
print(data)
# 不可變動列表 Tuple
data = (3, 4, 5)
data[0] = 5  # 錯誤，tuple 的資料不可以變動
print(data)  # 所以會印不出來
