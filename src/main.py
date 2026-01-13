'''
Вариант 6
Создать файл записей, в котором хранится информация о квартирах, продаваемых
риэлтерским агентством: адрес (улица, дом, квартира), количество комнат, общая площадь,
жилая площадь, этаж, этажность дома, фамилия владельца, стоимость.
Разработать и реализовать программу "Риэлтерское агентство", которая считывает
исходную информацию и позволяет на основе неё создавать следующие отчёты:
    1 Полный список всех квартир, который будет отсортирован следующему ключу:
количество комнат (по убыванию) + стоимость (по возрастанию)
    2 Список всех квартир с заданным количеством комнат , отсортированный по
следующему ключу: этаж (по возрастанию), этажность дома (по возрастанию) +
стоимость (по убыванию).
    3 Список всех квартир стоимостью в диапазоне от N1 до N2 рублей, отсортированный
по следующему ключу: стоимость (по убыванию) + общая площадь (по
возрастанию).
Создать базу квартир, включающую не менее 25 записей и на основе неё сформировать все
указанные списки. База должна содержать такие записи, чтобы во всех списках явно
прослеживался заданный вид сортировки по всем ключам. Для сортировки записей
использовать сортировку Шелла.
'''
from sort import *
from check import *


def add_apartment(apartments):
    print("\n" + "=" * 40)
    print("Добавление квартиры")
    print("=" * 40)
    print("(Для отмены введите 'Выйти' в любом поле)\n")

    street = get_input('Улица: ', str)
    if street == "EXIT":
        return apartments

    house = get_input('Дом: ', int)
    if house == "EXIT":
        return apartments

    apartment_number = get_input('Квартира: ', int)
    if apartment_number == "EXIT":
        return apartments

    rooms = get_input('Кол-во комнат: ', int)
    if rooms == "EXIT":
        return apartments

    while True:
        total_area = get_input('Общая площадь: ', float)
        if total_area == "EXIT":
            return apartments

        living_area = get_input('Жилая площадь: ', float)
        if living_area == "EXIT":
            return apartments

        if living_area <= total_area:
            break
        print("Ошибка: Жилая площадь не может быть больше общей. Введите снова.\n")

    while True:
        total_floors = get_input('Этажность дома: ', int)
        if total_floors == "EXIT":
            return apartments

        floor = get_input('Этаж: ', int)
        if floor == "EXIT":
            return apartments

        if floor <= total_floors:
            break
        print("Ошибка: Этаж не может быть больше этажности дома. Введите снова.\n")

    owner = get_input('Фамилия владельца: ', str)
    if owner == "EXIT":
        return apartments

    price = get_input('Стоимость (руб): ', int)
    if price == "EXIT":
        return apartments

    apartment_record = f"{street} {house}-{apartment_number}, {rooms}, {total_area}, "
    apartment_record += f"{living_area}, {floor}, {total_floors}, {owner}, {price}\n"

    try:
        with open("flats.txt", "a", encoding="utf-8") as file:
            file.write(apartment_record)

        print("\n" + "=" * 40)
        print("Квартира успешно добавлена!")
        print(f"Запись: {apartment_record.strip()}")
        print("=" * 40)

        new_apartment = {
            "адрес": f"{street} {house}-{apartment_number}",
            "комнат": rooms,
            "общая_площадь": total_area,
            "жилая_площадь": living_area,
            "этаж": floor,
            "этажность": total_floors,
            "владелец": owner,
            "стоимость": price
        }
        apartments.append(new_apartment)

        save_apartments(apartments)
        return apartments

    except Exception as e:
        print(f"Ошибка при сохранении: {e}")
        return apartments


def edit_apartment(apartments):
    if not apartments:
        print("Список квартир пуст.")
        return apartments

    apartments = sort_by_price_and_area(apartments)

    print("\n" + "=" * 60)
    print("РЕДАКТИРОВАНИЕ КВАРТИРЫ")
    print("=" * 60)

    for i, apt in enumerate(apartments, 1):
        print(f"Номер: {i:2} | "
              f"Адрес: {apt['адрес']:20} | "
              f"Комнат: {apt['комнат']:2} | "
              f"Площадь: {apt['общая_площадь']:6.1f} м2 | "
              f"Жилая: {apt['жилая_площадь']:6.1f} м2 | "
              f"Этаж: {apt['этаж']:2}/{apt['этажность']} | "
              f"Владелец: {apt['владелец']:12} | "
              f"Стоимость: {apt['стоимость']:12,} руб")

    while True:
        try:
            prompt = f"\nВыберите номер квартиры для редактирования (1-{len(apartments)}): "
            choice = get_input(prompt, int)
            if choice == "EXIT":
                print("Редактирование отменено.")
                return apartments

            if 1 <= choice <= len(apartments):
                selected = apartments[choice - 1]
                print(f"\nВыбрана квартира: {selected['адрес']}")
                print("Какое поле вы хотите изменить?")
                print("1. Улица")
                print("2. Дом")
                print("3. Квартира")
                print("4. Количество комнат")
                print("5. Общая площадь")
                print("6. Жилая площадь")
                print("7. Этаж")
                print("8. Этажность дома")
                print("9. Фамилия владельца")
                print("10. Стоимость")
                print("11. Отмена")

                field_choice = get_input(
                    "Выберите поле для изменения (1-11): ", int)

                if field_choice == 11:
                    print("Редактирование отменено.")
                    return apartments

                parts = selected['адрес'].split()
                street = parts[0]
                house_apt = parts[1]
                house, apartment = house_apt.split('-')

                if field_choice == 1:
                    print(f"Текущая улица: {street}")
                    new_street = get_input("Новая улица: ", str)
                    if new_street == "EXIT":
                        print("Редактирование отменено.")
                        return apartments
                    selected['адрес'] = f"{new_street} {house}-{apartment}"

                elif field_choice == 2:
                    print(f"Текущий дом: {house}")
                    new_house = get_input("Новый дом: ", int)
                    if new_house == "EXIT":
                        print("Редактирование отменено.")
                        return apartments
                    selected['адрес'] = f"{street} {new_house}-{apartment}"

                elif field_choice == 3:
                    print(f"Текущая квартира: {apartment}")
                    new_apartment = get_input("Новая квартира: ", int)
                    if new_apartment == "EXIT":
                        print("Редактирование отменено.")
                        return apartments
                    selected['адрес'] = f"{street} {house}-{new_apartment}"

                elif field_choice == 4:
                    print(f"Текущее количество комнат: {selected['комнат']}")
                    new_value = get_input("Новое количество комнат: ", int)
                    if new_value == "EXIT":
                        print("Редактирование отменено.")
                        return apartments
                    selected['комнат'] = new_value

                elif field_choice == 5:
                    current_area = selected['общая_площадь']
                    print(f"Текущая общая площадь: {current_area}")
                    new_value = get_input("Новая общая площадь: ", float)
                    if new_value == "EXIT":
                        print("Редактирование отменено.")
                        return apartments
                    selected['общая_площадь'] = new_value

                    if selected['жилая_площадь'] > new_value:
                        print("Предупреждение: Жилая площадь теперь больше общей.")
                        print("Измените жилую площадь в соответствующем пункте.")

                elif field_choice == 6:
                    current_living = selected['жилая_площадь']
                    print(f"Текущая жилая площадь: {current_living}")
                    new_value = get_input("Новая жилая площадь: ", float)
                    if new_value == "EXIT":
                        print("Редактирование отменено.")
                        return apartments

                    if new_value > selected['общая_площадь']:
                        print("Ошибка: Жилая площадь не может быть больше общей.")
                        print(f"Общая площадь: {selected['общая_площадь']}")
                        continue

                    selected['жилая_площадь'] = new_value

                elif field_choice == 7:
                    print(f"Текущий этаж: {selected['этаж']}")
                    new_value = get_input("Новый этаж: ", int)
                    if new_value == "EXIT":
                        print("Редактирование отменено.")
                        return apartments

                    if new_value > selected['этажность']:
                        print("Ошибка: Этаж не может быть больше этажности дома.")
                        print(f"Этажность дома: {selected['этажность']}")
                        continue

                    selected['этаж'] = new_value

                elif field_choice == 8:
                    print(f"Текущая этажность дома: {selected['этажность']}")
                    new_value = get_input("Новая этажность дома: ", int)
                    if new_value == "EXIT":
                        print("Редактирование отменено.")
                        return apartments

                    if selected['этаж'] > new_value:
                        print("Ошибка: Этаж не может быть больше новой этажности.")
                        print(f"Текущий этаж: {selected['этаж']}")
                        continue

                    selected['этажность'] = new_value

                elif field_choice == 9:
                    print(f"Текущий владелец: {selected['владелец']}")
                    new_value = get_input("Новый владелец: ", str)
                    if new_value == "EXIT":
                        print("Редактирование отменено.")
                        return apartments
                    selected['владелец'] = new_value

                elif field_choice == 10:
                    print(f"Текущая стоимость: {selected['стоимость']:,}")
                    new_value = get_input("Новая стоимость: ", int)
                    if new_value == "EXIT":
                        print("Редактирование отменено.")
                        return apartments
                    selected['стоимость'] = new_value

                save_apartments(apartments)
                print("Изменения сохранены!")
                return apartments

            else:
                print(f"Введите число от 1 до {len(apartments)}")

        except ValueError:
            print("Введите целое число.")


def delete_apartments(apartments):
    if not apartments:
        print("Список квартир пуст.")
        return apartments

    apartments = sort_by_price_and_area(apartments)

    print("\n" + "=" * 60)
    print("УДАЛЕНИЕ КВАРТИРЫ")
    print("=" * 60)

    for i, apt in enumerate(apartments, 1):
        print(f"Номер: {i:2} | "
              f"Адрес: {apt['адрес']:20} | "
              f"Комнат: {apt['комнат']:2} | "
              f"Площадь: {apt['общая_площадь']:6.1f} м2 | "
              f"Этаж: {apt['этаж']:2}/{apt['этажность']} | "
              f"Владелец: {apt['владелец']:12} | "
              f"Стоимость: {apt['стоимость']:12,} руб")

    while True:
        try:
            prompt = f"\nВыберите номер записи для удаления (1-{len(apartments)}): "
            choice = int(input(prompt))

            if 1 <= choice <= len(apartments):
                while True:
                    selected = apartments[choice - 1]
                    confirm = input(f"Вы уверены, что хотите удалить запись?(да/нет)\n"
                                    f"Адрес: {selected['адрес']} | "
                                    f"Комнат: {selected['комнат']} | "
                                    f"Цена: {selected['стоимость']:,} руб.\n").lower()

                    if confirm in ['да', 'д', 'yes', 'y']:
                        apartments.pop(choice - 1)
                        save_apartments(apartments)
                        print("Запись успешно удалена из файла")
                        return apartments

                    elif confirm in ['нет', 'н', 'no', 'n']:
                        print("Удаление отменено")
                        return apartments

                    else:
                        print("Введите 'да' или 'нет'")

            else:
                print(f"Введите число от 1 до {len(apartments)}")

        except ValueError:
            print("Введите целое число")


def save_apartments(apartments):
    with open("flats.txt", "w", encoding="utf-8") as file:
        for apt in apartments:
            line = f"{apt['адрес']}, {apt['комнат']}, {apt['общая_площадь']}, "
            line += f"{apt['жилая_площадь']}, {apt['этаж']}, {apt['этажность']}, "
            line += f"{apt['владелец']}, {apt['стоимость']}\n"
            file.write(line)


def load_apartments():
    apartments = []
    try:
        with open("flats.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                parts = line.split(", ")
                apartment_info = {
                    "адрес": parts[0],
                    "комнат": int(parts[1]),
                    "общая_площадь": float(parts[2]),
                    "жилая_площадь": float(parts[3]),
                    "этаж": int(parts[4]),
                    "этажность": int(parts[5]),
                    "владелец": parts[6],
                    "стоимость": int(parts[7])
                }
                apartments.append(apartment_info)
    except FileNotFoundError:
        print("Файл с данными не найден. Создан новый список квартир.")
    return apartments


def display_results(apartments, mode):
    if mode == 1:
        if len(apartments) == 0:
            print("Список квартир пуст.")
            return apartments
        
        sorted_apartments = sort_by_rooms_and_price(apartments)
        print("\nСортировка по количеству комнат и стоимости:")
        print("-" * 90)
        for apt in sorted_apartments:
            print(f"Адрес: {apt['адрес']:25} | "
                  f"Комнат: {apt['комнат']:2} | "
                  f"Стоимость: {apt['стоимость']:12,} руб | "
                  f"Владелец: {apt['владелец']}")
        print()
        return apartments

    elif mode == 2:
        if len(apartments) == 0:
            print("Список квартир пуст.")
            return apartments
        
        sorted_apartments = sort_by_floor_and_price(apartments)
        print("\nСортировка по этажу, этажности дома и стоимости:")
        print("-" * 90)
        for apt in sorted_apartments:
            print(f"Адрес: {apt['адрес']:25} | "
                  f"Этаж: {apt['этаж']:3}/{apt['этажность']} | "
                  f"Стоимость: {apt['стоимость']:12,} руб")
        print()
        return apartments

    elif mode == 3:
        if len(apartments) == 0:
            print("Список квартир пуст.")
            return apartments

        sorted_apartments = sort_by_price_and_area(apartments)
        print("\nСортировка по стоимости и общей площади:")
        print("-" * 90)
        max_price, min_price = get_price_range()
        filter_apartments_by_price(sorted_apartments, max_price, min_price)
        return apartments

    elif mode == 4:
        updated_apartments = edit_apartment(apartments)
        return updated_apartments

    elif mode == 5:
        updated_apartments = add_apartment(apartments)
        return updated_apartments

    elif mode == 6:
        updated_apartments = delete_apartments(apartments)
        return updated_apartments


def main_menu():
    apartments_list = load_apartments()

    while True:
        print("\n" + "=" * 60)
        print("БАЗА ДАННЫХ РИЭЛТОРСКОГО АГЕНТСТВА")
        print("=" * 60)
        print(
            f"На данный момент кол-во объектов в БД: {len(apartments_list)}\n")

        print("Доступные функции:")
        print("1. Сортировка квартир по количеству комнат и стоимости")
        print("2. Сортировка по этажу, этажности дома и стоимости")
        print("3. Сортировка по стоимости (в указанном диапазоне) и общей площади")
        print("4. Редактировать объект")
        print("5. Добавить новый объект")
        print("6. Удалить объект")
        print("7. Выход")

        selected_mode = select_mode()

        if selected_mode == 7:
            print("До свидания!")
            break

        apartments_list = display_results(apartments_list, selected_mode)


if __name__ == "__main__":
    main_menu()
