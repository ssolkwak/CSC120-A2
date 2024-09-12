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

    def update_price(self, itemID: int, new_price: int):
        if itemID in self.inventory:
            self.inventory[itemID]["price"] = new_price
        else:
            print("Item", itemID, "not found. Cannot update price.")
    
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for itemID in self.inventory:
                # Print its details
                print(f'Item ID: {itemID} : {self.inventory[itemID]}')
        else:
            print("No inventory to display.")

    def refurbish(self, itemID: int, new_os: Optional[str] = None):
        if itemID in self.inventory:
            computer = self.inventory[itemID] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", itemID, "not found. Please select another item to refurbish.")
        
def main():
    inv = ResaleShop()
    myComputer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)

    inv.buy(myComputer)
    inv.print_inventory()
    inv.refurbish(3)
    inv.sell(1)
main()