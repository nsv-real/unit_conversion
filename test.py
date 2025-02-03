import unittest
from functools import wraps

from weight_convert import *

class TestFunctions(unittest.TestCase):

    def test_convert_kg(self):
        print("*** START Testing `convert_kg` ***")
        unit = "kg"
        weight = 2.2
        print(f"Unit is {unit}")
        print(f"--- Weight is {weight}")
        kg_weights = convert_kg(weight)
        
        self.assertEqual(kg_weights.kgs, weight)
        print(f"`kgs` field should equal weight {weight}")

        ounce_to_kg = conversion["kg"]["ounce"]
        self.assertEqual(kg_weights.ounces, ounce_to_kg * weight)
        print("`ounces` field in result should equal {0} * {1}({2}) = {3}".format(ounce_to_kg, weight, unit, ounce_to_kg * weight ))

        pound_to_kg = conversion["kg"]["pound"]
        self.assertEqual(kg_weights.pounds, pound_to_kg * weight)
        print("`pounds` field in result should equal {0} * {1}({2}) = {3}".format(pound_to_kg, weight, unit, pound_to_kg * weight ))
        
        print("*** Finish Testing `convert_kg` ***")
        print("-----")

    def test_convert_pounds(self):
        print("*** START Testing `convert_pounds` ***")
        unit = "lbs"
        weight = 1
        print(f"Unit is {unit}")
        print(f"--- Weight is {weight}")
        lb_weights = convert_pounds(weight)
        
        self.assertEqual(lb_weights.pounds, weight)
        print(f"`pounds` field should equal weight {weight}")

        ounces_to_pounds = conversion["pound"]["ounce"]
        self.assertEqual(lb_weights.ounces, ounces_to_pounds * weight)
        print("`ounces` field in result should equal {0} * {1}({2}) = {3}".format(ounces_to_pounds, weight, unit, ounces_to_pounds * weight ))

        self.assertEqual(lb_weights.kgs, conversion["pound"]["kg"] * weight)
        print("`kgs` field in result should equal {0} * {1}({2}) = {3}".format(conversion["pound"]["kg"], weight, unit, conversion["pound"]["kg"] * weight ))
        
        print("*** Finish Testing `convert_kg` ***")
        print("-----")

    def test_convert_ounces(self):
        print("*** START Testing `convert_ounces` ***")
        unit = "oz"
        weight = 16
        print(f"Unit is {unit}")
        print(f"--- Weight is {weight}")
        oz_weights = convert_ounces(weight)
        
        self.assertEqual(oz_weights.ounces, weight)
        print(f"`ounces` field should equal weight {weight}")

        pounds_to_ounces = conversion["ounce"]["pound"]
        self.assertEqual(oz_weights.pounds, pounds_to_ounces * weight)
        print("`pounds` field in result should equal {0} * {1}({2}) = {3}".format(pounds_to_ounces, weight, unit, pounds_to_ounces * weight ))

        kgs_to_ounces = conversion["ounce"]["kg"]
        self.assertEqual(oz_weights.kgs, kgs_to_ounces * weight)
        print("`kgs` field in result should equal {0} * {1}({2}) = {3}".format(kgs_to_ounces, weight, unit, kgs_to_ounces * weight ))
        
        print("*** Finish Testing `convert_ounces` ***")
        print("-----")

if __name__ == '__main__':
    unittest.main()