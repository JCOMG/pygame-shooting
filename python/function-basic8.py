#定義函式
#def multiply(): #  函式內部的程式碼如果沒有做呼叫就不會執行
 #   print(3*4)
#呼叫函式
#multiply()






# def multiply(n1,n2):
#     print(n1*n2)
# multiply(3,4)
# multiply(4,8) 






def multiply (n1,n2):
    print (n1*n2)
    return
value=multiply(3,4)     #multiply(3,4)會跑回第22行的def multiply(n1,n2)，並且印出12，但是return None回給multiply(3,4)
print(value)            #所以multiply(3,4)為None，會印出12 和   None 






#定義函式

# def multiply(n1,n2):
#     print(n1*n2)
#     return 100    #return 100 就會列印出100不管前面的print(n1*n2)，還是會列印出3*4=12
# #呼叫函式
# value=multiply(3,4)
# print (value)
#multiply(5,6)
#multiply(8,9)



#定義函式

#def multiply(n1,n2):
 #   print(n1*n2)
  #  return n1*n2
#呼叫函式
#value=multiply(3,4)+multiply(10,5)
#print (value)




#程式的包裝
# def calculate():
#     sum=0                       #28~31是在加1~10喔
#     for n in  range (1,11):
#         sum=sum+n
#     print (sum)

# calculate()



# def calculate(max):
#     sum=0                      
#     for n in  range (1,max+1):
#         sum=sum+n
#     print (sum)

# calculate(20)

