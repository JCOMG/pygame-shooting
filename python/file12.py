# file=open("data.txt",mode="w")      #開啟
# file.write("Hello File\nSecond line")#操作，現在的狀態只能打英文，打中文會有亂碼
# file.close()                        #關閉   



# file=open("data.txt",mode="w",encoding="utf-8")          #多打encoding="utf-8"就可以讓中文不會是亂碼
# file.write("測試中文\n好棒棒喔")
# file.close()   



# with open ("data.txt",mode="w",encoding="utf-8")as file:        #增加 with可以自動安全的關閉檔案 寫入檔案
#     file.write("測試中文\n好棒棒喔")
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     data=file.read()                                            #將寫入檔案的東西存放到data，並把它顯示到終端機上
# print(data)



#把檔案中的數字資料做，一行一行的讀取出來，並計算出總和
# with open ("data.txt",mode="w",encoding="utf-8") as file:
#     file.write("5\n3")                  #首先將5打出來，換行，然後打3，
# sum=0
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     for line in file:                   #將數字資料一行一行的讀取
#         sum+=int(line)                  #5跟3其實還是字串，所以要先將字串轉換成整數(int)，並加到總合
# print(sum)



# import json
# with open ("config.json",mode="r") as file:
#     data=json.load(file)
# print(data)     #data是一個字典資料
# print("name: ",data["name"])
# print("version: ",data["version"])


# import json
# with open ("config.json",mode="r") as file:
#     data=json.load(file)
# print(data)
# data["name"]="New Name"     #修改變數中的資料
# #把最新的資料複寫回去給檔案(config.json)中，不會出現在下列的terminal裡
# with open ("config.json",mode="w")as file:
#     json.dump(data,file)


