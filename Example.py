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
        
        print(self.Str)

result5 = InputOutputString()
result5.printString()


