#to format the dates and time
import datetime
format="%a %b %d %H:%M:%S %Y"
today=datetime.datetime.today()
print("datetime as per ISO:",today)
x=today.strftime(format)
print("datetime using strftime:",x)
y=datetime.datetime.strptime(x,format)
print("date time using strptime:",y.strftime(format))
