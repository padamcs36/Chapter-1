from math import *
print("            /|")
print("          /  |")
print("        /    |")
print("      /      |")
print("    /        |")
print("  /          |")
print("/            |")
print("-------------")

print("Basic Data types and Use of Variable")
char_name = "Padam  Rai Motiani"
char_age = 21;
print("Hi, This is "+ char_name +" From Umarkot ")
print("I am ",char_age, " year old.")
char_name = "Dileep"
char_age = 20;
print("I am "+char_name+" Kumar I'm",char_age)

father_name = "Naroo"
surname = "Gandheer"
print("My father name is "+father_name+" Our surname is "+surname)
dept = "Computer System Engnineering"

print(dept.upper())
print(dept.lower().islower());
print(dept)
print(dept.replace("Computer", "Software"))
print(len(char_name))
print(char_name.index("l"))
var_name = 36
print(sqrt(var_name))
print(pow(3,4))
print(max(4,-1))
print(max(-3,-1))
print(round(3.53))
print(ceil(2.11))
print(floor(3.999))


print("This Example is Taken  from NanoProgram test.")
truth = "beauty"
index = 0
letters = []
while index < len(truth):
    letters.append(truth[index])
    index += 2

letters = '-'.join(letters)
print(letters)