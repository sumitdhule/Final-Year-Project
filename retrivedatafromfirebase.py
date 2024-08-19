#!C:\Users\DELL\AppData\Local\Programs\Python\Python310\python
#import cgi
import pymysql
import firebase_admin
from firebase_admin import credentials, db
#import jsontosql

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionbasedatte-b4a54-default-rtdb.firebaseio.com/"
})

# Access the Database
ref = db.reference('Students')

con = pymysql.connect(host='bnlexxma2lfq3xh9a90s-mysql.services.clever-cloud.com',user='uxteh95x3dfl49xv',password='4cacwHSLS9DaE8q0ljsp',database='bnlexxma2lfq3xh9a90s')
cursor = con.cursor()
 
# Retrieve Data
data = ref.get()
#jsontosql.CreateSQL(data)
for item in data:
    #print(item)
    nm=data[item]["name"]
    rno=int(data[item]["Roll Number"])
    yr=int(data[item]["year"])
    dept=data[item]["Department"]
    #print(rno)
    #print(yr)
    #print(dept)
    #print(nm)
    cursor.execute("insert into Studantdata values(%d,'%s','%s',%d);"%(yr,nm,dept,rno))
    con.commit()
'''print(data)
nm=data["name"]
print(nm)'''
