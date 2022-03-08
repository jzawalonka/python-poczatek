class Product:
    def __init__(self, name, category_name, price):
        self.name = name
        self.categoty_name = category_name
        self.price = price


class Order:
    def __init__(self, name, sum, products_list=None):
        self.name = name
        if products_list is None:
            products_list = []
        self.products_list = products_list
        self.sum = sum
        i = 0
        for i in range(0, len(products_list)):
            sum += products_list[i]


class Apple:
    def __init__(self, types, size, price_for_kg):
        self.types = types
        self.size = size
        self.price_for_kg = price_for_kg


class Potato:
    def __init__(self, types, size, price_for_kg):
        self.types = types
        self.size = size
        self.price_for_kg = price_for_kg


def wypisz():
    lobo = Apple(types="lobo", size="M", price_for_kg=3)
    zolty_ziemniak = Potato(types="zolty", size="L", price_for_kg=2)
    zamawiajacy = Order(name ="Jakub Zawalonka", )

def run_program():
    print("aaa")


if __name__ == "__main__":
    run_program()
