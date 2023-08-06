from component import Component

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def get_price(self):
        total_price = 0
        for child in self.children:
            total_price += child.get_price()
        return total_price
