# #簡單複習
# def  say(msg="Hello"):      #定義函式
#     print(msg)
# say()                       #呼叫函式





#參數的預設資料
# def power (a,b=0):
#     print(a**b) #a的b次方
# power (3,2)
# power (4)   #沒有給b的數值時，就用def裡的b的參數值，就是b=0


# #使用參數名稱對應
# def divide(n1,n2):
#     print(n1/n2)
# divide(3,4)
# divide(n2=4,n1=2)


# def average(*numbers):      #無限參數資料，就是你想放多少資料都可以
#     print(numbers)
# average(3,4)
# average(6,-7,0.5)
# average(10,11,13,14)




# #無限參數資料
# def avg(*numbers):
#     sum=0
#     for n in numbers :
#          sum=sum+n 
#     print(sum/len(numbers))     #算出平均數
# avg(3,4)
# avg(3,4,5)
# avg(-1,8,0,23)




