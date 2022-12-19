import os
f1="C:\\Users\Win10\Desktop\f6.txt"
if(not os.path.isfile('f1')):
    print("Error!! File Not Found")
else:
    print("File Found")
