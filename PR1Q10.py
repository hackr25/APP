#find smallest integer from file
with open("f3.txt","r") as f3:
    list1=[]
    for i in f3:
        a=i.split()
        for p in a:
            if p.startswith('1') or p.startswith('2') or p.startswith('3'):
                list1.append(int(p))
            else:
                continue
print("smallest integer is :",min(list1))
