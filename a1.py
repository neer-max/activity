info = {
    'id1': {'name': ['Neeraj'], 'roll':2,'subject':['Computer','Art'] },
    'id2': {'name': ['Rohit'], 'roll':5,'subject':['Computer','Art'] },
    'id3': {'name': ['Neeraj'], 'roll':2,'subject':['Computer','Art'] },
}

dict_res = {}

for key, value in info.items():
    if value not in dict_res.values():
        dict_res[key] = value

print(dict_res)