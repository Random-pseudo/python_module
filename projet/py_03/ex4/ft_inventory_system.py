import sys

def main():
    print("=== Inventory System Analysis ===")
    inventory = {}

    for arg in sys.argv[1:]:
        if ':' not in arg:
            print("Error - invalid parameter '" + arg + "'")
            continue
        item, quantity = arg.split(':', 1)
        if item in inventory:
            print("Redundant item '" + item + "' - discarding")
            continue
        try:
            quantity = int(quantity)
            inventory[item] = quantity
        except ValueError as e:
            print("Quantity error for '" + item + "':" + e)

    print("Got inventory: " + str(inventory))
    item_list = list(inventory.keys())
    print("Item list: " + str(item_list))
    total = sum(inventory.values())
    print("Total quantity of the " + str(len(inventory)) + " items: " + str(total))
    for item, quantity in inventory:
        print("Item: " + item + " represents " + str(round(quantity / total * 100, 1)) + "%")
    most = inventory.keys(max(inventory.values()))
    least = inventory.keys(min(inventory.values()))
    print("Item most abundant: " + most)
    print("Item least abundant: " + least)
    inventory.update({"magic_item": 1})
    print("Updated inventory: " + str(inventory))