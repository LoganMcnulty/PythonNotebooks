class Settings():
    # a class to store all settings for alien invasion
    
    def __init__(self):
        """ initialize game settings"""
        # screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (52, 146, 235)
        self.ship_speed_factor = 1.5
        self.bull_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        
    def shipSpeed():
        print("Please enter the speed of your ship ('slow', 'med', 'fast')")
        while True:
            speedInput = input("Ship Speed: ")
            speedInput = speedInput.lower()
            if speedInput == 'slow':
                self.ship_speed_factor = 1
                break
            elif speedInput == 'med':
                self.ship_speed_factor = 1.5
                break
            elif speedInput == 'fast':
                self.ship_speed_factor = 2
                break
            else:
                print("Invalid entry, please enter 'slow', 'med', or 'fast'")
                

    