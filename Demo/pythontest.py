# import json

# json_string ='''{
#     "pass": 1,
#     "number": 2
# }'''

# json_dic = {
#     "pass" : 2,
#     "number" : 1,
# }


# json_object = json.loads(json_string) # to python dic
# json_object2 = json.dumps(json_dic,indent=2) # to json str
# with open('test.json') as f: # to python dic
#     json_object3 = json.load(f)
#     # json_dump = json.dump(json_object,f,indent=2) 'w' 모드로 바꿔야하고 덮어쓰기 되는효과
# print(type(json_object))
# print(json_object2)
# print(type(json_object3))

from datetime import datetime

print(datetime.now().strftime('%H') == '14')