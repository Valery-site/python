import math

def main():
    # Значения переменных
    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    c = float(input("Введите значение c: "))
    d = float(input("Введите значение d: "))

    # Значение экспоненты
    e = 2.71828182845904

    # Подвыражения первого выражения
    sub_expr1 = a - b
    sub_expr2 = 2 and c
    sub_expr3 = math.log(c, d)
    sub_expr4 = sub_expr1 / sub_expr2
    result1 = sub_expr4 * sub_expr3

    # Подвыражения второго выражения
    sub_expr5 = a or b
    sub_expr6 = c * d
    sub_expr7 = math.sin(d)
    sub_expr8 = sub_expr5 / sub_expr6
    result2 = sub_expr8 - 5 + e - sub_expr7

    # Печать результатов
    print("Результат первого выражения:", result1)
    print("Результат второго выражения:", result2)

if __name__ == "__main__":
    main()