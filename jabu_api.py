
from google.oauth2 import service_account
from googleapiclient.discovery import build
import api_call

SERVICE_ACCOUNT_FILE = "jabu_service_account.json"
credentials = service_account.Credentials.from_service_account_file(
    filename=SERVICE_ACCOUNT_FILE
)

service_sheets = build("sheets","v4", credentials=credentials)

GOOGLE_SHEETS_ID = "1LORq6auWGdhEyLV7Qas94g__lyLm2Xf0ybMedM13bPE"

worksheet_name = "Sheet1!"
cell_range_insert = "A:A"
#values = [['A New Hope'], ['The Empire Strikes Back'], ['Return of the Jedi'], ['The Phantom Menace'], ['Attack of the Clones'], ['Revenge of the Sith']]
values = api_call.api_movies()
value_range_body = {
    "majorDimension":"ROWS", 
    "values":values
}


service_sheets.spreadsheets().values().append(
    spreadsheetId=GOOGLE_SHEETS_ID, 
    valueInputOption="USER_ENTERED", 
    range=worksheet_name + cell_range_insert, 
    body=value_range_body
).execute()

