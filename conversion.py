from collections import namedtuple
from functools import wraps

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

Weight = namedtuple("Weight", ["kgs", "pounds", "ounces"])
FluidVolume = namedtuple("FluidVolume", ["floz", "cup", "pint", "quart", "gallon", "milliliter", "liter"])

def check_conversion_value():
    pass

def convert_kg(value):
    unit = "kg"
    """Kilogram to American ounce and pound.
       `value` is int or float.
       Returns `Weight` named tuple.
    """
    return Weight(value, weight_conversion[unit]["pound"] * value, 
                  weight_conversion[unit]["ounce"] * value)

def convert_pounds(value):
    unit = "pound"
    """American pound to ounce and kilogram.
       `value` is int or float.
       Returns `Weight` named tuple.
    """
    return Weight(weight_conversion[unit]["kg"] * value, value,
                  weight_conversion[unit]["ounce"] * value)

def convert_ounces(value):
    unit = "ounce"
    """American ounce to pound and kilogram.
       `value` is int or float.
       Returns `Weight` named tuple.
    """
    return Weight(weight_conversion[unit]["kg"] * value, 
                  weight_conversion[unit]["pound"] * value, value)


## FluidVolume = namedtuple("FluidVolume", ["floz", "cup", "pint", "quart", "gallon", "milliliter", "liter"])


