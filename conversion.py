conversion_table = {
        "weight": {
            "kg": {
                "pound": 2.20462,
                "ounce": 35.274
            },
            "pound": {
                "kg": 0.453592,
                "ounce": 16
            },
            "ounce": {
                "kg": 0.0283,
                "pound": 0.0625
            }
        },

        "fluid":  {
            "floz": {
                "gallon": 0.0078125,
                "quart": 0.03125,
                "pint": 0.0625,
                "cup": 0.1232238,
                "milliliter": 29.5735,
                "liter": 0.0295735
            },
            "cup": {
                "gallon": 0.0634013,
                "quart": 0.253605,
                "pint": 0.50721,
                "floz": 8,
                "milliliter": 240,
                "liter": 0.24
            },
            "pint": {
                "gallon": 0.125,
                "quart": 0.5,
                "cup": 2,
                "floz": 16,
                "milliliter": 473.176,
                "liter": 0.473176
            },
            "quart": {
                "gallon": 0.25,
                "pint": 2,
                "cup": 4,
                "floz": 32,
                "milliliter": 946.353,
                "liter": 0.946353
            },
            "gallon": {
                "quart": 4,
                "pint": 8,
                "cup": 16,
                "floz": 128,
                "milliliter": 3785.41,
                "liter": 3.78541
            },
            "milliliter": {
                "gallon": 0.000264172,
                "quart": 0.00105669,
                "pint": 0.00211338,
                "cup": 0.00416667,
                "floz": 0.033814,
                "liter": 0.001
            },
            "liter": {
                "gallon": 0.264172,
                "quart": 1.05669,
                "pint": 2.11338,
                "cup": 4.22676,
                "floz": 33.814,
                "milliliter": 1000
            }
        }
}    

class Unit:
    """ Unit class
    """
    def __init__(self, initial_unit_name, initial_unit_quantity, category, converted_units):
        """ __init__ method
            param - initial_unit_name - 'kg', 'pound', 'liter', etc.
            param - initial_unit_quantity - an int or float specifying how many units
            param - category - one of 'fluid' or 'weight'
            param - converted_units - a list of converted unit names
        """
        self.initial_unit_name = initial_unit_name
        self.initial_unit_quantity = initial_unit_quantity
        self.category = category
        self.converted_units = converted_units
    
    def __repr__(self):
        return f"Unit<Category: {self.category.title()}, Initial unit: {self.initial_unit_name}, Initial value: {self.initial_unit_quantity}, Converted: {self.converted_units}>"

class UnitConverter:
    """ UnitConveted class
    """
    
    def __init__(self, conversion_table, initial_unit_name=None, initial_unit_quantity=None, category=None):
        """ __init__ method
        param - initial_unit_name - 'kg', 'pound', 'liter', etc.
        param - initial_unit_quantity - an int or float specifying how many units
        param - category - one of 'fluid' or 'weight'
        """
        self.category = category

        try:
            self.conversion_table = conversion_table[self.category]
        except KeyError as e:
            raise ValueError(f"Category `{category}` not found in conversion table")

        self.allowed_units = list(self.conversion_table.keys())
        
        if initial_unit_name.lower() not in self.allowed_units:
            raise ValueError(f"`category` must be one of: {' '.join(self.allowed_units)}")
        
        self.initial_unit_name = initial_unit_name.lower()

        if type(initial_unit_quantity) not in [int, float] or initial_unit_quantity < 0:
            raise ValueError("`initial_unit_quantity` must be a non-negative float or int!")

        self.initial_unit_quantity = initial_unit_quantity
        self.calculate_conversions()

    def calculate_conversions(self):
        """ calculate_conversion method
            calculates/initializes Unit object
        """

        conversions = self.conversion_table[self.initial_unit_name]

        self.unit = Unit(self.initial_unit_name, self.initial_unit_quantity, self.category, list(conversions.keys()))

        for unit, conversion in conversions.items():
            setattr(self.unit, unit, conversion * self.initial_unit_quantity)

    def __repr__(self):
        return f"UnitConverter<Category: {self.category.title()}, Initial unit: {self.initial_unit_name}, Initial value: {self.initial_unit_quantity}>"
