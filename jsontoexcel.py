#!C:\Users\DELL\AppData\Local\Programs\Python\Python310\python
#import cgi
import pandas as pd
import json
import firebase_admin
from firebase_admin import credentials, db
import json

print("Content-type:text/html")
print()
#print("sdfdsfds")

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionbasedatte-b4a54-default-rtdb.firebaseio.com/"
})

# Access the Database
ref = db.reference('Students')

data = ref.get()

file=open('./json_files/Student.json','a')
json.dump(data,file)
file.close()
#print('data stored in json file...')

# Step 1: Read JSON data
with open('./json_files/Student.json') as f:
    data = json.load(f)
htmlstr=""
# Step 2: Convert JSON to DataFrame
df = pd.DataFrame(data)
df_transposed = df.transpose()
html_data = df_transposed.to_html()
htmlstr=htmlstr+" "+html_data
print(html_data)
# Step 3: Write DataFrame to Excel
#df_transposed = df.transpose()
#df_transposed.to_excel('./xlsx_files/transposed_excel_file.xlsx', index=False)
#df.to_excel('./xlsx_files/Student.xlsx', index=False)


print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<p>Attendence Done <br>You can download</p>")
print("<a href='./xlsx_files/transposed_excel_file.xlsx'><b>Get Attendence</b></a>")
print("</div>")