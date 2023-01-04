#7b sort
from datetime import datetime
list_date=['03/aug/22','29/apr/22','02/may/22','12/dec/22','21/sep/22']
list_date.sort(key=lambda date:datetime.strptime(date,"%d/%b/%y"))
print(list_date)
