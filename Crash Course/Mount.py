class Mount():
    def __init__(self, animal, age, location):
        self.animal = animal
        self.age = age
        self.location = location
        self.miles = 0
        
    def get_description(self):
        long_description = "This mount is a " + self.animal.title() + ". \nIt is " + str(self.age) + " years old.\nOne can be purchased from the " + self.animal.title() + " breeder in " + self.location.title()
        return long_description
    
    def get_miles(self):
        milesTraveled = "This mount has traveled a total of " + str(self.miles) + " miles."
        return milesTraveled
    
    def update_miles(self, miles):
        if miles > self.miles:
            self.miles = miles
        else:
            print("You can't roll back the miles!")
            
    def add_miles(self, newMiles):
        if newMiles > 0:
            self.miles += newMiles
        else:
            print("you cannot deduct miles!")
