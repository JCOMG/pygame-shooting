#網路連線
# import urllib.request as request
# src="https://www.ntu.edu.tw" 
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8")        #臺灣大學的網站的原始碼(HTML、JS、CSS)前端工程
# print(data)


# import urllib.request as request
# import json
# src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire" 
# with request.urlopen(src) as response:
#     data=json.load(response)        #利用json模組處理json資料格式    
# print(data)




# import urllib.request as request
# import json
# src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire" 
# with request.urlopen(src) as response:
#     data=json.load(response)        #利用json模組處理json資料格式    
# #將公司名稱列印出來
# clist=data["result"]["results"]        #根據網站裡的資料槓桿取，網址裡有result還有results我們對其他東西不感興趣對results感興趣而已
# print(clist)                           #從一堆result裡面我們只要公司名稱




# import urllib.request as request
# import json
# src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire" 
# with request.urlopen(src) as response:
#     data=json.load(response)            
# #將公司名稱列印出來
# clist=data["result"]["results"]        
# for company in clist:
#     print(company["公司名稱"])      #會只有印公司名稱





import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire" 
with request.urlopen(src) as response:
    data=json.load(response)            
#將公司名稱列印出來
clist=data["result"]["results"]
with open("data.txt","w",encoding=("utf-8"))as file:     
    for company in clist:
        file.write(company["公司名稱"]+"\n")        #在這個程式碼裡新增一個文字檔，然後將公司名稱全部打進去裡面
