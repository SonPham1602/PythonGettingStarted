# Bài1
# Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5,
#  nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). Các số thu được sẽ được in 
#  thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.
result2 = 1
for i in range(1,9):
    result2 = result2*i

print(result2)
# Bai2
# Viết một chương trình có thể tính giai thừa của một số cho trước. 
# Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. 
# Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

# Cách 1:
result2 = 1
for i in range(1,9):
    result2 = result2*i

print ("Ket qua bai 2:",result2)

#Cách 2:
result2 = 1
x = int(input("Nhập số cần tính giai thừa: "))
for i in range(1,x+1):
    result2=result2*i
print("Giai thừa của",x,"là",result2)
array = [1,435,34,2,6,78,354,7658,345,4,5,657,568,4568,345]
print("Before order: ",array)

array.sort()
print("After ascending order :",array)
array.sort(reverse=True)
print("After descending order :",array)
#Bai 3 
#Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary chứa (i, i*i) 
# như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này. 
# Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.
n = int(input("Nhap vao mot so:"))
d=dict()
for i in range(1,n+1):
    d[i] = i*i
 
print(d)
#Bai 4
#Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển,
# tạo ra một danh sách và một tuple chứa mọi số.
# Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
result4=input("Nhap vao gia tri :")
l=result4.split(",")
t=tuple(l)
print(l)
print(t)
#Bai 5
#Định nghĩa một class có ít nhất 2 method: 
#getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.
#printString: in chuỗi vừa nhập sang chữ hoa. 
#Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.
#Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: QUANTRIMANG.COM

class InputOutputString(object):
    def __init__(self, *args, **kwargs):
        self.Str=""
        return super().__init__(*args, **kwargs)
    def getString(self):
        self.Str = input("Nhap chuoi:")
    
    def printString(self):
        if not self.Str:
            print("Chuoi rong")
        else:
            print(self.Str)

result5 = InputOutputString()
result5.printString()
# Bai 6
# Tinh hang tinh binh phuong cua mot so

#Note: Trong python co ham tinh binh phuong nhanh **


def Square2(num):
    return num ** 2

def Square(num):
    return num*num

x = input("Nhap so muon tinh binh phuong:")
while(not x.isdigit()):
  x = input("Chuoi nhap vao ko duoc la so.Vui long nhap lai:")

result6=int(x)
print("Ket qua binh phuong cua",result6,"la",Square(result6))
# Bai 7
# Python có nhiều hàm được tích hợp sẵn, nếu không biết cách sử dụng nó, bạn có thể đọc tài liệu trực tuyến hoặc tìm vài cuốn sách.
# Nhưng Python cũng có sẵn tài liệu về hàm cho mọi hàm tích hợp trong Python. 
# Yêu cầu của bài tập này là viết một chương trình để in tài liệu về 
# một số hàm Python được tích hợp sẵn như abs(), int(), input() và thêm tài liệu cho hàm bạn tự định nghĩa.

print(int.__doc__)
print(abs.__doc__)
print(input.__doc__)

#Note: Cac de them doc vao ham . Bang cach them dau ... (Noi dung cua Document) ...

#Bai8
#Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance


#Bai tap python level 2

#Bai 1
#Viết chương trình và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H]) 
# (bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H]
# .Với giá trị cố định của C là 50, H là 30. D là dãy giá trị tùy biến, được nhập vào từ giao diện người dùng,
# các giá trị của D được phân cách bằng dấu phẩy.
#Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 100,150,180 thì đầu ra sẽ là 18,22,24.

#Bai 16
#Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó. 
# Giả sử đầu vào sau được cấp cho chương trình: hello world! 123
#Thì đầu ra sẽ là: 
#Số chữ cái là: 10
#Số chữ số là: 3
numberOfChar = 0
numberOfNumber = 0
x = input("Nhap vao mot chuoi:")
for s in x :
  if s.isdigit():
    numberOfNumber+=1
  else:
    numberOfChar+=1

print("So luong ki tu:",numberOfChar)
print("So luong chu so:",numberOfNumber)


#Bai 17
#Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường.
#Giả sử đầu vào là: Quản Trị Mạng
#Thì đầu ra là:
#Chữ hoa: 3
#Chữ thường: 8

numberOfUpper = 0
numberOfLower = 0
x = input("Nhap vao mot chuoi:")


for s in x:
  if s.isupper():
    numberOfUpper+=1
  elif s.islower():
    numberOfLower+=1
  else:
    pass

print("Chu hoa:",numberOfUpper)
print("Chu thuong:",numberOfLower)


