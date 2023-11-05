#載入pandas 模組
import pandas as pd 
#建立series 
data=pd.Series([20,10,15])
#基本Series操作
# print(data)
# print (data.max())
# print(data.median())
#進階一點的series 操作
# data=data==20               # 跟data裡的數字做比較，會產生布林值
# print(data)

#建立一個DataFrame
data=pd.DataFrame ({
    "name":["Amy","John","Bob"],
    "salary":[30000,50000,40000]

})  
#基本DataFrame操作
# print(data)
# #取得特定的欄位
# print (data["name"])

#取得特定的列
print(data)
print("......................")
print(data.iloc[0])             #印出第1列
print(data.iloc[1])             #印出第2列