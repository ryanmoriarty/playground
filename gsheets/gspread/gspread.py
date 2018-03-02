import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('sofar_client.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("Where is the money Lebowski?").sheet1
