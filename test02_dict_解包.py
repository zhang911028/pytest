dit = {"diannao": "huipu", "shujuku": "mysql", "notes": "notepad++"}

'''print(type(dit))

for k in dit:
    print(k)
    print(dit[k])'''

for k in dit.keys():
    pass

for v in dit.values():
    pass

for k, v in dit.items():
    print(k, v)


s = [i for i in dit.items()]
print(s)
