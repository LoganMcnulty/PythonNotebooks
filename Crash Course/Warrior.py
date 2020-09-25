def make_warrior(userName, warClass, **armor):
    warrior = {}
    inventory = {}
    warrior['Username'] = userName
    warrior['Class'] = warClass
    
    for slot, item in armor.items():
        inventory[slot] = item
    
    warrior['Inventory'] = inventory
    print("Welcome " + warrior['Username'] + "\nYour " + warClass + " is armed with...")
    
    for slot, item in warrior['Inventory'].items():
        print(" - " + item)
    
    print("\n")
    
    return warrior