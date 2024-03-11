import pandas as pd
from rbuilder.models import Locations, Links


def xl_to_db():
    # Чтение данных из Excel
    df = pd.read_excel('rbuilder/prices_100.xlsx', index_col=0)
    locations_col = df.columns.tolist()
    # print(addresses_col)
    locations_line = df.index.tolist()
    # print(addresses_line)
    # print(addresses_col == addresses_line)

    # Обработка и сохранение локаций
    address_objects = {}
    for loc in locations_col:
        # Разделение адреса на составные части
        country, city, address = loc.split('.')
        address_obj, _ = Locations.objects.get_or_create(country=country, city=city, addr=address)
        address_objects[loc] = address_obj

    # Обработка и сохранение связей
    for row_address in df.index:
        for col_address in df.columns:
            price = df.at[row_address, col_address]
            if not pd.isna(price):  # Проверка на отсутствие данных
                addr_1 = address_objects[row_address]
                addr_2 = address_objects[col_address]
                print(f'{addr_1} - {addr_2} for {price}')
                Links.objects.get_or_create(loc_1=addr_1, loc_2=addr_2, bandwidth=100, price=price)
