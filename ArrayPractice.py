from array import *
vals = array('i',[3,4,-1,9,2]) # i shows integer data types.
print(vals.buffer_info()) #two arguments in output first address of the array and second size.
print(vals.typecode)
print(vals[0])
value = array('i',[4,3,-1,9,-4])
print("Array-2 with for loop: ")
sum = 0
for i in range(len(value)):
    sum += value[i]
print("Sum is: ",sum)


print("**************** Simple Marksheet ******************")
marks = array('I',[])
subject = array('i',[])
n = int(input("Enter the length of the Loop :"))
for i in range(n):
    input("Enter name of the Subject: ")

for val in range(n):
    mark = int(input("Enter marks: "))
    marks.append(mark)
for i in range(n):
    print(marks[i])
