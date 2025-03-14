# Домашнее задание по теме "Генераторные сборки"

# Задача:
# Дано 2 списка:
# first = ['Strings', 'Student', 'Computers']
# second = ['Строка', 'Урбан', 'Компьютер']
# Необходимо создать 2 генераторных сборки:
# 1 В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков
#   first и second, если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.
# 2 В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк
#   в одинаковых позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip.
#   Используйте функции range и len.

# __________________________Р_Е_Ш_Е_Н_И_Е:_______________________________________________ #
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(s1) - len(s2) for s1, s2 in zip(first, second) if not len(s1) == len(s2))
print(list(first_result))
second_result = (len(first[i]) == len(second[i]) for i in range(0, len(first)))
print(list(second_result))