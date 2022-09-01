from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from datetime import datetime
from schedule_api import schedule

# Get the day ID || Day_id is the number of the day, starting from 0
day_id = datetime.now().weekday()

# Check if Saturday or Sunday
if day_id >= 5:
    day_id = 0


class Container(BoxLayout):

    # Create ObjectProperty link
    label_link = ObjectProperty()
    link_label_day = ObjectProperty()

    # Function when "Update" button is pressed
    def update(self):
        schedule.update()
        
        # Get the day ID 
        global day_id
        day_id = datetime.now().weekday()
        # Check if Saturday or Sunday
        if day_id >= 5:
            day_id = 0
        
        self.link_label_day.text = str(schedule.get_day_scheldue(day_id)[1]) # Set the date label

        # Checking for errors
        if schedule.get_day_scheldue(day_id) == None:
            self.label_link.text = str('Vajuta "Tänane tunniplaan" nuppu.')
        else:
            self.label_link.text = str(schedule.get_day_scheldue(day_id)[0]) # Set the scheldue label

    def day_math(self,num):
        
        # Change day value. 
        global day_id

        # Value limit
        if day_id >= 4 and num == 1:
            day_id = 0
        elif day_id == 0 and num == -1:
            day_id = 4
        else:
            day_id += num
        

        self.link_label_day.text = str(schedule.get_day_scheldue(day_id)[1]) # Set the date label
        self.label_link.text = str(schedule.get_day_scheldue(day_id)[0]) # Set the scheldue label



class TunniplaanApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    TunniplaanApp().run()