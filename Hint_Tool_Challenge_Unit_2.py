#Asking user to enter password
password = input("Enter your password: ")

#Removing any whitespaces at the start or end of the password
clean_password = password.strip()

#Getting the first and last letter of password
first_letter = clean_password[0]
last_letter = clean_password[-1]

#Display password hint
print(f"------PASSWORD HINT--------- ")
print(f"Your Password Hint: ")
print(f"It starts with {first_letter.upper()} and ends with {last_letter.upper()}.")