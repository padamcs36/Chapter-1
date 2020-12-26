from array import *

vals = array('i',[2,4,6,8,10])
#This is also a method to create a array when you are not sure the type of the array
#and you want to assign the value of previous array
newArr = array(vals.typecode, (a*a for a in vals))
for i in range(len(newArr)):
    print(newArr[i],end=" ") #end=" " print the values in one row
    #print(newArr[i]) #each value is printed on the new line
print("\n",vals.buffer_info()) #it gives the size and address of the array.