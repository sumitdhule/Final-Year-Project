#!C:\Users\DELL\AppData\Local\Programs\Python\Python310\python
import cgi
import firebase_admin
from firebase_admin import credentials, db
print("Content-type:text/html")
print()
print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<div class='container'><br>")

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionbasedatte-b4a54-default-rtdb.firebaseio.com/"
})

req=cgi.FieldStorage()
bno=int(req.getvalue("bno"))
pr='P'
ab='A'
#bno=int(input("Enter roll number "))
print("<br><center><b>Student Information</b></center>")

print("<table class='table table-bordered table-hover'>")
print("<tr style='background-color:azure'>")
print("</tr>")
print("<table class='table table-bordered table-hover'>")
print("<tr style='background-color:azure'>")
print("<th>Month")  
print("<th>Date")
print("<th>Year")
print("<th>1st Lecture") 
print("<th>2nd Lecture")
print("<th>3rd Lecture")
print("</tr>")

# Access the Database
ref = db.reference('Students')
data = ref.get()
for item in data:
    nm=data[item]["fname"]
    rno=int(data[item]["Roll Number"])
    sec=data[item]["Section"]
    yr=int(data[item]["year"])
    dept=data[item]["Department"]
    if rno==bno:
        print("Roll NO : ",rno)
        print("<hr>")
        print("Student Name : ",nm)
        print("<hr>")
        print("Section : ",sec)
        print("<hr>")
        print("Year of Admission : ",yr)
        print("<hr>")
        print("Department : ",dept)
        print("<br><hr>")
    
print("</table>")
print("<b>Student Excellence Report</b>")
print("<br><hr>")
print("<b>Students Extra Curricular Activities</b>")
print("<br><hr>")
print("<b>Student Certifications/Internships</b>")
print("<br><hr>")
print("</div>")

           