import unittest


def get_data(filename):
    try:
        with open(filename, 'r', encoding='utf8') as f:
            text = f.read()
    except FileNotFoundError:
        print("Такого файла не существует."
              "Работа завершена")
        exit()
    else:
        numbers = []
        text = text.strip().split()
        for line in text:
            try:
                number = int(line)
            except ValueError:
                print("В файле присутствуют элементы типа 'str'\n"
                      "Работа завершена")
                raise
            else:
                numbers.append(number)
        return numbers


def minimum(numbers):
    return sorted(numbers)[0]


def maximum(numbers):
    return sorted(numbers)[-1]


def summa(numbers):
    result = 0
    for elem in numbers:
        result += elem
    return result


def product(numbers):
    result = 1
    for elem in numbers:
        result = result * elem
    return result


def main():
    filename = input("Введите имя файла:")
    numbers = get_data(filename)
    #Задание 5 обработка ошибки переполнения
    try:
        print(f'Минимальное число:{minimum(numbers)}')
        print(f'Максимальное число:{maximum(numbers)}')
        print(f'Сумма чисел:{summa(numbers)}')
        print(f'Произведение чисел:{product(numbers)}')
    except OverflowError:
        print("Размер файла слишком большой")
        exit()


if __name__ == '__main__':
    main()
