#載入 pandas 模組
import pandas as pd 


# #基礎的篩選練習-Series
# data=pd.Series([30,15,20])
# condition=[True,False,True]     #代表我們要的只有30和20
# filteredData=data[condition]
# print(filteredData)



# #進階的運算符號比較後篩選-Series
# data=pd.Series([30,15,20])
# condition=data>18
# print(condition)




#字串篩選-Series
data=pd.Series(["您好","Python","Pandas"])
condition=[True,False,True]
filteredData=data[condition]
print(filteredData)





#上面那些都 只是概念，真正的code會是  
# data=pd.Series(["您好","Python","Pandas"])
# condition=data.str.contains("P")        #data裡的字串含有P的都把它篩選出來
# print(condition)
# filteredData=data[condition]
# print(filteredData) 



#真正在做code的會做     篩選練習-DataFrame
data=pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,50000,40000]
}
)
print(data)
print("...........................................")
condition=data["salary"]>=40000
print(condition)
print("...........................................")
filteredData=data[condition]
print(filteredData)
print("...........................................")
condition=data["name"]=="Amy"
print(condition)
filteredData=data[condition]
print(filteredData)