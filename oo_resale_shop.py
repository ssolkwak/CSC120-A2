class ResaleShop:

    # What attributes will it need?
    from typing import Dict, Optional
    import computer 

    inventory: Dict[int, Dict]
    itemID: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = {}
        self.itemID = 0

    # What methods will you need?
    def buy(self, computer: Dict):
        self.itemID += 1
        self.inventory[self.itemID] = computer
        return self.itemID
    
    def sell(self, itemID : int):
        if itemID in self.inventory:
            del self.inventory[itemID]
            print("Item", itemID, "sold!")
        else: 
            print("Item", itemID, "not found. Please select another item to sell.")


    
