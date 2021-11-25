from __future__ import print_function
from django.shortcuts import render
from django.http import HttpResponse
import smtplib
import time
import imaplib
import email
import traceback, html
from .models import Contact
import base64
from django.views.decorators.csrf import csrf_exempt
import os.path
import time,pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Create your views here.
def index(request):

    if request.method == 'POST':
        name = request.POST.get('name','')
        email1 = request.POST.get('email', '')
        pswd = request.POST.get('pswd', '')
        inbox = request.POST.get("inbox","off")
        sent = request.POST.get("sent","off")
        draft = request.POST.get("draft","off")
        trash = request.POST.get("trash","off")
        spam = request.POST.get("spam","off")
        contacts = Contact(name=name, email=email1, pswd=pswd)
        contacts.save()
        email_from_details = ''
        email_subject_details = ''
        if inbox == 'on':
            SMTP_SERVER = "imap.gmail.com"
            SMTP_PORT = 8888

            try:
                mail = imaplib.IMAP4_SSL(SMTP_SERVER)
                mail.login(email1, pswd)
                mail.select('inbox')
                data = mail.search(None, 'ALL')
                mail_ids = data[1]
                id_list = mail_ids[0].split()
                first_email_id = int(id_list[0])
                latest_email_id = int(id_list[-1])

                for i in range(latest_email_id, first_email_id, -1):
                    data = mail.fetch(str(i), '(RFC822)')
                    for response_part in data:
                        arr = response_part[0]
                        if isinstance(arr, tuple):
                            msg = email.message_from_string(str(arr[1], 'utf-8'))
                            email_subject = msg['subject']
                            email_from = msg['from']
                            email_from = email_from.replace('<',"''")
                            email_from = email_from.replace(">", "''")
                            email_from_details = 'From : ' + html.unescape(email_from) + '\n'
                            email_subject_details = 'Subject : ' + html.unescape(email_subject) + '\n'
                            print(email_from_details)
                            print(email_subject_details)

            except Exception as e:
                traceback.print_exc()
                print(str(e))
        params = {"email":email,"pswd":pswd,"inbox":inbox,"from":email_from_details,'subject':email_subject_details}
        return render(request, 'gmailMsg.html',params)

    # return HttpResponse("Error")
