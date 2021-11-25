from __future__ import print_function

from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
import os.path
import time
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Create your views here.
def index(request):

    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

    def main():
        """Shows basic usage of the Gmail API.
        Lists the user's Gmail labels.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'interns-service-acc-cloud-work.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('gmail', 'v1', credentials=creds)

        # Call the messages
        results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
        messages = results.get('messages', [])

        msgCount = int(input("How many messages do you want to see? "))
        if not messages:
            print('No labels found.')
        else:
            print('messages:')
            for message in messages[:msgCount]:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                print(msg['snippet'])
                print("\n")
                time.sleep(2)
                print(messages['name'])
        if __name__ == '__main__':
            main()
