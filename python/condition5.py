#if False:
    #print("True執行")#只要判斷式是false，直接執行else
#else:
    #print("False 執行")
    #if 布林值:     elif 布林值:    else:布林值:

#x=input("輸入數字")     #基本型態都是字串型態
#x=int(x)    #轉換為整數型態
#x = int(input(x))    #整數型
#if x>200:
    #print("大於200")
#elif x>150:
    #print("大於100,小於200")

#else:
 #   print("小於等於100")

 #四則運算
n1=int(input("請輸入數字一: "))
n2=int(input("請輸入數字二:"))
op=input("+,-,*,/")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/": 
    print(n1/n2)
else:
    print("不支援的運算")


