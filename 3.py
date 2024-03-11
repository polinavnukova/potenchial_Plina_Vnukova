import csv

# открываем файл
with open('products (1).csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=';'))
    request = input()
    reader = sorted(reader, key=lambda x: float(x['Count']))
    catigori = []
    # считываем строчки, выводим товар с наименьшим кол-ом продаж, пока не введется стоп слово
    # while request != 'молоко':
    #     for row in reader:
    #         if row['Category'] not in catigori:
    #             catigori.append(row['Category'])
    #             print(f'{row["Category"]} товар: {row["product"]} был куплен {row["Count"]} раз')
    #             break
    while request != 'молоко':
        is_real_category = False
        for i in range(len(reader)):
            if reader[i]['Category'] == request:
                category = reader[i]['Category']
                name = reader[i]['product']
                summ = reader[i]['Count']
                print(f'{category} товар: {name} был куплен {summ} раз')
                is_real_category = True
                break
        if not is_real_category:
            print('Такой категории не существует в нашей БД')
        request = input()

    request = input()





