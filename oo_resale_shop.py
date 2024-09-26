from computer import Computer

class ResaleShop:

    from typing import Dict, Optional

    inventory: list
    itemID: int

    # Constructor for inventory
    def __init__(self):
        self.inventory = []

    # add a new computer to inventory
    def buy(self, computer: Computer):
        self.inventory.append(computer)

    # remove a computer from inventory
    def sell(self, computer : Computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
            print("Item", computer.description, "sold!")
        else: 
            print("Item", computer.description, "not found. Please select another item to sell.") 
            # print error message if not found
    
    # display all computers and their details in inventory
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            for computer in self.inventory:
                print(computer)
        else:
            print("No inventory to display.")

        
def main():

    inventory = ResaleShop()
    
    macpro = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    
    anotherMac = Computer(
        "Mac Pro (Late 2015)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Sonoma", 2015, 2000)

    inventory.buy(macpro)
    inventory.print_inventory()

    inventory.buy(anotherMac)
    inventory.print_inventory()

    macpro.update_price(1000)
    inventory.print_inventory()

    anotherMac.refurbish()
    inventory.print_inventory()

    inventory.sell(macpro)
    inventory.print_inventory()

main()