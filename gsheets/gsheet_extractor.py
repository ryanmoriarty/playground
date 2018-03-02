from gsheet_connector import gSheetConnector as gs

def all():
    cities = gs(
        '1TnYumkVPc14XcmRgWKNgGWPj0qV64AG6sazbqdbXLlQ', #spreadsheetId
        'Cities!A2:H', #Values
        'Cities!A1:H1', #Labels
        'cities' #Fileout
    )
    cities.main()

    facebook = gs(
        '1wQN_VbF_-LpkNy63cdD-m9Skv8IhG3Bj4zZ54Hlu7Og',
        'Daily Spend!A2:C',
        'Daily Spend!A1:C1',
        'facebook_spend'
    )
    facebook.main()

if __name__ == "__main__":
    all()
