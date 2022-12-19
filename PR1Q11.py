def sk_head(f4):
    data=f3.readline().strip()
    return(data)
def sk_com(f5):
    for i in f3:
        if i.startswith("#"):
            continue
        else:
            print(i.strip())
with open("f3.txt",'r')as f3:
    sk_head(f3)
    sk_com(f3)
