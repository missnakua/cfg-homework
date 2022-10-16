"""

TASK 1

Write a class to represent a Cash Register.
Your class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. You can add new variables and functions if you want to.
2. You will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""

class CashRegister:

    def __init__(self, total_items, total_price, is_full_price=False):
        """
        Initialises an empty list to hold purchased items.
        Compulsory attributes: total_items, total_price
        Optional attributes: discount
        20% off items where discount applies.
        """
        # is discount = "item is at a discount of 0.80 if it is not full price, as full price equals false"
        self.total_items = None # {'item': 'price'}
        self.total_price = 0
        self.is_full_price = is_full_price
        self.discount = 0.8 if is_full_price else None
        self.items = []


    def add_item(self, item, price):
        return self.items.append(item, price)


    def remove_item(self, item):
        return self.items.remove(item)


    def apply_discount(self):
        """
        Applies a 20% off discount to items at checkout.
        """
        # if self.is_full_price=False:
        #     self.items * 0.8
        #     print(f"This item is discounted.")
        # else:
        #     print(f"This item is full price")

    def get_total(self, price):
        """
        Calculates the total price of items in the Cash Register at checkout.
        """
        self.total_price = 0
        for self.item in self.items:
            total += bukky_shopping_list.get("price")
            return total


    def show_items(self):
        """
        Returns a list of all items in the Cash Register.
        """
        for self.item in self.items:
            print("Item Description:", self.items.get("item")),
            print(str("Price:",self.pr))

            show_items = customer_item.get("item")
            return show_items



    def reset_register(self):
        """
        Clears the Cash Register
        """
        self.total_items.clear()
        self.total_price = 0
        self.discount = 0
        self.total_items[:] = []


# EXAMPLE code run:
# Instantiate the Cash Register class
bukky_shopping_list = {"sofa": 82.00, "kettle": 5.00}
shopping_list = CashRegister()

bukky_items = CashRegister(total_items=5, total_price=20)

bukky_items.add_item("watermelon", 8.00)
print(bukky_items)


# jess_shopping_list = CashRegister()
# michelle_shopping_list = CashRegister()
# azeez_shopping_list = CashRegister()
# lauren_shopping_list = CashRegister()