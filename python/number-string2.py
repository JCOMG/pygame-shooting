#數字運算
#整數除法
x=7/6
print(x)
y=7//6 #取整數
print(y)
#次方運算
w=2**3
print(w) #這裡應該要print 8 不知道為什麼不行
z=2**0.5 #開根號運算
print(z)



#字串運算
s="Hello\nWorld"
print(s)

s="""HELLO
WORLD"""
print(s)

s="Hello"*3+"World"
print(s)

s="Hello"
print(s[0]) #取出第一個值

s="Hello"
print(s[1:4])#包含索引1不包含索引4，所以只會顯示出ell
s="Hello"
print(s[1:])#包含索引1包含後面的其他字母，所以會只顯示出ello
s="Hello"
print(s[:4])#包含索引0~3，不包含索引值4，所以只會顯示出Hell