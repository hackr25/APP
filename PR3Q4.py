#to print the values of diffrent attributes
import datetime
print("present datetime:",datetime.datetime.now())
print("datetime of today:",datetime.datetime.today())
print("present utc:",datetime.datetime.utcnow())
x=datetime.datetime.now()
for var in['year','month','day','hour','minute','second','microsecond']:
    print(var,'is',getattr(x,var))
