#1:Capitalize
#Ham nay co tac dung in hoa chu cai dau 
str = "son pham"
print(str.capitalize())
#2:Center
#ham nay tra ve chuoi hien thi o giua chuoi
str = "phamngocson"
print(str.center(5))
#3:Count
#Ham ngay dung de tra ve so luong tu trong chuoi,
#Co 3 tham so count(string,start,end)
#sting la chuoi can tim kiem
#start la vi tri bat dau
#end la vi tri ket thuc

str = "huynh tra my la mot co gai xinh dep, my cung dam dang"
print(str.count("my"))
#4:encode
#Ham nay dung de ma hoa mot chuoi
str = "huynhtramy"
print(str.encode())
#5:decode
#Ham nay dung de giai ma mot chuoi

#6:endswith
#Kiem tra xem co phai ki tu ket thuc bang chuoi do ko 
str = "phamngocson"
print(str.endswith("n"))
#it will return true
print(str.endswith("son"))
#it will return true
print(str.endswith("pham"))
#it will return false

#7:expandtabs

#8:find
#Ham nay tra ve vi tri dau tien cua chuoi trong chuoi, neu khong thay se tra ve -1
str = "pham ngoc son"
print(str.find("son"))
#10:isalnum
#Ham nay tra ve true khi chuoi nhap vao chi gom chu va so
#Nguoc lai se tra ve false 
#Note: Pham Ngoc Son => false

str="phamngocson"
print(str.isalnum())
#it will return true

#11:isalpha
# Ham nay tra ve true khi chuoi can kiem tra chi chua chu cai 
str = "phamngocson"
print(str.isalpha())
#it will return true
str = "phamngocson1602"
#it will return false

#12: isdigit 
# Ham nay tra ve true khi chuoi deu la so
# Tra ve false khi nguoc lai
str = "123123123"
print(str.isdigit())
#It will return true
#13: islower
#Ham nay tra ve true khi cac chu trong chuoi deu la chu thuong 
str = "phamngocson"
print(str.islower())
#it will return true

#14:isupper
#Ham nay tra ve true khi chu trong chuoi deu la chu hoa
str = "HUYNHTRAMY"
print(str.isupper())
#It will reture true