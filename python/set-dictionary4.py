#集合的運算
#s1={3,4,5}
#print(10  not in s1)
#s1={3,4,5}
#s2={4,5,6,7}
#s3=s1&s2   交集: 取兩個集合中，相同的資料
#s1|s2      聯集: 取兩個集合中的所有資料，但不重複取
#s3=s1-s2 #差集: 從s1中，減去和s2重疊的部分(意思就是指s1獨有的資料)
#print(s3)
#s3=s1^s2    #反交集: 取兩個集合中，不重疊的部分(意思是指s1和s2各自獨有的資料)
#print(s3)
#s=set("Hello")          #把字串中的字母拆解成集合:  set (字串)   
#print(s)        #沒有順序性
#print('H' in s)
#字典運算:key-value的配對(ex:apple是key，蘋果是value)
dic={"apple":"蘋果","bug":"蟲蟲"}   
print(dic["apple"])
del dic["apple"]    #刪除字典中的鍵值對(key-value pair)
print (dic)
dic={x:x*2 for x in [3,4,5]}   # for 任何未知數 in 列表 這是固定的!無法變動，這叫做從列表的資料產生資料
print(dic)























