from conversion import *

def convert(initial_unit_name=None, initial_unit_quantity=None, category=None):
    """
    """
    return UnitConverter(conversion_table, initial_unit_name=initial_unit_name, initial_unit_quantity=initial_unit_quantity, category=category).unit

def print_unit(unit):
    """
    """
    print(unit)
    print(f"Starting unit is: {unit.initial_unit_name}")
    print(f"Starting quanity is: {unit.initial_unit_quantity}")

    for units in unit.converted_units:
        print(f"Unit: {units}, Value:{getattr(unit, units)}")
    


def main():
    pass

if __name__ == "__main__":
    main()