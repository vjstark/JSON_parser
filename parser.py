import json

def load_json(path):
    with open(path,'r') as jfile:
        data = jfile.read()
    jdata = json.loads(data)

    return jdata


path1 = "/Users/vjstark/Downloads/RA_temp/demo.json"
path = "/Users/vjstark/Downloads/RA_temp/abcd.json"
jdata = load_json(path)
id = "35LwpAyBbFBx9X9aJuCCml"
href = "#"+id

def jsonParser(superParent, parentKey, jsonData):

    for key, value in jsonData.items():
        if type(value) is dict:
            jsonParser(parentKey, key, value)
        elif type(value) is str and (value == id or value==href):
            print(superParent, parentKey, jsonData)
        elif type(value) is list:
            for dct in value:
                jsonParser(parentKey,'',dct)

jsonParser('','',jdata)


# def recursive_items(dictionary):
#     for key, value in dictionary.items():
#         if isinstance(value, dict):
#             if id in value.values():
#                 print(value)
#             else:
#                 recursive_items(value)
#         elif isinstance(value, list):
#             for dct in value:
#                 if id in dct.values():
#                     print(dct)
#                 elif isinstance(value, dict):
#                     recursive_items(value)


# else:
#     if key == id:
#         print(key, value)
#         #yield (key, value)


# recursive_items(jdata)
# for key, value in recursive_items(jdata):
#     print(key, value)

# def rec(jdata):
#     stack = list(jdata.items())
#     visited = set()
#     while stack:
#         k, v = stack.pop()
#         if k == id:
#             print(k)
#         else:
#             if k not in visited:
#                 if isinstance(v, dict):
#                     stack.extend(v.items())
#                 else:
#                     if isinstance(v, list):
#                         for dct in v:
#                             if id in dct.values():
#                                 print('yay')
#                                 print(dct)
#             else:
#                 #print('oo')
#                 print(f'{k,v}')
#             visited.add(k)
#
# rec(jdata)

# def item_generator(json_input, lookup_key):
#     if isinstance(json_input, dict):
#         for k, v in json_input.items():
#             if k == lookup_key:
#                 yield v
#             else:
#                 yield from item_generator(v, lookup_key)
#     elif isinstance(json_input, list):
#         for item in json_input:
#             yield from item_generator(item, lookup_key)

# op = item_generator(jdata, id)
# for i in op:
#     print(i)
