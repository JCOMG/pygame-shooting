#定義類別、與類別屬性  (封裝在類別中的變數和函式)
# class   IO:                                             #IO是我們用來想像可以INPUT、OUTPUT(讀取、寫入)
#     supportSrcs=["console","file"]                      #讓使用者可以從終端機跟檔案讀取資料，supportedSrcs是類別IO的一個屬性
#     def read(src):                                      #定義一個函式read,函式read也是類別IO的其中一個屬性,src是參數
#         print("Read from",src)
# #使用類別
# print(IO.supportSrcs)                                   #可以類別.屬性就可以使用類別
# IO.read("file")




# class   IO:                                            
#     supportSrcs=["console","file"]                      
#     def read(src):      
#         if src not in IO.supportSrcs:
#             print("not supported")
#         else:                                
#             print("Read from",src)
# print(IO.supportSrcs)                                   
# IO.read("file")
# IO.read("internet")         #不在supportSrcS裡，因為裡面只有["console","file"]，所以他會印出not supported 








#進階的題目，從13~22行裡改變的
class Jimmy:
    x=["Eunice love Jimmy","Eunice hates Jimmy"]
    def love(a):
        if a in Jimmy.x:
            print("GOOD")
        else:
            print("SRY")
Jimmy.love("hello")
print(Jimmy.x)