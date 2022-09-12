from kivymd.uix.screen import MDScreen
from datetime import datetime
from screens.classmenuscreen.classmenuscreen import ClassMenuScreen
from screens.schelduescreen.schelduescreen import ScheldueScreen

# Get the day ID || Day_id is the number of the day, starting from 0
day_id = datetime.now().weekday()

# Check if Saturday or Sunday
if day_id >= 5:
    day_id = 0

class rootscreen(MDScreen):
    
    def today(self):
        self.ids.swiper.set_current(day_id)