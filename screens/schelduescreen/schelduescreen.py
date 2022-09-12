from turtle import update
from kivymd.uix.screen import MDScreen
from schedule_api import schedule
from datetime import datetime
import configparser
from kivymd.uix.screenmanager import MDScreenManager
config = configparser.ConfigParser()

# Get the day ID || Day_id is the number of the day, starting from 0
day_id = datetime.now().weekday()

# Check if Saturday or Sunday
if day_id >= 5:
    day_id = 0

Class_Name = [
 '1. klass',
 '2. klass',
 '3.a klass',
 '3.b klass',
 '3.v klass',
 '4. klass',
 '5.a klass',
 '5.b klass',
 '6. klass',
 '7. klass',
 '7.v klass',
 '8. klass',
 '9. klass',
 '9.v klass',
 '10.a klass',
 '10.b klass',
 '11. klass',
 '12.a klass',
 '12.b klass',
]

class ScheldueScreen(MDScreen):
    print('schelduescreen loaded')
    # Function when "Update" button is pressed
    def update(self):
        schedule.update()

        # Get the day ID 
        global day_id
        day_id = datetime.now().weekday()
        # Check if Saturday or Sunday
        if day_id >= 5:
            day_id = 0
        config.read('config.ini')

        # Set the class label
        self.ids.Class_Label_1.text = str(Class_Name[int(config['SETTINGS']['class_id'])])
        self.ids.Class_Label_2.text = str(Class_Name[int(config['SETTINGS']['class_id'])])
        self.ids.Class_Label_3.text = str(Class_Name[int(config['SETTINGS']['class_id'])])
        self.ids.Class_Label_4.text = str(Class_Name[int(config['SETTINGS']['class_id'])])
        self.ids.Class_Label_5.text = str(Class_Name[int(config['SETTINGS']['class_id'])])

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
    