from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime, timedelta
import os
from logs import Logs


class MyGoogleDrive():

    def __init__(self, cred_path):

        gauth = GoogleAuth()
        # Try to load client credentials
        gauth.LoadCredentialsFile(cred_path)

        if gauth.credentials is None:
            # Authenticate if they're not there
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            # Refresh them if expired
            gauth.Refresh()
        else:
            # Initialize the saved creds
            gauth.Authorize()
            # Save the current credentials to a file
            gauth.SaveCredentialsFile(cred_path)

        self.drive = GoogleDrive(gauth)
        
    def push(self, file_path, folder_id):
        try:
            filename = os.path.basename(file_path)
            Logs.Print('Uploading file: ' + str(filename) + " on gdrive folder: " + str(folder_id))
            textfile = self.drive.CreateFile({'title':filename, 'mimeType':'image/jpg',"parents": [{"kind": "drive#fileLink","id": folder_id}]})
            textfile.SetContentFile(file_path)
            textfile.Upload()
        except Exception as e:
            Logs.Print("Exception: " + str(e))

    def cleanup(self, days, gdrive_folder_ids):
        try:
            date_N_days_ago = datetime.now() - timedelta(days=days)
            files = self.drive.ListFile({"q": "trashed = false and modifiedDate < '" + str(date_N_days_ago).split(' ')[0] +"'", "maxResults": 1000}).GetList()
            for file in files:
                if file['id'] not in gdrive_folder_ids:
                    Logs.Print(file['title'] + " will be deleted")
                    file.Delete()
        except Exception as e:
            Logs.Print("Exception: " + str(e))