#載入pandas 模組
import pandas as pd
#資料索引
# data=pd.Series([5,4,-2,3,7])        #不換索引的話，預設是0,1,2,3，可以把它換成a,b,c,d
# data=pd.Series([5,4,-2,3,7],index=["a","b","c","d","e"])
# print(data)



#觀察資料
# print("資料型態",data.dtype)
# print("資料數量",data.size)
# print("資料索引",data.index)



#取得資料:  根據順序、根據索引，0代表第1列 2代表第3列
# print(data[2],data[0])
# print(data["e"],data["d"])


#數字運算:  基本、統計、順序
# print("最大值",data.max())
# print("總和",data.sum()) 
# print("標準差",data.std())
# print("中位數",data.median())
# print("最大的前3個數",data.nlargest(3))



#字串運算:  基本、串接、搜尋、取代
data=pd.Series(["您好","PYTHON","Pandas"])
print(data)
print("............................................................")
print(data.str.lower())     #把字串全部都變小寫，中文不受限制
print("............................................................")
print(data.str.len())       #算出每個字串的長度
print("............................................................")
print(data.str.cat(sep=","))    #把字串串起來，可以自訂串接的符號，所以會變成 您好，PYTHON，Pandas
print("............................................................")
print(data.str.contains("P"))   #確認字串中是否有包含大寫P，會跑出布林值
print("............................................................")
print(data.str.replace("您好","Hello"))     #會把 您好換成Hello




