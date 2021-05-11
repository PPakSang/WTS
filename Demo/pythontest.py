import json

json_string ='''{
    "pass": 1,
    "number": 2
}'''

json_dic = {
    "pass" : 2,
    "number" : 1,
}


json_object = json.loads(json_string) # to python dic
json_object2 = json.dumps(json_dic,indent=2) # to json str
with open('test.json','w') as f: # to python dic
    
    json_dump = json.dump(json_object,f,indent=2)
print(type(json_object))
print(json_object2)
