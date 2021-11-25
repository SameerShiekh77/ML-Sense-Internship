# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
#
# """Shows basic usage of the Gmail API.
# Lists the user's Gmail labels.
# """
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
            'E:\Internship\ML Sense Intern\Day 3\gmailAPI\client_secret_59866668171-l8shdphn53spjqg5s3gj7n6mrgahdbc6.apps.googleusercontent.com.json',
            SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('gmail', 'v1', credentials=creds)

# # Call the Gmail API
# # results = service.users().labels().list(userId='me').execute()
# # labels = results.get('labels', [])
#
# # if not labels:
# #     print('No labels found.')
# # else:
# #     print('Labels:')
# #     for label in labels:
# #         print(label['name'])
#
# # Call the messages
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