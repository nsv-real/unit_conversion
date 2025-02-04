from collections import namedtuple

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
    }
}

Weight = namedtuple('Weight', ['kgs', 'pounds', 'ounces'])

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


if __name__ == "__main__":
    print(convert_kg(10))
    print(convert_pounds(10))
    print(convert_ounces(10))
