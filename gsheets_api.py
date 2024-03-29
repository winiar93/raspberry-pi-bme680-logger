from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import psutil
from google.oauth2 import service_account
#,data2,data3,data4
def push_to_google_sheets(data1,data2,data3,data4,data5,data6):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'keys.json'

    credentials = None
    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1mVQZs7y0SodDIHx89V-_bdP2RAwBICmPl-fXiZVs42k'
    SAMPLE_RANGE_NAME = 'Class Data!A2:F'

    service = build('sheets', 'v4', credentials=credentials)

    # Call the Sheets API
    sheet = service.spreadsheets()

    my_data_list = [[data1,data2,data3,data4,data5,data6]]
    request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                     range="Arkusz1!A2",
                                                     valueInputOption='USER_ENTERED',
                                                     body={"values": my_data_list}).execute()

    return(request)

