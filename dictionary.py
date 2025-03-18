capital_cities = {
    "Kenya": "Nairobi",
    "Uganda": "Kampala",
    "Tanzania": "Dodoma",
    "Rwanda": "Kigali",  
}
print(capital_cities)
# The code above is a dictionary that contains the names of countries and their capital cities. 
print(capital_cities["Kenya"])

del capital_cities["Kenya"]
print("updated capital_cities:", capital_cities)

print(capital_cities["Tanzania"])

#looping through a dictionary
numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
}
for i in numbers:
    print(i, numbers[i])