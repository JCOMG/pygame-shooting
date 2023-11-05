#抓取 ptt 電影版的網頁原始碼(HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html" 
#建立一個   Request物件，為了要讓我們更像人類所以要附加   Request Headers的資訊，所以就可以抓到資料了(會跑出一堆html格式的資料)
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"

})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
print(data)
print("...........................................................我是分割線")




#解析原始碼，取得每篇文章的標題
#解析的話需要第三方套件，要在終端機打 pip install beautifulsoup4 
import bs4 
root=bs4.BeautifulSoup(data,   "html.parser")
print(root.title)
print("...........................................................分割線")
print(root.title.string)
print("...........................................................分割線")
titles=root.find("div",class_="title")  #尋找class="title"的div標籤
print(titles)
print("...........................................................分割線")
print(titles.a.string)          # <a href="/bbs/movie/M.1597060781.A.785.html">[新聞] 經典重回大銀幕「全面啟動」10周年紀念版再度震撼</a>，(接下一行)
                                # 頭跟尾都有 a  所以titles.a.string裡才有a，string 是抓全面啟動只有抓到標題(接下一行)
                                # (因為時間上的關係所以找到的資料有可能不一樣的)
print("...........................................................分割線")
titles=root.find_all("div",class_="title")      #把所有的標題都印出來
print(titles)
print("...........................................................分割線")
for title in titles:                               #因為有些的標題可能會有(本文已被刪除)這種標題，所以要刪掉
    if title.a !=None:
        print(title.a.string)
