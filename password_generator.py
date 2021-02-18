# password_generator.py

import random
import string

print('Welcome to PASSWORD GENERATOR!')

# input the length of password
length = int(input('Enter the length of the password you would like to create: '))                      

# define data
num = string.digits
symbols = string.punctuation
lower = string.ascii_lowercase
upper = string.ascii_uppercase

# sum the data
all = num + symbols + lower + upper

# use random 
temp = random.sample(all,length)

# create the password 
password = "".join(temp)

print('Your generated password contains lowercase and uppercase letters, numbers and symbols in a random arrangement:')
print(password)
