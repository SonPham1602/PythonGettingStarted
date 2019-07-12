# Bài1
# Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5,
#  nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). Các số thu được sẽ được in 
#  thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.
result2 = 1
for i in range(1,9):
    result2 = result2*i

print(result2)

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


