import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('sofar_client.json', scope)

gc = gspread.authorize(credentials)
sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/ccc?key=1wQN_VbF_-LpkNy63cdD-m9Skv8IhG3Bj4zZ54Hlu7Og')
#sht1 = gc.open_by_key('1TnYumkVPc14XcmRgWKNgGWPj0qV64AG6sazbqdbXLlQ')
