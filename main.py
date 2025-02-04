from conversion import *

def convert(initial_unit_name=None, initial_unit_quantity=None, category=None):
    """ `convert` function
         param - initial_unit_name - 'kg', 'pound', 'liter', etc.
         param - initial_unit_quantity - an int or float specifying how many units
         param - category - one of 'fluid' or 'weight'
         returns Unit object
    """
    return UnitConverter(conversion_table, initial_unit_name=initial_unit_name, initial_unit_quantity=initial_unit_quantity, category=category).unit

def print_unit(unit):
    """ `print_unit` function
         param - unit - Unit object
         returns None
    """
    print("[+] Starting conversion...")
    print(unit)
    print(f"Starting unit is: {unit.initial_unit_name}")
    print(f"Starting quanity is: {unit.initial_unit_quantity}")

    for units in unit.converted_units:
        print(f"Unit: {units}, Value: {getattr(unit, units)}")
    
    print("[+] Ending conversion...")

def main():
    """ Main function
    """

    fluids = [ ["floz", 16, "fluid"], ["liter", 4, "fluid"], ["quart", 4, "fluid"], ["cup", 16, "fluid"] ]
    weights = [ ["ounce", 16, "weight"], ["pound", 1, "weight"], ["kg", 2.2, "weight" ] ]

    print("Converting fluids...")
    for fluid in fluids:
        u = convert(initial_unit_name=fluid[0], initial_unit_quantity=fluid[1], category=fluid[2])
        print_unit(u)
    print()
    print()
    print("Converting weights...")
    for weight in weights:
        u = convert(initial_unit_name=weight[0], initial_unit_quantity=weight[1], category=weight[2])
        print_unit(u)

if __name__ == "__main__":
    main()
