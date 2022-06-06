dict = {5:'welcome',6:'to',7:'college',
'a':{1:'geeks',2:'for',3:'study'},
'b':{1:'name',2:'studyin'}}
print(dict)

del dict[6]
print('\nremove 6 from dict::',dict)

del dict['a'][2]
print('\nremove dict element::',dict)

Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
pop_ele = Dict.pop(1)
print('\nDictionary after deletion: ' + str(Dict))
print('Value associated to poped key is: ' + str(pop_ele))

dict1 = {5:'welcome',6:'to',7:'college',
'a':{1:'geeks',2:'for',3:'study'},
'b':{1:'name',2:'studyin'}}
dict1.clear()
print("clear dictionary::",dict1)