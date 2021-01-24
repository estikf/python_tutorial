"""
tuple1 = ()
tuple2 = tuple()
print(type(tuple1))
print(type(tuple2))
set1 = set()
print(type(set1))
list1 = []
list2 = list()
print(type(list1))
print(type(list2))
dict1 = {}
dict2 = dict()
print(type(dict1))
print(type(dict2))
"""
"""
dict1 = {'a' : 1 , 'b' : 2 , 'c' : 4 , 'd' : 6 , 'f' : 10}
print(dict1['a'])
print(sum(dict1.values()) / len(dict1))
"""
"""
friends = {'mahmut' : 24 , 'ebru' : 90 }
friends['eren'] = 90
print(friends)
del friends['mahmut']
print(friends)
friends.update({'mahmut' : 123})
print(friends)
"""
"""
my_dict = {'odd_numbers': [1, 2 ,3]}
for v in my_dict.values():
    my_list = []
    for y in v:
        my_list.append(y**3)
my_dict['odd_numbers'] = my_list
print(my_dict)
"""
"""
dict1 = {'ahmet' : 21 , 'mehmet' : 42 , 'süleyman' : 56}
my_key_list = []
my_value_list = []
for k,v in dict1.items():
    my_key_list.append(k)
    my_value_list.append(v)
print(my_key_list)
print(my_value_list)
print(sum(my_value_list))
"""
dict1 = {x : 2*x+3 for x in range(1,11)}
print(dict1)
