import os.path
import os
from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive"]

def create_folder(service, parent_id):
    """Create a folder with the current date as its name."""
    current_date = datetime.now().strftime("%d-%A-%Y %H:%M:%S")
    folder_metadata = {
        "name": current_date,
        "parents": [parent_id],
        "mimeType": "application/vnd.google-apps.folder"
    }
    folder = service.files().create(body=folder_metadata, fields="id").execute()
    return folder.get("id")

def main():
    """Upload files to a directory named by the current date on Google Drive."""
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("drive", "v3", credentials=creds)

        response = service.files().list(q="name='BackupHelios' and mimeType='application/vnd.google-apps.folder'", spaces='drive').execute()
        if not response['files']:
            parent_folder_id = create_folder(service, None)
        else:
            parent_folder_id = response['files'][0]['id']

        current_date_folder_id = create_folder(service, parent_folder_id)

        for file in os.listdir("Helios-Backup-Client"):
            file_metadata = {
                "name": file,
                "parents": [current_date_folder_id]
            }
            media = MediaFileUpload(f"Helios-Backup-Client/{file}")
            upload_file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()
            print("Backed Up File: ", file)

    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
