# while 迴圈程式:
# n=1
# while n<=10:    #從這裡開始
#     print(n)
#     n+=1        #到這裡結束都是while的程式碼 要記的縮排
# sum=0
# while n<=10:
#     sum+=n
#     n+=1
# print(sum)


# for迴圈:
# sum=0
# for x in [3,5,1]:
#     print(x)
# for x in range (1,11):
#     print(x)
#     sum+=x
# print(sum)
#
# def add(numbers,num):
#     sum1=0
#     for num in range (1,numbers):
#         print(num)
#         sum1 += num
#     print(sum1)
# add(10 , 2)

product = 1
for count in range(4):  # 0 1 2 3
    print(count)
    product = product * (count + 1)
    print(product)

product1 = 1
for count1 in range(1, 5):  # 1 2 3 4
    print(count1)
    product1 = product1 * count1
    print(product1)

for x in range(1, 10, 2): # 1是最小範圍 10是最大的範圍 跑出1 3 5 7 9
    print(x)

for x in range(7, 3, -2):# 7是最大範圍 , 3是最小範圍   不會跑出3  跑出7 5
    print(x)

for x in range(7, 2, -3):# 7是最大範圍 , 2是最小範圍   不會跑出2 3   跑出7 4
    print(x)

