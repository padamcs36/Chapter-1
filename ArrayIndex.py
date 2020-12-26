from array import *

arr = array('i',[])

a = int(input("enter the length of the array: "))

for i in range(a):
    x = int(input("Enter number of values :"))
    arr.append(x)

print(arr)

val = int(input("Enter the number to search: "))
count = 0
for e in arr:
    if e == val:
        print("The index of the array is: ",count)
        break
    count += 1
else:
    print("Invalid Search! Please enter valid number.")

p = int(input("Enter the  index of the array to find the value :"))
print(arr[p])