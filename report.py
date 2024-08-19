#!C:\Users\DELL\AppData\Local\Programs\Python\Python310\python
#import cgi
#import pymysql
import firebase_admin
from firebase_admin import credentials, db

print("Content-type:text/html")
print()
print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<div class='container'><br>")
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionbasedatte-b4a54-default-rtdb.firebaseio.com/"
})

# Access the Database
ref = db.reference('Students')

data = ref.get()
#print(data)
print("<table class='table table-bordered table-hover'>")
print("<tr style='background-color:azure'>")
print("<th>YearOFAdmission")  
print("<th>StudentName")
print("<th>Department")
print("<th>Roll No")
print("<th>Section") 
#print("<th>gender")
print("</tr>")
for item in data:
    #print(item,":")
    #print(data[item],"\n")
    fnm=data[item]["fname"]
    lnm=data[item]["lname"]
    nm=fnm+"  "+lnm
    rno=int(data[item]["Roll Number"])
    yr=int(data[item]["year"])
    dept=data[item]["Department"]
    sec=data[item]["Section"]
    print("<tr>")
    print("<td>%d" %yr)
    print("<td>%s" %nm)
    print("<td>%s" %dept)
    print("<td>%d" %rno)
    print("<td>%s" %sec)
    #print("<td>%s" %rec[4])
    print("</tr>")

#con.close()
print("</table>")
print("</div>")