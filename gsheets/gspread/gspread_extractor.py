from gspread_connector import gspreadConnector

gs = gspreadConnector(
    '1TnYumkVPc14XcmRgWKNgGWPj0qV64AG6sazbqdbXLlQ',
    'Cities')

print(gs.get_headers())
print(gs.get_rows())

gs = gspreadConnector(
    '1wQN_VbF_-LpkNy63cdD-m9Skv8IhG3Bj4zZ54Hlu7Og',
    'Daily Spend1')

print(gs.get_headers())
print(gs.get_rows())
