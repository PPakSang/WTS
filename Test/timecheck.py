import datetime

for i in range(4):
    print(type(datetime.date.today() + datetime.timedelta(weeks=i)))