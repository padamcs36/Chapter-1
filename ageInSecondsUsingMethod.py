# def age_in_seconds():
#     print("This is Method-1")
#     age = input("Enter your age: ")
#     age_seconds = int(age) * 365 * 24 * 60 * 60
#     print("You  are lived {} seconds.".format(age_seconds))
#
# def age_in_year():
#     age_year = input("Enter your age: ")
#     age_in_seconds()
#     print("You are  {} years old.".format(age_year))
#
# age_in_year()

def age_in_second():
    print("This program will show your age in seconds.")
    age_y = input("Enter your age in year ")
    age_sec = int(age_y)*365*24*60*60
    print("You are  lived {} seconds.".format(age_sec))
age_in_second()