from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import sys

import pandas as pd
import datetime

class gSheetConnector:
    """
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None
    """

    # If modifying these scopes, delete your previously saved credentials
    # at ~/.credentials/sheets.googleapis.com-python-quickstart.json
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPLICATION_NAME = 'Google Sheets API Python Quickstart'


    def __init__(self,spreadsheetId,rangeName,labelsName,fileout):
        self.spreadsheetId = spreadsheetId
        self.rangeName = rangeName
        self.labelsName = labelsName
        self.fileout = fileout


    def get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'sheets.googleapis.com-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

    def main(self):
        """Shows basic usage of the Sheets API.

        Creates a Sheets API service object and prints the names and majors of
        students in a sample spreadsheet:
        https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit

        spreadsheetId = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
        rangeName = 'Cities!A2:E'

        """
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                        'version=v4')
        service = discovery.build('sheets', 'v4', http=http,
                                  discoveryServiceUrl=discoveryUrl)


        # RM added
        # Get the values from the spreadsheet...
        result = service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheetId, range=self.rangeName).execute()
        values = result.get('values', [])

        # RM added
        # Get the columns
        result = service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheetId, range=self.labelsName).execute()
        labels = result.get('values', [])

        # Write results
        if not values:
            print('No data found.')
        else:

            # Create CSV of returned values using Pandas...
            print('Writing {0} to CSV'.format(self.spreadsheetId))
            df = pd.DataFrame.from_records(values,columns=labels[:1])

            # Add extract time...
            extractTime = datetime.datetime.now()
            df['ExtractTime'] = extractTime.strftime("%Y-%m-%d %H:%M")

            # Construct filename and write to CSV...
            filename = self.fileout + '_' + extractTime.strftime("%Y-%m-%d") + '.csv'
            df.to_csv(filename,encoding='UTF8',index=None)
            print('File: {0} created'.format(filename))


if __name__ == '__main__':
    spreadsheetId = sys.argv[1]
    rangeName = sys.argv[2]
    labelsName = sys.argv[3]
    fileout = sys.argv[4]

    main(self,spreadsheetId,rangeName,labelsName,fileout)
