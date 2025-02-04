

weight_conversion = {
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
}

fluid_volume_conversion = {
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

class Weight:
    def __init__(self, initial_unit_name, initial_unit_quanity):
        self.initial_unit_name = initial_unit_name
        self.initial_unit_quantity = initial_unit_quanity
        self.conversion_values = {}

    def __repr__(self):
        return f"Weight<Initial unit: {self.initial_unit_name}, initial value: {self.initial_unit_quantity} converted: {self.conversion_values}>"

class WeightConverter:
    def __init__(self, conversion_table, initial_unit_name=None, initial_unit_quantity=None):
        self.conversion_table = conversion_table
        self.allowed_units = list(self.conversion_table.keys())

        if initial_unit_name.lower() not in self.allowed_units:
            raise ValueError(f"`initial_unit_name` parameter must be one of \
                             {' '.join(self.allowed_units)}!")
        
        if type(initial_unit_quantity) not in [int, float] or initial_unit_quantity < 0:
            raise ValueError("`initial_unit_quanity` must be a positve `int` or `float`")
        
        self.initial_unit_name = initial_unit_name.lower()
        self.initial_unit_quantity = initial_unit_quantity

        self.calculate_conversions()

    def calculate_conversions(self):

        self.weight = Weight(self.initial_unit_name, self.initial_unit_quantity)

        conversions = self.conversion_table[self.initial_unit_name]

        for unit, conversion in conversions.items():
            self.weight.conversion_values[unit] = conversion


class FluidVolume:
    def __init__(self, initial_unit_name, initial_unit_quanity):
        self.initial_unit_name = initial_unit_name
        self.initial_unit_quantity = initial_unit_quanity
        self.conversion_values = {}

    def __repr__(self):
        return f"FluidVolume<Initial unit: {self.initial_unit_name}, initial value: {self.initial_unit_quantity} converted: {self.conversion_values}>"
    
class FluidVolumeConverter:
    def __init__(self, conversion_table, initial_unit_name=None, initial_unit_quantity=None):
        self.conversion_table = conversion_table
        self.allowed_units = list(self.conversion_table.keys())

        if initial_unit_name.lower() not in self.allowed_units:
            raise ValueError(f"`initial_unit_name` parameter must be one of \
                             {' '.join(self.allowed_units)}!")
        
        if type(initial_unit_quantity) not in [int, float] or initial_unit_quantity < 0:
            raise ValueError("`initial_unit_quanity` must be a positve `int` or `float`")
        
        self.initial_unit_name = initial_unit_name.lower()
        self.initial_unit_quantity = initial_unit_quantity

        self.calculate_conversions()

    def calculate_conversions(self):

        self.fluid_volume = FluidVolume(self.initial_unit_name, self.initial_unit_quantity)

        conversions = self.conversion_table[self.initial_unit_name]

        for unit, conversion in conversions.items():
            self.fluid_volume.conversion_values[unit] = conversion    
