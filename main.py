from leaf import Leaf
from composite import Composite

def main():
    tablet = Leaf("Tablet", 300)
    syrup = Leaf("Syrup", 150)

    antibiotics = Composite()
    antibiotics.add(tablet)
    antibiotics.add(syrup)

    vitamins = Composite()
    vitamins.add(Leaf("Vitamin C", 50))
    vitamins.add(Leaf("Vitamin D", 60))

    medical_supplies = Composite()
    medical_supplies.add(antibiotics)
    medical_supplies.add(vitamins)

    # Calculate the total price
    total_price = medical_supplies.get_price()
    print(f"Total price of medical supplies: {total_price}")

if __name__ == "__main__":
    main()
