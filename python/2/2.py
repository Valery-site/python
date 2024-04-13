import turtle


def draw_circle(radius):
    """Функция для рисования круга с заданным радиусом."""
    turtle.circle(radius)


def draw_square(side_length):
    """Функция для рисования квадрата с заданной длиной стороны."""
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)


def draw_rectangle(width, height):
    """Функция для рисования прямоугольника с заданными шириной и высотой."""
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)


def get_positive_number(prompt):
    """Функция для запроса у пользователя положительного числа."""
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            else:
                print("Введите положительное число!")
        except ValueError:
            print("Введите корректное число!")


def main():
    """Основная функция программы."""
    turtle.speed(1)  # Установить скорость черепахи

    # Запрос выбора пользователем фигуры
    shape = input("Введите фигуру (круг, квадрат, прямоугольник): ").lower()

    # Рисование фигуры в зависимости от выбора пользователя
    if shape == 'круг':
        radius = get_positive_number("Введите радиус круга: ")
        draw_circle(radius)
    elif shape == 'квадрат':
        side_length = get_positive_number("Введите длину стороны квадрата: ")
        draw_square(side_length)
    elif shape == 'прямоугольник':
        width = get_positive_number("Введите ширину прямоугольника: ")
        height = get_positive_number("Введите высоту прямоугольника: ")
        draw_rectangle(width, height)
    else:
        print("Введена неверная фигура!")

    turtle.done()


if __name__ == "__main__":
    main()