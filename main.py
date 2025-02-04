from conversion import *

def convert(initial_unit_name=None, initial_unit_quantity=None, category=None):
    """
    """
    if type(initial_unit_quantity) not in [int, float] or initial_unit_quantity < 0:
        raise ValueError("`initial_unit_quantity` must be a non-negative float or int!")
    
    return UnitConverter(conversion_table, initial_unit_name=initial_unit_name, initial_unit_quantity=initial_unit_quantity, category=category).unit

def print_unit(unit):
    """
    """




def main():
    pass

if __name__ == "__main__":
    main()