# Define a new type of data
class Product:

    # Set the initial values
    def __init__(self, name, price, nutrition_info):
        self.name = name
        self.price = price
        self.nutrition_info = nutrition_info
        self.inventory = 0


pina_bar = Product("Piña Chocolotta", 7.99, ["200 calories", "24 g sugar"])

almond_bar = Product("Almond All Love", 12.99, ["220 calories", "18 g sugar"])

nib_bar = Product("Nom Nom Nibs", 6.99, ["180 calories", "20 g sugar"])

# Make a list with all three products
products = [pina_bar, almond_bar, nib_bar]