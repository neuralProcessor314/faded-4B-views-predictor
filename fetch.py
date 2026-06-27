# Original version copyright 2018 Google LLC
# Original license:
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Modified by neuralProcessor314
# Copyright 2026 neuralProcessor314. GNU GPLv3.0

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import pandas as pd

# If modifying these scopes, delete the file do_not_push/token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# ID and Range
SAMPLE_SPREADSHEET_ID = "10oMAHaOk_tala3QCmmssSQb_c1B-DWhfEEvswbiJ6eo"
SAMPLE_RANGE_NAME = "A2:D"

save_dir = "data/raw_data.csv"

def main():
  creds = None
  # The file do_not_push/token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first time.
  print("Checking for credentials.")
  if os.path.exists("do_not_push/token.json"):
    creds = Credentials.from_authorized_user_file("do_not_push/token.json", SCOPES)

  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "do_not_push/credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("do_not_push/token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    print("Fetching.")
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )

    values = result.get("values", [])
    if not values:
      print("No data found.")
      return

    # print("D, H, M, views:")
    # for row in values:
    #   print(str(row[0]), str(row[1]), str(row[2]), str(row[3]))

    values = pd.DataFrame(values)
    values.to_csv(save_dir, index=False)
    print("Saved data at " + save_dir + '.')

  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()