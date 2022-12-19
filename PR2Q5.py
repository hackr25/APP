#to implement different functions on matched objects
import re
pat='Python'
str1='python is a high-level language'
m1=re.search(pat,str1)
s=m1.start()
print(s)
e=m1.end()
print(e)
sp=m1.span()
print(sp)
sp1=m1.span()[0]
print(sp1)
sp2=m1.span()[1]
print('The pattern "%s" is found in "%s" from "%d" to "%d" ("%s")'%(m1.re.pattern,m1.string,s,e,str1[s:e]))
