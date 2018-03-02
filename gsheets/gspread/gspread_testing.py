import pandas as pu
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('sofar_client.json', scope)
gc = gspread.authorize(credentials)
sh = gc.open_by_key('1TnYumkVPc14XcmRgWKNgGWPj0qV64AG6sazbqdbXLlQ')

worksheet = sh.worksheet("Cities")
results = worksheet.get_all_values()

cols = results[0]
values = results[1:]

df = pu.DataFrame.from_records(values,columns=cols)
print(df.shape)
print(df.head)
