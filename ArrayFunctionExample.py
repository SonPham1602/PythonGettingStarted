# We are able to create a array of int
# This is empty array
array = []
# Add a new data in array
array.append(1)
array.append(2)
array.append(3)
array.append(4)
array.append(5)
# Length of array
print("Length of array is", len(array))
print(array)
# delete one item in array
array.pop()
array.remove(1)
print(array)
# reverse array
array.reverse()
print("Array after reverse:", array)
# Create another array
array2 = [9, 8, 7, 6, 5]
print("Array2 :",array2)
array3 = array + array2
print("Array3 is copy array :",array3)


