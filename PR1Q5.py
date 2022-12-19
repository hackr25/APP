with open('f2.txt','r') as f2:
    c=f2.readlines()
    for p in sorted(c):
        print(p.strip())
        
    
