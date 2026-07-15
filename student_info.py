# Collecting user's information using input() function
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: "))

# Displaying formatted greeting using f-string
full_name = input("Enter your full name: ")
print (f"Welcome, {full_name} ")

# Displaying UPPERCASE using .upper() method and Title Case using .title() method
print (full_name.upper())
print (full_name.title())

# Calculate and display the age in months (age X 12)
age_months = age * 12
print (f"Age in months: {age_months}")

# Calculate and displaying number to 2 decimal places using round() function
rounded_favourite_number = round(favourite_number, 2)
print (f"favourite number: {rounded_favourite_number}") 

# Printing the data type of each collected vale using type() function
print (type(full_name))
print (type(surname))
print (type(age))
print (type(favourite_number))

# Displaying user in formatted profile card
print ("---------------")
print (" STUDENT PROFILE ")
print ("---------------")
print (f"Full Name: {full_name}")
print (f"Age: {age}")
print (f"Age in Months: {age_months}")
print (f"Favourite Number: {rounded_favourite_number}") 
