def get_products(products, max_price):
    affordable_products = []
    for product in products:
        if product['цена'] <= max_price:
            affordable_products.append(product['продукт'])
    return affordable_products

def test_no_affordable_products():
    products = [{'продукт': 'хлеб', 'цена': 30}, {'продукт': 'молоко', 'цена': 40}]
    max_price = 20
    assert get_products(products, max_price) == []

def test_all_affordable_products():
    products = [{'продукт': 'хлеб', 'цена': 25}, {'продукт': 'молоко', 'цена': 15}]
    max_price = 50
    assert get_products(products, max_price) == ['хлеб', 'молоко']

def test_some_affordable_products():
    products = [{'продукт': 'хлеб', 'цена': 25}, {'продукт': 'молоко', 'цена': 60}]
    max_price = 30
    assert get_products(products, max_price) == ['хлеб']

def test_empty_list():
    products = []
    max_price = 100
    assert get_affordable_products(products, max_price) == []