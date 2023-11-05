# Point 實體物件的設計: 平面座標上的點
# class point:
#     def __init__(self):                                  # (2條喔)__init__，固定的名字，代表著初始化的函式
#         self.x=4
#         self.y=5
# # 建立第一個實體物件
# p1=point()                                               #要產生的實體物件
# print(p1.x , p1.y)                                       #實體物件(p1).屬性名稱(x and y)
# #建立第二個實體物件
# p2=point()
# print(p2.x , p2.y)



# class point:
#     def __init__(self , x , y):                                 
#         self.x=x
#         self.y=y
# # 建立第一個實體物件
# p1=point(3,4)                                               
# print(p1.x , p1.y)                                      
# #建立第二個實體物件
# p2=point(5,6)
# print(p2.x , p2.y)





# # Full name 實體物件的設計: 分開紀錄姓、名資料的全名
# class Fullname:
#     def __init__(self):
#         self.firstname ="Jimmy"
#         self.lastname ="Chuang"
# name1=Fullname()
# print(name1.firstname , name1.lastname )






class Fullname:
    def __init__(self,firstname,lastname):
        self.firstname =firstname 
        self.lastname =lastname
name1=Fullname("Jimmy","Chuang")
print(name1.firstname , name1.lastname )
name2=Fullname("Eunice","Tang")
print(name2.firstname , name2.lastname)

















