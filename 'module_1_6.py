my_dict={'Alexander': 1990, 'Anna':2002,'Victor':2020}
print(my_dict)
print(my_dict['Victor'])
print(my_dict.get('Anna'),': None')
my_dict.update({'Anna':2002,
               'Victor':2020})
Year_birth=my_dict.pop('Victor')
print(Year_birth)
print(my_dict)
my_set={1,1,2,"Яблоко",23,34,24}
print(my_set)
my_set.discard(24)
my_set.add(72)
my_set.add(64)
print(my_set)