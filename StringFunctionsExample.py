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

#16:isspace
#Ham nay tra ve true khi chuoi la mot khoan trang khong chua so hay chu
str = "       "
print(str.isspace())
#It will return true
str = "Pham Ngoc Son"
print(str.isspace())
#it will return false

#17:istitle
#ham nay tra ve true khi tat ca chu cai dau tien cua tu deu viet hoa

str = "Pham Ngoc Son"
print(str.istitle())
#it will return true

#18: join
#Ham nay dung de join chuoi 1 vao chuoi 2 
#VD: str1 = " " , str2 = "son" => "s o n"

str1 = " "
str2 = "ngocson"
print(str1.join(str2))
#Ket qua tra ve se la: n g o c s o n

#19: len()
#ham nay tra ve lo dai cua chuoi 
#Note: Ham nay trong thuoc class string. Nen muon su dung ham nay can phai goi nhu sau
#len(string)
str = "phamngocson"
print(len(str))
#Ket qua tra ve se la 11

#20: ljust 
#ham nay se lam day chuoi voi khi tu
#vd: str = "sonpham"
str = "sonpham"
print(str.ljust(12,"_"))

#21:rjust
#Ham nay nguoc lai voi ljust
#Thay ve them vao cuoi thi se them vao dau

#22:lower
#Ham la chuyen chu thuong thanh chu hoa
#vd: SON =>son

str = "PHAMNGOCSON"
print(str.lower())

#23:upper
#Ham nay nguoc lai voi ham lower
#vd: son => SON

str = "phamngocson"
print(str.upper())

#24:lstrip()
#Ham nay dung de xoa di cac ki tu char o dau mang
#Mac dinh la khoang cach 
#vd:"   Son"=>"Son"
str = "     SonPham"
print(str.lstrip())
#25:rstrip
#Ham nay giong voi ham lstrip nhung vi  tri xoa thi o cuoi chuoi
#vd:"Son      "=>"Son"

str = "Son        "
print(str.rstrip())

#26:strip
#Ham nay la to hop cua lstrip va rstrip 
#vd:"    Son     " => "Son"

str = "    Son Pham     "
print(str.strip())
#27: rfind
#Ham nay  tra ve vi tri cuoi cung trong chuoi
#vd "pham ngoc son , son dep trai"=> tra ve vi tri cua son thu 2
str = "pham ngoc son, son dep trai"
print(str.rfind("son"))

#28:rindex => right and index
#Ham nay dung de vi tri chuoi can tim trong chuoi luon
#Diem khac nhau giua find va index la: Index co tra ve exeption



#29:replace
#Ham thay the chuoi trong string 
#Co 2  cach truyen tham so
#1:replace(str1,str2) str1=>old string ,str2 => new strng
#2:replace(str1,str2,number) str1 => old string, str2 => new string , number => so luong tu thay the 

str = "pham ngoc son"
print(str.replace("son","SON")) 

#30:Max
#Ham nay dung de tra ve ki tu cuoi cung trong bang chu cai abc
#vd "Son"=>"s"
#Note:Ham nay khong thuc lop cua string nen khi muon su dung ham nay thi phai goi nhu sau max(str)
#Note2:Ham nay chi hoat dong khi chuoi ko co dau cach
str = "Son"
print(max(str))

#31: Min
#Ham nay nguoc lai voi Max tra ve chu cai dau tien trong bang chu cai 
#vd:"Son"=>"n"

str = "son"
print(max(str))

#32:title
#Ham nay se lam hoa chu cai dau tien cua cac chu trong chuoi 
#vd:"pham ngoc son"=>"Pham Ngoc Son"
str = "pham ngoc son"
print(str.title())

#33:swapecase
#Ham nay se bien chu thuong thanh hoa, hoa thanh thuong 
#vd: "Son Pham"=>"sON pHAM"
str = "Son Pham"
print(str.swapcase())



