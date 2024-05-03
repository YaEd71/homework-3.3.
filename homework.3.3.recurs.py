def test_1(txt, *types, names_authos="ED", **values):
    print("Тип: ", type(values))
    print("Аргумент:", values)
    print(txt)
    print(types)
    print(names_authos)
    for key, value in values.items():
        print(key, value)

test_1("Параметры всех типов",  1, 3, 4, names_authos = "Eduard", work = "params" )

def my_factorial(n, *args, txt = "Факториал"):
    a = 1
    for i in range(len(args)):
        a *= args[i]
    print(txt + ":", a)

my_factorial( 1,  1, 2, 3, 4, 5, 6, 7, txt = "Факториал 7!")

