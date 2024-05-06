def test_1(txt, *types, names_authos="ED", **values):
    print("Тип: ", type(values))
    print("Аргумент:", values)
    print(txt)
    print(types)
    print(names_authos)
    for key, value in values.items():
        print(key, value)

test_1("Параметры всех типов",  1, 3, 4, names_authos = "Eduard", work = "params" )

# Рекурсия: "Факториал 7!"
def my_factorial(number):

    if number == 1:
        return number
    else:
        return number * my_factorial(number - 1)

print(my_factorial(7))

print(my_factorial(int(input("Введите число: "))))
