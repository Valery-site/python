from abc import ABCMeta, abstractmethod

# Определение класса R для использования в композиции
class R:
    def __init__(self):
        print("r")

# Определение класса Re, использующего композицию с классом R
class Re:
    def __init__(self):
        self._rer = R()

# Определение базового класса Stick
class Stick:
    def __init__(self, owner, length):
        self._owner = owner  # Инкапсуляция: приватное поле _owner
        if length < 0:
            raise ValueError("Длина палки не может быть отрицательной")
        self._length = length

    # Переопределение метода для информативного вывода
    def __str__(self):
        return f"Owner: {self._owner}, Length: {self._length}"

    # Статический метод, не требующий доступа к экземпляру
    @staticmethod
    def who_are_you():
        print("stick")

    # Метод доступа к приватному полю _owner через декораторы
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner

# Определение класса Hand, наследующего от класса Stick
class Hand(Stick):
    def __init__(self, power, *args):
        super().__init__(*args)  # Вызов конструктора родительского класса
        self._power = power

    # Переопределение метода для информативного вывода
    def __str__(self):
        return super().__str__() + f", Power: {self._power}"

    # Полиморфный метод
    @staticmethod
    def who_are_you():
        print("hand")

    # Перегрузка оператора +
    def __add__(self, other):
        return self._power + other._power

# Определение абстрактного класса Class1 с абстрактным методом test
class Class1(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def test(x):
        pass

# Определение класса Class2, наследующего от Class1, с виртуальным методом test
class Class2(Class1):
    @staticmethod
    def test(x):
        print(x)

# Определение пользовательского исключения
class CustomException(Exception):
    def __init__(self, message="Пользовательское исключение"):
        self.message = message
        super().__init__(self.message)

# Основная программа
if __name__ == "__main__":
    try:
        # Создание и использование объектов класса Stick
        st = Stick("Maiki", 100)
        st.owner = "Maiki Maikovich"
        print(st.owner)
        print(st)
        Stick.who_are_you()

        print()

        # Попытка создать палку с отрицательной длиной
        stick_with_negative_length = Stick("Negative Stick", -10)
    except ValueError as ve:
        print(f"Произошла ошибка: {ve}")
    finally:
        print("Конец программы")

    # Использование assert
    x = 10
    assert x > 0, "x должен быть положительным числом"

    # Генерация пользовательского исключения
    try:
        raise CustomException("Сработало пользовательское исключение")
    except CustomException as ce:
        print(ce)