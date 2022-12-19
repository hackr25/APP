#to read 10 characters and thrn then rest of the file
with open('f1.txt','r')as file:
    first_ten_char=file.read(10)
    the_rest=file.read()
print('the first 10 characters are:',first_ten_char)
print('remaning characters are:',the_rest)
