
print("Printing Those number not divisible by 3 and 5: ")

for i in range(1,100):
    #if(i%3 != 0 and i%5 != 0):
    if i%3 == 0 or i%5 == 0:
        continue #continue statement skip those number which are divisible by 3 and 5
    print(i)