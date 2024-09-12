from computer import Computer

class ResaleShop:

    # What attributes will it need?
    from typing import Dict, Optional

    inventory: Dict[int, Computer]
    itemID: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = {}
        self.itemID = 0

    # What methods will you need?
    def buy(self, computer: Computer):
        self.itemID += 1
        self.inventory[self.itemID] = computer
        print("Item", self.itemID, "stocked!") 
    
    def sell(self, itemID : int):
        if itemID in self.inventory:
            del self.inventory[itemID]
            print("Item", itemID, "sold!")
        else: 
            print("Item", itemID, "not found. Please select another item to sell.")
    
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for itemID in self.inventory:
                # Print its details
                print("Item ID:", itemID, ":", self.inventory[itemID].attributes())
        else:
            print("No inventory to display.")

    def update_price(self, itemID: int, new_price: int):
        if itemID in self.inventory:
            self.inventory[itemID].price = new_price
        else:
            print("Item", itemID, "not found. Cannot update price.")
        
def main():

    inventory = ResaleShop()
    
    # First, let's make a computer
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)

    inventory.buy(computer)
    inventory.print_inventory()
    inventory.update_price(1, 500)
    inventory.print_inventory()
    inventory.sell(1)
    inventory.print_inventory()

main()