class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class CashRegister:

    def __init__(self):

        self.total_price = 0
        self.discount = 0
        self.total_items = []

    def add_item(self, item):
        self.total_items.append(item)
        print(f"{item.name} has been added to your basket.")

    def remove_item(self, item):
        self.total_items.remove(item)
        print(f"{item.name} has been removed from your basket.")

    def apply_discount(self, discount_amount):
        self.discount += discount_amount

    def get_total(self):
        self.total_price = 0
        for item in self.total_items:
            self.total_price += item.price
        return self.total_price - self.discount

    def show_items(self):
        print("Items in current basket:")
        for item in self.total_items:
            print(f"Item: {item.name}, Price: {item.price}")

    def reset_register(self):
        self.total_items = []
        self.total_price = 0
        self.discount = 0

bukky_basket = CashRegister()
jess_basket = CashRegister()
michelle_basket = CashRegister()

sofa = Item("sofa", 80.00)
chair = Item("chair", 50.00)
table = Item("table", 60.00)
lamp = Item("lamp", 20.00)

bukky_basket.add_item(sofa)
michelle_basket.add_item(lamp)
michelle_basket.add_item(table)
jess_basket.add_item(chair)

michelle_basket.remove_item(lamp)

bukky_basket.show_items()
michelle_basket.show_items()
jess_basket.show_items()

bukky_basket.apply_discount(5)

print(f"Bukky's total amount is now £{bukky_basket.get_total()} with a £5 discount.")
print(f"Bukky and Jess' baskets total to £{bukky_basket.get_total() + jess_basket.get_total()} altogether.")

bukky_basket.reset_register()
michelle_basket.reset_register()
jess_basket.reset_register()
