import csv

# открываем файл
with open('products (1).csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=';'))
    # считываем каждую строчку из файла
    for row in reader:
        name = [bukva for bukva in row['product']]
        data = [number for number in row['Date']]
        # генерируем промокоды
        login = f'{name[0]}{name[1]}{data[0]}{data[1]}{name[-2]}{name[-1]}{data[4]}{data[3]}'
        row['promocode']  = login

# создаем новый файл
with open('product_promo.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count', 'promocode'],
                            delimiter=';')
    writer.writeheader()
    writer.writerows(reader)

