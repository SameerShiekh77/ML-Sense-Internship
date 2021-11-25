from django.shortcuts import render,HttpResponse
import bcrypt
from home.models import UserHashingPassword
from google.cloud import storage
import google.cloud.storage
import json
from google.cloud import storage
import os
import sys
# Create your views here.
def index(request):
    # passwd = b's$cret12'rom django.shortcuts import render,HttpResponse
    # import bcrypt
    # from home.models import UserHashingPassword
    # from google.cloud import storage
    # import google.cloud.storage
    # import json
    # from google.cloud import storage
    # import os
    # import sys

    if request.method == 'POST':
        name = request.POST.get('name')
        passwd = request.POST.get('pswd')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(b"{passwd}", salt)
        hashingPswd = UserHashingPassword(name=name,pswd=hashed)
        hashingPswd.save()
        PATH = os.path.join(os.getcwd(), 'interns-service-acc-cloud-work.json')
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = PATH
        storage_client = storage.Client(PATH)
        print(storage_client)
        bucket = storage_client.get_bucket('clouddjangoproject')
        filename = [filename.name for filename in list(bucket.list_blobs(prefix=''))]
        print(filename)
        filename = 'NewHashingPasword.txt'
        with open('NewHashingPasword.txt',"a") as f:
            f.write("Name: "+name +'Hashing Pasword: '+str(hashed)+"\n")
        UPLOADFILE = os.path.join(os.getcwd(), filename)
        bucket = storage_client.get_bucket('clouddjangoproject')
        blob = bucket.blob(filename)
        blob.upload_from_filename(UPLOADFILE)
        print("Original Password: ", passwd)
        print("Salt", salt)
        print("Hashed bcrypted:", hashed)

    return render(request,"index.html")