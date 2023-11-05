#抓取 Medium.com的文章資料
import urllib.request as req
url="https://medium.com/_/api/home-feed" 
#建立一個   Request物件，為了要讓我們更像人類所以要附加   Request Headers的資訊，所以就可以抓到資料了(會跑出一堆html格式的資料)
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"

})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")    #根據觀察，取得的資料是 json格式
print(data)
print("...........................................................我是分割線")




#解析json格式的資料，取得每篇文章的標題 
import json 
data=data.replace("])}while(1);</x>","")
data=json.loads(data)        #把原始的資料解析成字典/列表的表示形式
print(data)
print(".............................................................")

#取得json資料中的文章標題
posts=data["payload"]["references"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])
