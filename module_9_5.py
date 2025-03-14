# Домашнее задание по теме "Итераторы"

# Задача "Range - это просто":

# Создайте пользовательский класс исключения StepValueError, который наследуется от ValueError.
# Наследования достаточно, класс оставьте пустым при помощи оператора pass.
#
# Создайте класс Iterator, который обладает следующими свойствами:
# Атрибуты объекта:
# 1 start - целое число, с которого начинается итерация.
# 2 stop - целое число, на котором заканчивается итерация.
# 3 step - шаг, с которым совершается итерация.
# 4 pointer - указывает на текущее число в итерации (изначально start)
# Методы:
# 1 __init__(self, start, stop, step=1) - принимающий значения старта и конца итерации, а также шага.
#   В этом методе в первую очередь проверяется step на равенство 0.
#   Если равно, то выбрасывается исключение StepValueError('шаг не может быть равен 0')
# 2 __iter__ - метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора.
# 3 __next__ - метод, увеличивающий атрибут pointer на step. В зависимости от знака атрибута step итерация завершится
#   либо когда pointer станет больше stop, либо меньше stop. Учтите это при описании метода.
#
# Пункты задачи:
# 1 Создайте класс исключения StepValueError.
# 2 Создайте класс Iterator и опишите его атрибуты и методы.
# 3 Создайте несколько объектов класса Iterator и совершите итерации с ними при помощи цикла for.

# Примечания:
# Особое внимание уделите методу __next__ и условиям в нём.

# __________________________Р_Е_Ш_Е_Н_И_Е:_______________________________________________ #
class StepValueError(ValueError):
    pass
class Iterator():
    def __init__(self, start, stop, step = 1):
        self.start = start  # start - целое число, с которого начинается итерация.
        self.stop = stop    # stop - целое число, на котором заканчивается итерация.
        self.step = step    # step - шаг, с которым совершается итерация (по умолчанию =1).
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start   # pointer - указывает на текущее число в итерации (изначально start)
        return self # возвращаем ссылку на самого себя, т.к. наш объект должен быть итератором

    def __next__(self):
        self.pointer += self.step   # увеличиваем атрибут pointer на step
        if self.step < 0:
            if self.pointer < self.stop:
                raise  StopIteration()
        else:
            if self.pointer > self.stop:
                raise  StopIteration()
        return self.pointer

try:
    iter1 = Iterator(100, 200, 0)
    for k in iter1:
        print(k, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()