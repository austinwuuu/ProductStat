import os
products = []
if os.path.isfile('product_stat.csv'):
    print('File exists')
    with open('product_stat.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if 'Product,Price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
else:
    print('File not found')

#product input
while True:
    name = input("Enter the product's name: ")
    if name == 'q':
        break
    price = input("Enter the product's price: ")
    price = int(price)
    products.append([name, price])
print(products)


# print buying history
for p in products:
    print('The price of', p[0], 'is', p[1])

with open ('product_stat.csv', 'w', encoding='utf-8') as f:
    f.write('Product,Price\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')
    
