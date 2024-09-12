from computer import Computer

class ResaleShop:

    from typing import Dict, Optional

    inventory: Dict[int, Computer]
    itemID: int

    # Constructor for inventory
    def __init__(self):
        self.inventory = {}
        self.itemID = 0

    # add a new computer to inventory
    def buy(self, computer: Computer):
        self.itemID += 1
        self.inventory[self.itemID] = computer
        print("Item", self.itemID, "stocked!") 
    
    # remove a computer from inventory
    def sell(self, itemID : int):
        if itemID in self.inventory:
            del self.inventory[itemID]
            print("Item", itemID, "sold!")
        else: 
            print("Item", itemID, "not found. Please select another item to sell.") # print error message if not found
    
    # display all computers and their details in inventory
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for itemID in self.inventory:
                # Print its details
                print("Item ID:", itemID, ":", self.inventory[itemID].attributes())
        else:
            print("No inventory to display.")

    # update the price of a computer in inventory using item ID
    def update_price(self, itemID: int, new_price: int):
        if itemID in self.inventory:
            self.inventory[itemID].price = new_price
        else:
            print("Item", itemID, "not found. Cannot update price.")

    # update the OS and/or the price of a computer in inventory using item ID
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
        
def main():

    inventory = ResaleShop()
    
    macpro = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)

    inventory.buy(macpro)
    inventory.print_inventory()

    inventory.update_price(1, 500)
    inventory.print_inventory()

    inventory.refurbish(1)
    inventory.print_inventory()

    inventory.sell(1)
    inventory.print_inventory()

main()