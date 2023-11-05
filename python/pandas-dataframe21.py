#載入pandas模組
import pandas as pd 


#資料索引
data=pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":["30000","50000","40000"]
},index=["a","b","c"])
print(data)
# print("..............................................")
# print("資料數量",data.size)
# print("資料形狀(列、欄)",data.shape)
# print("資料索引",data.index)



# # 取得到(Row/橫向)的Series資料:     根據順序、根據索引
# print("取得第2列",data.iloc[1],sep="\n")     #根據單純的順序，取得第2列的資料
# print(".................................................")      
# print("取得到第c列的",data.loc["c"],sep="\n")       #根據「索引」所取得的資料，取得第3列的資料

 

#取得(Colume/直向)的Series資料:     根據欄位的名稱
# print("取得name欄位",data["name"],sep="\n")
# names=data["name"]      #取得單維度的Series資料
# print("把 name 全部轉成大寫的",names.str.upper(),sep="\n")
# salaries=data["salary"]
# print("計算員工的平均數",salaries.mean())



#建立新的欄位
data["revenue"]=[500000,400000,300000]     #data[新欄位的名稱]=列表
print(data)
data["rank"]=pd.Series([3,6,1],index=["a","b","c"])        #rank隨便排沒差    data[新欄位名稱]=Series的資料
print(data)
data["salary"]=pd.Series([30000,50000,40000],index=["a","b","c"])
data=data["revenue"]/data["salary"]
print(data)
