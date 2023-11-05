import pandas as pd 
#讀取資料
data=pd.read_csv("googleplaystore.csv", encoding='unicode_escape')     #把csv格式的檔案讀取成一個DataFrame,版本跟教學可能不一樣，需要用encoding='unicode_escape'


#觀察資料
print("資料數量",data.shape)
print("資料欄位",data.columns)
print(".........................................")



#分析資料 : 評分的各種統計數據
# print(data["Rating"])       #NaN是遺失的資料，4.1 3.9 4.7是goolge play store 裡應用程式的評分
# data["Rating"]=pd.to_numeric(data["Rating"].str.replace("Free","").replace("[,+]",""))
# print("平均數",data["Rating"].mean())           
# print("中位數",data["Rating"].median())
# print("前100個應用程式的平均",data["Rating"].nlargest(100).mean())
# print(".........................................")
# data["Rating"]=pd.to_numeric(data["Rating"].str.replace("[>,+]","").replace("Free",""))
# condition=data["Rating"]<=5
# data=data[condition]
# print("平均數",data["Rating"].mean())
# print("中位數",data["Rating"].median())
# print("前100個應用程式的平均",data["Rating"].nlargest(100).mean())



#分析資料 : 安裝數量的各種統計數據
# data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free","").replace("Photography","").replace("Paid",""))     #googleplaystore 有太多不乾淨的字，我們可以直接把他們給替換成空，就可以了
# print(data["Installs"])
# print("平均數",data["Installs"].mean())
# condition=data["Installs"]>100000
# print("安裝數量大於100000的應用程式有幾個",data[condition].shape)       #4919列 13欄
# print("安裝數量大於100000的應用程式有幾個",data[condition].shape[0])    #4919列(個)



#基於資料的應用: 關鍵字搜尋應用程式名稱
keyword=input("請輸入關鍵字:")
condition=data["App"].str.contains(keyword,case=False)              #應用程式的名稱App 是否包含使用者輸入的關鍵字  ，case=False 忽略大小寫
print(data[condition])                              #例如: 我打game 會跑出googleplaystoere裡的遊戲應用程式，一共有38個
print(data[condition]["App"])                       #例如: 我打game 只列出遊戲的名稱     
print("包含關鍵字的應用程式數量",data[condition].shape[0]) #38筆資料，13欄
