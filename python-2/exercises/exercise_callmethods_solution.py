# Define a new type of data
class Product:

    # Set the initial values
    def __init__(self, name, price, nutrition_info):
        self.name = name
        self.price = price
        self.nutrition_info = nutrition_info
        self.inventory = 0

    # Define methods
    def increase_inventory(self, amount):
        self.inventory += amount

    def reduce_inventory(self, amount):
        self.inventory -= amount

    def get_label(self):
        return "Foxolate Shop: " + self.name

    def get_inventory_report(self):
        if self.inventory == 0:
            return "There are no bars!"
        return f"There are {self.inventory} bars."

pina_bar = Product("Piña Chocolotta", 7.99,
    ["200 calories", "24 g sugar"])

# Replace this comment with a method call that
# increases the inventory by 6 bars
pina_bar.increase_inventory(6)

# Should report "There are 6 bars"
report1 = pina_bar.get_inventory_report()

# Replace this comment with a method call that
# decreases the inventory by 1 bar
pina_bar.reduce_inventory(1)

# Should report "There are 5 bars"
report2 = pina_bar.get_inventory_report()

# Replace this comment with a method call that
# increases the inventory by 25 bars
pina_bar.increase_inventory(25)

# Should report "There are 30 bars"
report3 = pina_bar.get_inventory_report()

# Replace this comment with a method call that
# decreases the inventory by 30 bars
pina_bar.reduce_inventory(30)

# Should report "There are no bars!"
report4 = pina_bar.get_inventory_report()

"""
If you have extra time, try to adjust the  reduce_inventory method so that inventory never goes below zero,
and adjust the get_inventory_report method so that it says "bar" instead of bar" when inventory is only 1.
"""