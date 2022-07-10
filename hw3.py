#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def numbers(x):
    rng = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {rng[i]}: "))
    return a


def check(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


stmt = numbers(3)

if check(stmt) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")