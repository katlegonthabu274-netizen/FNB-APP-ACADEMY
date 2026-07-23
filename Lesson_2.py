#TRACKING INDIVIDUALLETTERS(INDEXING)
name = "Python"
print(name[0]) #printing the 1st character of object variable using indexing
print(name[-1]) #printing the last character of the object variable using indexing
print(name[2]) #prints the 3rd character of the object variable using indexing

#MANIPULATING STRINGS USING METHODS/()
town = " Johannesburg "
print(town.upper())
print(town.strip())
print(town.title())
print(town.find("s")) 
print(town.replace('Johannesburg' , 'Joburg' ))

#CREATING PROFESSIONAL SYSTEM EMAIL GENERATOR

first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()

username = f"{first[0]}{last}"
print(f"Your email address is: {username.lower()}@university.co.za")

message = 'Bobby\'s World'
print(message)
print(len(message))
print(message[8:])#slicing:prints string from indexed character at position 8 until the last character
print(message[2:3])#from index 2 up to but not including 3
print(message.count('b')) #counts number of times 'b' occurs in a string
print(message.find('y')) #finds index position of 'y' in a string

