def even(a):
    if(a%2==0):
        print(a)
with open("f3.txt",'r') as f3:
    print("Even numbers are ")
    for i in f3:
        even(int(i.strip()))
        
