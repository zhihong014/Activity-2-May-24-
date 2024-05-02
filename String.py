message = 'Hello'
print(message)

first_character = message[0]
print('First character of message is ', first_character)

length = len(message)
print('Length of message is ', length)

name = input('Enter your name:')
print('Your name is ', name)


greeting = "Hello, " + name + "!"
print(greeting)

# Use string methods
uppercase_message = greeting.upper()
print("Uppercase message:", uppercase_message)

# Check if a substring is in the string
contains_DuniA = "DuniA" in greeting
print("Does the message contain 'DuniA'? ", contains_DuniA)

# Replace part of the string
new_message = message.replace("DuniA", "World")
print("Updated message:", new_message)
