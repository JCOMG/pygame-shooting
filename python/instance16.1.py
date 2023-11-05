# class point:                                        #point 實體物件的設計: 平面座標上的點
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def show(self):                                 #定義實體方法
#         print(self.x,self.y)
# p=point(3,4)
# print(p.x,p.y)











# class point:                                        #point 實體物件的設計: 平面座標上的點
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def show(self):                                 #定義實體方法(self 是預設的)
#         print(self.x,self.y)
#     def distance(self,x1,y1):
#         return (((self.x-x1)**2+(self.y-y1)**2)**0.5)
# p=point(3,4)
# p.show()
# result=p.distance(0,0)
# print(result)







file 實體物件的設計: 包裝檔案讀取的程式
class file:
    def __init__(self,name):
        self.name=name 
        self.file= None #尚未開啟檔案，初期是None
    def open (self):
        self.file=open(self.name,mode="r", encoding="utf-8")    #open(self.name,mode="r", encoding="utf-8")是python 内建打開檔案的函式
    def read(self):
        return self.file.read()     #self.file.read()會把檔案中的物件讀取出來
#先創立一個檔案 ex: data1.txt，內容是哈哈哈哈之類的，要記得案ctrl+s做儲存的動作
#再讀取第一個檔案
f1=file("data1.txt")            #建立檔案的實體物件
f1.open()                       #呼叫open的實體方法
data=f1.read()                  #在呼叫read的實體方法
print(data)                     #再把檔案給讀取出來
#讀取第二個檔案
f1=file("data2.txt")
f1.open()
data=f1.read()
print(data)
