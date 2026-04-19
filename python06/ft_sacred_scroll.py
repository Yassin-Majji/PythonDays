import alchemy

print("\n=== Sacred Scroll Mastery ===\n")

print("Testing direct module access:")
print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
print("alchemy.elements.create_water():", alchemy.elements.create_water())
print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
print("alchemy.elements.create_air():", alchemy.elements.create_air())

print("\nTesting package-level access (controlled by __init__.py):")

list_function_names = ["create_fire", "create_water",
                       "create_earth", "create_air"]

for func_name in list_function_names:
    try:
        result = getattr(alchemy, func_name)()
        print(f"alchemy.{func_name}(): {result}")
    except AttributeError:
        print(f"alchemy.{func_name}(): AttributeError - not exposed")

print("\nPackage metadata:")
print(f"Version: {alchemy.__version__}")
print(f"Author: {alchemy.__author__}")
