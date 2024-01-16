import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pydrive.auth import GoogleAuth

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]

creds = "credentials_3.json.json"

def connect_gdrive(creds):
    gauth = GoogleAuth()
    scope = ['https://www.googleapis.com/auth/drive']
    gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(creds, scope)
    drive_prep = GoogleDrive(gauth)
    return drive_prep

# connect_gdrive(creds)

from google.oauth2 import service_account


scope = ['https://www.googleapis.com/auth/drive']
credentials = service_account.Credentials.from_service_account_file(
                              filename=creds, 
                              scopes=scope)
service = build('drive', 'v3', credentials=credentials)


# items = results.get("files", [])
# if not items:
#   print("No files found.")
# print("Files:")
# for item in items:
#   print(f"{item['name']} ({item['id']})")


def delete_file_gdrive(url='181R-ug68jYWaI9vBttHnHbt7cTQbuZ1s'):
    file_list = service.ListFile({'q': "'{0}' in parents and trashed=false".format(url)}).GetList()
    type(file_list)
    return file_list

print(delete_file_gdrive())