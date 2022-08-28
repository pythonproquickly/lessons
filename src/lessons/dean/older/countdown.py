from dateutil import parser
from datetime import datetime

date1 = parser.parse('2019-08-01 10:30')
date2 = parser.parse('2019-08-20 11:30')

diff = date2 - date1

print(diff)
print(diff.days)

print(parser.parse(str(datetime.now())))
