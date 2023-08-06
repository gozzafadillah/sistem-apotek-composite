from component import Component

class Leaf(Component):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    # Tambahkan ini untuk mengimplementasikan metode abstrak, meskipun tidak melakukan apa-apa.
    def add(self, component):
        pass

    def remove(self, component):
        pass
