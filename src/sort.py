def sort_by_rooms_and_price(apartments):
    n = len(apartments)
    gap = n // 2 + 1

    while gap > 0:
        for i in range(gap, n):
            current = apartments[i]
            j = i

            while j >= gap and (
                apartments[j - gap]["комнат"] < current["комнат"] or
                (apartments[j - gap]['комнат'] == current['комнат'] and
                 apartments[j - gap]['стоимость'] > current['стоимость'])
            ):
                apartments[j] = apartments[j - gap]
                j -= gap
            apartments[j] = current
        gap //= 2
    return apartments


def sort_by_floor_and_price(apartments):
    n = len(apartments)
    gap = n // 2 + 1

    while gap > 0:
        for i in range(gap, n):
            current = apartments[i]
            j = i

            while j >= gap and (
                apartments[j - gap]["этаж"] > current["этаж"] or
                (apartments[j - gap]['этаж'] == current['этаж'] and
                 apartments[j - gap]['этажность'] > current['этажность']) or
                (apartments[j - gap]['этаж'] == current['этаж'] and
                 apartments[j - gap]['этажность'] == current['этажность'] and
                 apartments[j - gap]['стоимость'] < current['стоимость'])
            ):
                apartments[j] = apartments[j - gap]
                j -= gap
            apartments[j] = current
        gap //= 2
    return apartments


def sort_by_price_and_area(apartments):
    n = len(apartments)
    gap = n // 2 + 1

    while gap > 0:
        for i in range(gap, n):
            current = apartments[i]
            j = i

            while j >= gap and (
                apartments[j - gap]['стоимость'] < current['стоимость'] or
                (apartments[j - gap]['стоимость'] == current['стоимость'] and
                 apartments[j - gap]['общая_площадь'] > current['общая_площадь'])
            ):
                apartments[j] = apartments[j - gap]
                j -= gap
            apartments[j] = current
        gap //= 2
    return apartments


def filter_apartments_by_price(apartments, max_price, min_price):
    filtered_count = 0
    filtered_apartments = []

    for apartment in apartments:
        if min_price <= apartment['стоимость'] <= max_price:
            filtered_count += 1
            filtered_apartments.append(apartment)

    if filtered_count == 0:
        print(f"\nК сожалению, нет квартир в диапазоне стоимости:")
        print(f"от {min_price:,} руб до {max_price:,} руб\n")
        return False
    else:
        print(f"\nНайдено квартир: {filtered_count}")
        print("-" * 90)
        for apartment in filtered_apartments:
            print(f"Стоимость: {apartment['стоимость']:12,} руб | "
                  f"Общая площадь: {apartment['общая_площадь']:8.1f} м² | "
                  f"Адрес: {apartment.get('адрес', 'не указан')}")
        print()
        return True
