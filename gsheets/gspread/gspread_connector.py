import gspread
from oauth2client.service_account import ServiceAccountCredentials

class gspreadConnector:

    def __init__(self,sheetID,sheetName):
        self.sheetID = sheetID
        self.sheetName = sheetName

        self.gspreadConn()

    def gspreadConn(self):
        scope = ['https://spreadsheets.google.com/feeds']

        credentials = ServiceAccountCredentials.from_json_keyfile_name('sofar_client.json', scope)
        gc = gspread.authorize(credentials)

        sh = gc.open_by_key(self.sheetID)

        try:
            worksheet = sh.worksheet(self.sheetName)
        except:
            print('Sheet: {0} not found'.format(self.sheetName))
            self.results = None
            return None

        self.results = worksheet.get_all_values()
        if self.results == None:
            print('No results found')

    def get_rows(self):
        if self.results == None: return None
        self.values = self.results[1:]
        return self.values

    def get_headers(self):
        if self.results == None: return None
        self.cols = self.results[0]
        return self.cols

""" TO DO
if __name__ == '__main__':
    self.sheetID = sys.argv[1]
    self.sheetName = sys.argv[2]
"""
