from datetime import date

d0 = date(2021, 8, 24)
d1 = date(2021, 7, 26)
delta = d1 - d0
print(delta.days)

from datetime import datetime
date_format = "%m/%d/%Y"
a = datetime.strptime('8/18/2008', date_format)
b = datetime.strptime('9/26/2008', date_format)
delta = b - a
print(delta.days) # that's it