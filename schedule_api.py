import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import discovery
import configparser

config = configparser.ConfigParser()

# Scopes, I recommend not to change.
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET_ID = '15vSrId7Kiz__4qFvo9WvX_FdR4zKQBQHQON93oF7Mzo' # Take spreadsheet ID from config.ini file
RANGE_SCHEDULE =  [
'schedule!B:B',
'schedule!D:D',
'schedule!E:E',
'schedule!F:F',
'schedule!G:G',
'schedule!I:I',
'schedule!J:J',
'schedule!K:K',
'schedule!M:M',
'schedule!O:O',
'schedule!P:P',
'schedule!Q:Q',
'schedule!S:S',
'schedule!T:T',
'schedule!U:U',
'schedule!V:V',
'schedule!W:W',
'schedule!X:X',
'schedule!Y:Y',
]
RANGE_LESSONS_TIME =  'schedule!A1:A48' 

#  Function to get data from google sheets
def get_data(RANGE):
    try:
        creds = None
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
        
        data = []
        # Unpack and add new line
        i = 1
        for row in values:
            data.append("".join(row) + '\n')
        return data
    except:
        os.remove('token.json')
        get_data(RANGE)

class schedule():

    # Function to get/update data
    def update():
        config.read('config.ini')
        global week_schedule
        week_schedule = get_data(RANGE_SCHEDULE[int(config['SETTINGS']['class_id'])])
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
            r = week_lessons_time[0].replace("\n","")
            return "".join(week_schedule[1:8]), r.replace(",","\n")
        if day_id == 1: # Teisipäev
            r = week_lessons_time[9].replace("\n","")
            return "".join(week_schedule[10:18]), r.replace(",","\n")
        if day_id == 2: # Kolmapäev
            r = week_lessons_time[19].replace("\n","")
            return "".join(week_schedule[20:27]), r.replace(",","\n")
        if day_id == 3: # Neljapäev
            r = week_lessons_time[28].replace("\n","")
            return "".join(week_schedule[29:36]), r.replace(",","\n")
        if day_id == 4: # Reede
            r = week_lessons_time[37].replace("\n","")
            return "".join(week_schedule[38:45]), r.replace(",","\n")