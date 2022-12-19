#find smallest integer from file
with open("f4.txt","r") as f3:
    list1=[]
    for i in f3:
        a=i.split()
        for p in a:
            if p.startswith('1') or p.startswith('2') or p.startswith('3'):
                list1.append(int(p))
            else:
                continue
even_list=[]
odd_list=[]
for i in list1:
    if(i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)
with open("odd.txt","w")as f5:
    str1=str(odd_list)
    f5.write(str1)
with open("even.txt","w")as f6:
    str2=str(even_list)
    f6.write(str2)
