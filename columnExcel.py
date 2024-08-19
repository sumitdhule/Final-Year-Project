import pandas as pd
import json
import firebase_admin
from firebase_admin import credentials, db
import json
from pathlib import Path

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

# Step 2: Convert JSON to DataFrame
df = pd.DataFrame(data)
# Step 3: Write DataFrame to Excel
df_transposed = df.transpose()
df_transposed.to_excel('./xlsx_files/transposed_excel_file.xlsx', index=False)
#df.to_excel('./xlsx_files/Student.xlsx', index=False)

df=pd.read_excel('./xlsx_files/transposed_excel_file.xlsx')
single_column = df['Attendance Sheet']
print(single_column)
#split
#df1 = df[single_column].str.split(',',expand=True)
#df.to_excel('./xlsx_files/Modifiedtransposed_excel_file.xlsx', index=False)

#file_path = Path('./json_files/Student.json')

# Delete the file
#file_path.unlink()