with open('f2.txt','r') as f2:
    c=f2.readline()
    for p in reversed(c):
        print(p.strip())
        
