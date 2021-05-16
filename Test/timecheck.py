import datetime

for i in range(4):
    print(type(datetime.date.today() + datetime.timedelta(weeks=i)))


print((datetime.date.fromisoformat('2012-05-01')-datetime.date.today()).days<0)