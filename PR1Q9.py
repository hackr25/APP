with open('f3.txt','r')as f3:
    sum=0
    for i in f3:
        a=int(i.strip())
        sum=sum+a
print('Summation= ',sum)
