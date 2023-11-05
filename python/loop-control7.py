#break 的範例
# n=0
# while n<5:
#     if n==3:
#         break
#     print(n) #印出迴圈中的n
#     n+=1
# print("最後的數字:",n)

# continue 的範例
# n=0
# for x in [0,1,2,3]:
#     if x%2==0:        %是取餘數
#         continue    #x是偶數，繼續下一個數字，像x==0,符合判斷式那就繼續下一個數字，x==1不符合那就印出來
#     print(x)          按下ctrl加上斜線(/)就可以把全部都註解起來
#     n+=1
# print("最後的數字n:",n)       因為有0跟2符合，所以會跑出n==2，跑到1跟3程式就不會跑到n+=1

#else 的範例
# sum=0
# for y in range(11):
#     sum+=y
# else:
#     print(sum)#印出0+1+2+3....+10

#找出平方根
n=input("輸入一個正整數 ")#還是字串
n=int(n)#轉換成數字
for i in range(n):# ex:n==9,那就是0~8
    if i*i==n:
        print("整數平方根",i)
        break#不會執行else
else:
    print ("沒有整數平方根")




