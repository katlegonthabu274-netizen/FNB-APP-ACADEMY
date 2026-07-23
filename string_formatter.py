first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter short bio: ")
username = (f"{first_name[0].lower()}{last_name.lower()}")
full_name = (f"{first_name.title()} {last_name.title()}")
clean_bio = (bio.strip())
bio_length = (len(bio))
updated_bio = (clean_bio.replace("I am" , "I'm" ))

print(f"----------USER PROFILE------------")
print(f"Username: {username}")
print(f"Full Name: {full_name}")
print(f"Bio: {updated_bio}")
print(f"Bio Length: {bio_length}")


