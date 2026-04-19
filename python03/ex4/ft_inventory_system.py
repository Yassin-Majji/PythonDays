import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    DIGITS = dict({"0": 0, "1": 1, "2": 2, "3": 3,
                   "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
                   })

    inventory = dict()

    if len(sys.argv) < 2:
        print(f"No inventory provided. Usage: python3 "
              f"{sys.argv[0]} <item:qty> <item:qty> ...")
        return

    data = []
    for arg in sys.argv[1:]:
        valid = 0
        i = 0
        while (i < len(arg)):
            if (arg[i] == ':' and i != 0 and i + 1 < len(arg)):
                valid = 1
            i += 1
        if (not valid):
            print(f"Invalid item format: '{arg}'. "
                  f"Expected 'name:quantity' example: sword:1")
            return
        data += [arg]

    for item in data:
        key = ""
        value = ""
        i = 0
        while (item[i] != ':'):
            key += item[i]
            i += 1
        i += 1
        while (i < len(item)):
            value += item[i]
            i += 1
        i = 0
        n = 0
        while i < len(value):
            d = value[i]
            if d not in DIGITS:
                print(f"Non-numeric or invalid quantity: '{value}'")
                return
            n = (n * 10) + DIGITS.get(d)
            i += 1
        if "items" not in inventory:
            inventory["items"] = {}
        inventory["items"].update({key: n})

    total_items = 0
    unique_items = 0
    inventory["statistics"] = {}
    inventory["statistics"]["most_abundant"] = {}
    inventory["statistics"]["least_abundant"] = {}
    in_first = 1
    for key, value in inventory["items"].items():
        if (in_first):
            inventory["statistics"]["most_abundant"].update(
                {"name": key, "quantity": value})
            inventory["statistics"]["least_abundant"].update(
                {"name": key, "quantity": value})
            in_first = 0
        if (value < inventory["statistics"]["least_abundant"].get("quantity")):
            inventory["statistics"]["least_abundant"].update(
                {"name": key, "quantity": value})

        if (value > inventory["statistics"]["most_abundant"].get("quantity")):
            inventory["statistics"]["most_abundant"].update(
                {"name": key, "quantity": value})

        total_items += value
        unique_items += 1

    inventory["statistics"].update(
        {"total_items": total_items})
    inventory["statistics"].update(
        {"unique_items": unique_items})

    total = inventory["statistics"].get("total_items")
    print(f"Total items in inventory: {total}")
    unique = inventory["statistics"].get("unique_items")
    print(f"Unique item types: {unique}")
    print()

    data = []
    for value in inventory["items"].values():
        data += [value]
    i = 0
    while (i < len(data) - 1):
        j = i + 1
        while (j < len(data)):
            if (data[j] > data[i]):
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
            j += 1
        i += 1

    print("=== Current Inventory ===")
    keys_prev = []
    for v in data:
        for key, value in inventory["items"].items():
            unit = "units"
            if (value == 1):
                unit = "unit"
            if (v == value and key not in keys_prev):
                keys_prev += [key]
                percent = (value / inventory['statistics'].
                           get('total_items')) * 100
                print(f"{key}: {value} {unit} ({percent:.1f}%)")
    print()
    most = inventory['statistics']["most_abundant"]
    least = inventory['statistics']["least_abundant"]

    print("=== Inventory Statistics ===")
    print(f"Most abundant: {most.get('name')} ({most.get('quantity')} units)")
    print(f"Least abundant: {least.get('name')} ({least.get('quantity')} unit)"
          )
    print()

    print("=== Item Categories ===")

    inventory["Categories"] = {}
    inventory["Categories"]["moderate"] = {}
    inventory["Categories"]["scarce"] = {}
    for key, value in inventory['items'].items():
        if (value >= 5):
            inventory["Categories"]["moderate"].update({key: value})
        else:
            inventory["Categories"]["scarce"].update({key: value})
    print(f"Moderate: {inventory['Categories']['moderate']}")
    print(f"Scarce: {inventory['Categories']['scarce']}")
    print()

    count = len(inventory["items"])
    i = 0
    print("=== Management Suggestions ===")
    print("Restock needed:", end="")
    for key, value in inventory["items"].items():
        if i == 1:
            print(", ", end="")
            i = 0
        if (value <= 1):
            print(key, end="")
            i = 1
    print("\n")
    i = 0
    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys: ", end="")
    for key in inventory['items'].keys():
        print(key, end="")
        if i < count - 1:
            print(", ", end="")
        i += 1
    print()
    i = 0
    print("Dictionary values: ", end="")
    for value in inventory['items'].values():
        print(value, end="")
        if i < count - 1:
            print(", ", end="")
        i += 1
    print()
    key = "sword"
    is_find = key in inventory['items'] and inventory['items'][key] > 0
    print(f"Sample lookup - '{key}' in inventory: {is_find}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
