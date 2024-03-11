import csv

with open('products (1).csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=';'))
    reader = sorted(reader, key=lambda x: float(x['Count']))
    naim = []
    for row in reader:
        naim.append(f'{row["Category"]},{row["Count"]}')
        count_tovara = row['Count']
        row['category naim'] = count_tovara
    print(naim[:10])

with open('hesh_table.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count', 'category naim'],
                            delimiter=';')
    writer.writeheader()
    writer.writerows(reader)

