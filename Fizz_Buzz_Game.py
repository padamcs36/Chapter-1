list = [3,5,7,9,11,12,15,20,21,30]

for i in list:
    if i%3 == 0 and i%5 != 0:
        print(i," fizz ")
    if i%5 == 0 and i%3 != 0:
        print(i," buzz")
    if i % 15 == 0:
        print(i," fizz buzz")
    if i%3 != 0 and i%5 != 0:
        print(i," fizz-buzz")