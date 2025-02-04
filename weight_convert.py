from collections import namedtuple
from functools import wraps

conversion = {
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
    },
    "floz": {
        "gallon": 128,
        "quart": 32,
        "pint": 16,
        "cup": 8,
        "milliliter": 29.6,
        "liter": 33.814
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
    return Weight(value, conversion[unit]["pound"] * value, 
                  conversion[unit]["ounce"] * value)

def convert_pounds(value):
    unit = "pound"
    """American pound to ounce and kilogram.
       `value` is int or float.
       Returns `Weight` named tuple.
    """
    return Weight(conversion[unit]["kg"] * value, value,
                  conversion[unit]["ounce"] * value)

def convert_ounces(value):
    unit = "ounce"
    """American ounce to pound and kilogram.
       `value` is int or float.
       Returns `Weight` named tuple.
    """
    return Weight(conversion[unit]["kg"] * value, 
                  conversion[unit]["pound"] * value, value)


## FluidVolume = namedtuple("FluidVolume", ["floz", "cup", "pint", "quart", "gallon", "milliliter", "liter"])


def convert_gallons(value):
    

    return FluidVolume(conversion["floz"]["gallon"] * value, conversion["floz"]["gallon"] / conversion["floz"] )
