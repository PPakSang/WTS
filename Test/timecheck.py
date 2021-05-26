import datetime

for i in range(4):
    print(type(datetime.date.today() + datetime.timedelta(weeks=i)))


print((datetime.date.fromisoformat('2012-05-01')-datetime.date.today()).days<0)

print(datetime.date.today(),datetime.date.today().isoweekday())
print (datetime.date.today() - datetime.timedelta(days=datetime.date.today().isoweekday()-7))