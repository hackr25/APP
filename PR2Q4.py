#to implement compile function
string1='a=5\nb=6\nsum=a+b\nprint("sum=",sum)'
object1=compile(string1,'sumstring','exec')
exec(object1)
