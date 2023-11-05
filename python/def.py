# def add(n1,n2):                 #程式運作的步驟1:定義一個函式，add是個名字(n1=參數值，n2=參數值)，名字隨便定義但只限英文字母
#     result=n1+n2                #程式運作步驟3:將設定好的參數值存放到result，return result 就是將result裡的東西回傳回去
#     return result               #回傳到value=add(3,5)
# value=add(3,5)                  #程式的運作步驟2:將定義的函式跟參數值(想要什麼數字都可以)存放到value
# print(value)                    #程式的運作步驟4:將value這個值給印出來

# def iloveu(n1,n2):
#     result=n1*n2
#     return result                            #不加return 是不會回傳任何東西，會回傳None

# value=iloveu(5,6)
# print(value)


# def jimmy(n1,n2):
#     print(n1*n2)                
#     return 10
# value=jimmy(5,6)
# print(value)


#程式的包裝
def all(number):
    sum=0
    for n in range (1,number+1):
        sum=sum+n
    print(sum)
all(10)
all(11)
