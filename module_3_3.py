# функция с параметрами по умолчанию

def print_params(*args, **kwargs):
    a = kwargs.get('a', 1)
    b = kwargs.get('b', 'word')
    c = kwargs.get('c', True)

    if len(args) > 0:
        a = args[0]
    if len(args) > 1:
        b = args[1]
    if len(args) > 2:
        c = args[2]

    print(f'a: {a}')
    print(f'b: {b}')
    print(f'c: {c}')

print("Вызов без аргументов:")
print_params()

print("\nВызов с одним аргументом (a = 10):")
print_params(10)

print("\nВызов с двумя аргументами (a = 5, b = 'Hello'):")
print_params(5, 'Hello')

print("\nВызов с тремя аргументами (a = 3, b = 5, c = [1, 2, 3]):")
print_params(3, 5, [1, 2, 3])

print("\nВызов с именованным аргументом b = 25:")
print_params(b = 25)

print("\nВызов с именнованным аргументом c = [1, 2, 3]:")
print_params(c= [1, 2, 3])



# распаковка параметров

values_list = [7, 'poker', '3,14']    # создание списка с тремя элементами трех типов

values_dic = {'a': 7, 'b': 'poker', 'c': '3,14'}    #создание словаря с тремя ключами и значениями разных типов

def print_params(a, b, c):   # определение функции
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
print_params(*values_list)    # распаковка списка
print_params(**values_dic)    # распаковка словаря

# распаковка + отдельные параметры

values_list2 = [3.14, 'Hello, Kitty']

def print_params(c, d, e):
    print(c, d, e)


print_params(*values_list2, 14)
