# import random       #隨機模組
# data=random.choice([1,5,6,10,20])    #隨機選取
# print(data)                          #每一次的隨機亂數都不一樣

# import random 
# data=random.sample([1,5,6,10,20],3)     #從[1,5,6,10,20]裡選取3個隨機變數
# print(data)


# import random
# data=[1,5,8,20]
# random.shuffle(data)            #隨機調換模組(就是洗牌的概念)
# print(data)

# import random
# data=random.random()        #0~1之間的隨機亂數
# print(data) 


# import random  
# data=random.uniform(60,100)     #60~100之間的隨機亂數     
# print(data)


#取得常態分配亂數
#平均數100,標準差10,得到的資料大部分都在"90~110"之間
# import random
# data=random.normalvariate(100,10)
# print(data)




import statistics as stat
data=stat.mean([1,4,5,8])       #算出平均數
print(data)
data=stat.median([1,2,3,4,5,8,100]) #算出中位數
print(data)
data=stat.stdev([1,2,3,4,5,8,100])     #算出標準差
print(data)
 