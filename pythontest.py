import string

from random import choice

arr=[choice(string.ascii_letters) for _ in range(8)]
data = ''.join(arr) #list 또는 tuple 사이에 들어가는거
print(arr)
print(data)