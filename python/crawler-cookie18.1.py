#一開始可能沒辦法抓到，因為ptt八卦版裡面有限制說是否滿18歲
#抓取 ptt 八卦版的網頁原始碼(HTML)
#接下要做包裝的部分，讓程式碼變得漂亮一點
import urllib.request as req
#主程式:    抓取多個頁面的標題
def getData(url):   #   要記得把程式碼縮排一下
    url="https://www.ptt.cc/bbs/Gossiping/index.html" 
    #建立一個   Request物件，為了要讓我們更像人類所以要附加   Request Headers的資訊，所以就可以抓到資料了(會跑出一堆html格式的資料)
    request=req.Request(url,headers={
        "cookie":"over18=1",        #我們要連線八卦版裡面的限制是否滿18歲
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
    # print(root.title)
    # print("...........................................................分割線")
    # print(root.title.string)
    # print("...........................................................分割線")
    titles=root.find("div",class_="title")  #尋找class="title"的div標籤
    print(titles)
    print("...........................................................分割線")
    # print(titles.a.string)          # <a href="/bbs/movie/M.1597060781.A.785.html">[新聞] 經典重回大銀幕「全面啟動」10周年紀念版再度震撼</a>，(接下一行)
                                    # 頭跟尾都有 a  所以titles.a.string裡才有a，string 是抓全面啟動只有抓到標題(接下一行)
                                    # (因為時間上的關係所以找到的資料有可能不一樣的)
    print("...........................................................分割線")
    titles=root.find_all("div",class_="title")      #把所有的標題都印出來
    print(titles)
    print("...........................................................分割線")
    for title in titles:                               #因為有些的標題可能會有(本文已被刪除)這種標題，所以要刪掉
        if title.a !=None:
            print(title.a.string)
    print("...........................................................分割線")
    #擷取上一頁的連結
    nextLink=root.find("a",string="‹ 上頁")  #找到內文是‹ 上頁的 a 標籤
    return nextLink["href"]     #抓取href這個屬性的網址
# 抓取一個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html" 
pageURL="https://www.ptt.cc/"+getData(pageURL)          #這樣就是一個完整的超連結
print(pageURL)
print("...........................................................分割線")
count=0
while count<3:
    pageURL="https://www.ptt.cc/"+getData(pageURL)          #可以抓到八卦坂里網頁的前三頁的資料，因為每前一頁的網址都不一樣
    count+=1
