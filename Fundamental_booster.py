print("Welcome to the Interactive Personal Data Collector!")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_number = int(input("Please enter your favourite number: "))

print("Thank you! Here is the information we collected:")

print(f"Name: {type(name)}, Memory Address: {id(name)}")
print(f"Age: {type(age)}, Memory Address: {id(age)}")
print(f"Height: {type(height)}, Memory Address: {id(height)}")
print(f"Fav_number: {type(fav_number)}, Memory Address: {id(fav_number)}")

current_year = 2026
birth_year = current_year - age

print(f"Your birth year is approximately: {birth_year} (based on your age of {age})")

print("Thank you for using the Personal Data collector. Goodbye!")
