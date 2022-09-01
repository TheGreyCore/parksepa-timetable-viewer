from __future__ import print_function
import os.path
from datetime import datetime
from turtle import update
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient import discovery
import configparser

# Config file read
config = configparser.ConfigParser()
config.read ('config.ini')

# Scopes, I recommend not to change.
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Temporary variables
class_id = 'B'
RANGE_SCHEDULE =  '11.b!B1:B48' 
RANGE_LESSONS_TIME =  '11.b!A1:A48' 

#  Function to get data from google sheets
def get_data(RANGE):
    
    SPREADSHEET_ID = config['SETTINGS']['SPREADSHEET_ID'] # Take spreadsheet ID from config.ini file

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = discovery.build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID, range=RANGE).execute()
    values = result.get('values', [])

    # If above code returns nothing
    if not values:
        print('[ERROR] No data found.')
        pass
    
    # Unpack and add new line
    data = []
    for row in values:
            data.append("".join(row) + '\n')

    return data

class schedule():

    # Function to get/update data
    def update():
        global week_schedule
        week_schedule = get_data(RANGE_SCHEDULE)
        global week_lessons_time
        week_lessons_time = get_data(RANGE_LESSONS_TIME)
    
    # Function to get day scheldue | Day_id is the number of the day, starting from 0
    def get_day_scheldue(day_id):
        
        # Testing is week_schedule definited
        try: 
            "".join(week_schedule[0])
        except: 
            schedule.update()

        # Returning the scheldue || the day + the date
        if day_id >= 5 or day_id == 0: #Pühapäev - Esmaspäev
            return "".join(week_schedule[1:8]), week_lessons_time[0].replace(",","\n")
        if day_id == 1: # Teisipäev
            return "".join(week_schedule[10:18]), week_lessons_time[9].replace(",","\n")
        if day_id == 2: # Kolmapäev
            return "".join(week_schedule[20:27]), week_lessons_time[19].replace(",","\n")
        if day_id == 3: # Neljapäev
            return "".join(week_schedule[29:36]), week_lessons_time[28].replace(",","\n")
        if day_id == 4: # Reede
            return "".join(week_schedule[38:45]), week_lessons_time[37].replace(",","\n")
    