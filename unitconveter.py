LENGTH = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000, "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.34}
WEIGHT = {"mg": 0.000001, "g": 0.001, "kg": 1, "t": 1000, "oz": 0.0283495, "lb": 0.453592}

def convert(value, from_unit, to_unit, units):
    in_base = value * units[from_unit]
    return in_base / units[to_unit]

print("=== unit converter ===")
print("1, length")
print("2, weight")

choice = input("choose 1 or 2:")

if choice == "1":
    units = LENGTH
    
elif choice == "2":
    units = WEIGHT
    
else:
    print("Invalid choice")
    exit()
    
print("Available units:", ", ".join(units.keys()))
value = float(input("Enter the value to convert: "))
from_unit = input("from unit: ")
to_unit = input("to unit: ")

if from_unit in units and to_unit   in units:
    result = convert(value, from_unit, to_unit, units)
    print(f"{value} {from_unit} = {result} {to_unit}")
    
else:print("unknown unit.")
      