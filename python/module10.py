#建立內建 sys 模組並取得資訊
import sys as s     #將sys取名叫s這個名字  
print(s.platform)
print(s.maxsize)
# # 建立 geometry 模組，載入使用
# import geometry                         #載入 模組名稱
# result=geometry.distance(1,1,5,5)       #模組名稱(geometry.py).模組中的參數(n1,n2,n3,n4))
# print(result)  
# result=geometry.slope(1,2,5,6)
# print(result)                    # import 的東西筆電可能跑不出來，如果跑步出來請按deug中的start debug or without debug就可以了



# # 調整搜尋模組的路徑
# import sys
# print(sys.path) #印出模組的搜尋路徑 (會是一大串的列表)



# import sys 
# sys.path.append("modules")      #python 底下有很多東西modules就是工具資料夾，而底下的condition.py,def.py等等都是主程式
# print(sys.path)                 #這樣用就是可以非常精簡將主程式跟工具分開來部會搞混，如果不打sys.path.append("modules"),那程式會找不到geometry因為他在modules的資料夾所以會需要sys.path.append("modules")
# print("--------------")
# import geometry 
# print(geometry.distance(1,1,5,5))
