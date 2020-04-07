import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('data.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
sheet = client.open("deep").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()

info = sheet.get_all_values()

c=len(info)+1
rows=[]

with open('k1.csv', 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        rows.append(row)

for i in rows:
	sheet.update_cell(c, 1, i)
	c = c+1

