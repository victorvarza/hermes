from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

cred_path = "app/conf/gdrive_cred.json"
gauth = GoogleAuth()
gauth.LoadCredentialsFile(cred_path)

if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

print("Writing credentials to {0}".format(cred_path))
gauth.SaveCredentialsFile(cred_path)
drive = GoogleDrive(gauth)