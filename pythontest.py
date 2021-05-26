import string
import bcrypt
import jwt
from django.conf import settings

from random import choice

# arr=[choice(string.ascii_letters) for _ in range(8)]
# data = ''.join(arr) #list 또는 tuple 사이에 들어가는거
# print(arr)
# print(data)



test1 = 'abc'
a= bcrypt.hashpw(test1.encode('utf-8'),bcrypt.gensalt())
print(a,bcrypt.gensalt())
test2 = 'abc'
print(bcrypt.checkpw(test2.encode('utf-8'),a))


token = jwt.encode({'name':1},'django-insecure-goh7v4ed=5i!)gn2ffx7wk_m@zir5a0nmtue1^3*3qvopb7or0','HS256')
print(token)
