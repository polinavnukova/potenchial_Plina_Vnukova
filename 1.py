import csv

with open('products (1).csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=';'))
    summa_zakusok = []
    for row in reader:
        veruchka = float(row['Price per unit']) * float(row['Count'])
        row['total'] = veruchka
        if row['Category'] == 'Закуски':
            rashet = float(row['Price per unit']) * float(row['Count'])
            summa_zakusok.append(rashet)
    print(sum(summa_zakusok))

with open('products_new.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count', 'total'],
                            delimiter=';')
    writer.writeheader()
    writer.writerows(reader)
