def select_mode():
    while True:
        try:
            mode = int(input("Выберите нужный режим: "))
            if 1 <= mode <= 7:
                return mode
            else:
                print('Нет такой функции')
        except ValueError:
            print("Ошибка: неправильный тип данных")


def get_input(prompt, input_type=int):
    if input_type in (int, float):
        while True:
            user_input = input(prompt)
            if user_input.lower() == 'выйти':
                return 'EXIT'
            try:
                if input_type == int:
                    value = int(user_input)
                else:
                    value = float(user_input)

                if value > 0:
                    return value
                else:
                    print('Значение не может быть отрицательным или нулевым')
            except ValueError:
                print('Введите корректное число')

    elif input_type == str:
        while True:
            try:
                user_input = input(prompt).strip()
                if user_input.lower() == 'выйти':
                    return 'EXIT'
                if user_input == '':
                    print('Обязательно для заполнения')
                    continue
                elif not user_input.isalpha():
                    print('Должны присутствовать только буквы')
                    continue
                else:
                    return user_input
            except Exception:
                print('Ошибка ввода')
                continue


def get_price_range():
    while True:
        try:
            max_price = int(input("Введите верхнюю границу стоимости: "))
            min_price = int(input("Введите нижнюю границу стоимости: "))

            if max_price < min_price:
                print("Ошибка: верхняя граница должна быть больше или равна нижней!")
                print(f"Вы ввели: верхняя={max_price}, нижняя={min_price}")
                continue

            if max_price < 0 or min_price < 0:
                print("Ошибка: стоимость не может быть отрицательной!")
                continue

            return max_price, min_price
        except ValueError:
            print("Ошибка: неправильный тип данных")
