my_dict={'Alexander': 1990, 'Anna':2002,'Victor':2020}
print(my_dict)
print(my_dict['Victor'])
print(my_dict.get('Елесей',': None'))
my_dict.update({'Герман':2001,
               'Анастасия':2015})
removed_year = my_dict.pop('Анастасия')
print(removed_year)
print(my_dict)

print()

my_set = {2, 3, 3, 2, 5, True, True, False, True, 'list', 'set', 'list', 'list'}
print('Множество:', my_set)
my_set.add('string')
my_set.add('float')
my_set.discard(2)
print('Изменённое множество:', my_set)