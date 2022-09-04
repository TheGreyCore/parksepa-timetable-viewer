from kivymd.uix.screen import MDScreen
from schedule_api import schedule
from datetime import datetime
from kivymd.app import MDApp

# Get the day ID || Day_id is the number of the day, starting from 0
day_id = datetime.now().weekday()

# Check if Saturday or Sunday
if day_id >= 5:
    day_id = 0
class rootscreen(MDScreen):

    def today(self):
        self.ids.swiper.set_current(day_id)

    # Function when "Update" button is pressed
    def update(self):
        schedule.update()

        # Get the day ID 
        global day_id
        day_id = datetime.now().weekday()
        # Check if Saturday or Sunday
        if day_id >= 5:
            day_id = 0

        self.ids.Day_Label_1.text = str(schedule.get_day_scheldue(0)[1]) # Set the date label
        self.ids.Scheldue_Label_1.text = str(schedule.get_day_scheldue(0)[0]) # Set the Scheldue label

        self.ids.Day_Label_2.text = str(schedule.get_day_scheldue(1)[1]) # Set the date label
        self.ids.Scheldue_Label_2.text = str(schedule.get_day_scheldue(1)[0]) # Set the Scheldue label

        self.ids.Day_Label_3.text = str(schedule.get_day_scheldue(2)[1]) # Set the date label
        self.ids.Scheldue_Label_3.text = str(schedule.get_day_scheldue(2)[0]) # Set the Scheldue label

        self.ids.Day_Label_4.text = str(schedule.get_day_scheldue(3)[1]) # Set the date label
        self.ids.Scheldue_Label_4.text = str(schedule.get_day_scheldue(3)[0]) # Set the Scheldue label

        self.ids.Day_Label_5.text = str(schedule.get_day_scheldue(4)[1]) # Set the date label
        self.ids.Scheldue_Label_5.text = str(schedule.get_day_scheldue(4)[0]) # Set the Scheldue label
    

