import unittest

def fuel_requirement(mass):
    return mass // 3 - 2

class TestFuelRequirement(unittest.TestCase):
    def test_fuel_requirement(self):
        self.assertEqual(fuel_requirement(12), 2)
        self.assertEqual(fuel_requirement(14), 2)
        self.assertEqual(fuel_requirement(1969), 654)
        self.assertEqual(fuel_requirement(100756), 33583)

if __name__ == '__main__':
    unittest.main()