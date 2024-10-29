immutable_var = (1, 'two', 3.0, [1, 2, 3, 4], True)
print(immutable_var)

# immutable_var[0] = 2
# TypeError: 'tuple' object does not support item assignment
# Главное свойство кортежа - это невозможность изменить содержимое кортежа
# после его создания

mutable_list = [1, 'two', 3.0, [1, 2, 3, 4], False]
mutable_list[0] = 'one'
mutable_list[1] = 2
print(mutable_list)