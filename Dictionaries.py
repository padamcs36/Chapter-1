# Dictionaries are key value pairs, first parameter is called key and second is called value
# key can be a string as well as number it doen't matter but it just be an unique
Monthconversion = {
    1:"January",
    "feb":"February",
    "mar":"March",
    "apr":"April",
    "may":"May",
    "jun":"June",
    "jul":"July",
    8:"August",
    "sep":"September",
    "oct":"october",
    "nov":"November",
    "dec":"December"
}
print(Monthconversion["may"]) # in parameter we are passing the key of the value
print(Monthconversion.get("dec"))
# If we put invalid key then we display default value in get method as second parameter.
a  = int(input("enter the key :"))
print(Monthconversion.get(a, "Invalid Key"))