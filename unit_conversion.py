class Weight:
    allowed_units = ["oz", "lb", "kg"]
    conversion_table = {
        "kg": {
            "lb": 2.20462,
            "oz": 35.274
        },
        "lb": {
            "kg": 0.453592,
            "oz": 16.0
        },
        "oz": {
            "kg": 0.0283,
            "lb": 0.0625
        }
    }
    
    def __init__(self, initial_unit_name=None, initial_unit_quantity=None):
        if initial_unit_name.lower() not in self.allowed_units:
            raise ValueError(f"`initial_unit_name` parameter must be one of \
                             {' '.join(self.allowed_units)}!")
        else:
            self.initial_unit_name = initial_unit_name.lower()

        self.initial_unit_quantity = float(initial_unit_quantity)

        self.calculate_units()
       

    def calculate_units(self):
        unit_conversion = self.conversion_table[self.initial_unit_name]

        setattr(self, self.initial_unit_name, self.initial_unit_quantity);

        for unit, conversion in unit_conversion.items():
            setattr(self, unit, self.initial_unit_quantity * conversion)