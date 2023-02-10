import unittest

def fuel_requirement(mass):
    fuel = mass // 3 - 2
    return 0 if fuel <= 0 else fuel + fuel_requirement(fuel)

class TestFuelRequirement(unittest.TestCase):
    def test_fuel_requirement(self):
        self.assertEqual(fuel_requirement(12), 2)
        self.assertEqual(fuel_requirement(14), 2)
        self.assertEqual(fuel_requirement(1969), 966)
        self.assertEqual(fuel_requirement(100756), 50346)

if __name__ == '__main__':
    unittest.main()
