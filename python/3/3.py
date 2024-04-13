import time
import json

# Функция для сохранения данных в файл
def save_data(filename, data):
    with open(filename, 'w') as file:
        if isinstance(data, dict):
            json.dump(data, file)
        elif isinstance(data, list):
            json.dump(data, file)

# Функция для загрузки данных из файла
def load_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Сохранение данных в файлы
list_data = [1, 2, 3, 4, 5]
dict_data = {'name': 'Valery', 'surname': 'Frolov'}

save_data('list_data.json', list_data)
save_data('dict_data.json', dict_data)

# Функция для проведения теста и сравнения времени выполнения операций над списком и словарем
def compare_operations(list_data, dict_data):
    # Измерение времени для операций с list
    list_start_time = time.time()
    list_operations(list_data)
    list_end_time = time.time()
    list_time = list_end_time - list_start_time

    # Измерение времени для операций с dict
    dict_start_time = time.time()
    dict_operations(dict_data)
    dict_end_time = time.time()
    dict_time = dict_end_time - dict_start_time

    # Вывод результатов
    print("\nВремя выполнения операций с list:", list_time)
    print("Время выполнения операций с dict:", dict_time)
    if list_time < dict_time:
        print("Список быстрее словаря")
    elif list_time > dict_time:
        print("Словарь быстрее списка")
    else:
        print("Время выполнения операций с list и dict одинаково")

# Операции с list
def list_operations(data):

    data.append(6)
    print("После добавления элемента в конец:", data)
    data.remove(5)
    print("После удаления элемента по значению 5:", data)

    data2 = [7, 8, 9]
    merged_data = data + data2
    print("Объединение двух списков:", merged_data)

    diff_data = list(set(data) - set(data2))
    print("Разница между списками:", diff_data)
    data.sort()
    print("Сортировка списка:", data)

# Операции с dict
def dict_operations(data):
    data['age'] = 21
    print("\nПосле добавления пары ключ-значение:", data)
    del data['age']
    print("После удаления пары ключ-значение:", data)
    data2 = {'city': 'Cherepovets', 'country': 'Russia'}
    merged_data = {**data, **data2}
    print("Объединение двух словарей:", merged_data)
    diff_keys = data.keys() - data2.keys()
    diff_dict = {k: data[k] for k in diff_keys}
    print("Разница между ключами в двух словарях:", diff_dict)

    # Сортировка словаря по ключам
    sorted_keys = sorted(data.keys())
    # Создание отсортированного словаря
    sorted_dict = {key: data[key] for key in sorted_keys}
    print("Отсортированный словарь:", sorted_dict)

# Вызов функции для проведения теста и сравнения времени выполнения операций
compare_operations(list_data, dict_data)