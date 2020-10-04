# # Is your birthday in pi? 

# +
# Find if your birthday is in pi
piPath = r'C:\Users\Logan.mcnulty\Desktop\Coding Stuff\Python\PythonNotebooks\ehmatthes-pcc_2e-078318e\chapter_10\pi_million_digits.txt'

with open(piPath) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string+= line.rstrip()

birthday = input('Enter your birthday (mmddyy)')

if birthday in pi_string:
    print('your birthday appears in the first million digits of pi!')
    
# splitting strings evenly
    firstHalf = pi_string[0:len(pi_string)//2] 
    secondHalf = pi_string[len(pi_string)//2 if len(pi_string)%2 == 0
                                 else ((len(pi_string)//2)+1):]
    
else:
    print('your birthday does not appear in the first million digits of pi!')
