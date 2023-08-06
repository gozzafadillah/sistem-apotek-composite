import unittest
from leaf import Leaf
from composite import Composite

class TestApotek(unittest.TestCase):
    def test_leaf(self):
        tablet = Leaf("Tablet", 300)
        syrup = Leaf("Syrup", 150)

        self.assertEqual(tablet.get_price(), 300)
        self.assertEqual(syrup.get_price(), 150)

    def test_composite(self):
        antibiotics = Composite()
        antibiotics.add(Leaf("Paracetamol", 100))
        antibiotics.add(Leaf("Amoxicillin", 200))

        vitamins = Composite()
        vitamins.add(Leaf("Vitamin C", 50))
        vitamins.add(Leaf("Vitamin D", 60))

        medical_supplies = Composite()
        medical_supplies.add(antibiotics)
        medical_supplies.add(vitamins)

        # Total price of antibiotics: 100 + 200 = 300
        # Total price of vitamins: 50 + 60 = 110
        # Total price of medical supplies: 300 + 110 = 410
        self.assertEqual(medical_supplies.get_price(), 410)

if __name__ == "__main__":
    unittest.main()
