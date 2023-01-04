from datetime import date
from datetime import timedelta
today=date.today
offset=(today.isoweekday())%7
print("offset=",offset)
last_sat=today-timedelta(days=offset)
print("last saturday was on",last_sat)
