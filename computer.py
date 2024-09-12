class Computer:
    
    from typing import Optional

    # computer attributes
    description: str 
    processor_type: str 
    hard_drive_capacity: int 
    memory: int 
    operating_system: str 
    year_made: int 
    price: int 

    # Contructor
    def __init__(self, description: str, 
                 processor_type: str, 
                 hard_drive_capacity: int, 
                 memory: int, 
                 operating_system: str, 
                 year_made: int, 
                 price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # update price of computer
    def update_price(self, new_price: int):
        self.price = new_price

    # update OS and/or price depending on the year made
    def refurbish(self, new_os: Optional[str] = None):
            if int(self.year_made) < 2000:
                self.price = 0 # too old to sell, donation only
            elif int(self.year_made) < 2012:
                self.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(self.year_made) < 2018:
                self.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                self.price = 1000 # recent stuff

            if new_os is not None:
                self.operating_system = new_os # update details after installing new OS

    # returns all details on computer
    def attributes(self):
        return vars(self)
