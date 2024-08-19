#!C:\Users\DELL\AppData\Local\Programs\Python\Python310\python
import cgi
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

print("Content-type:text/html")
print()
print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<div class='container'><br>")


# Initialize Firebase app with credentials
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionbasedatte-b4a54-default-rtdb.firebaseio.com/"
})

req=cgi.FieldStorage()
day=req.getvalue("dt")
month=req.getvalue("mt")
yr=req.getvalue("yr")


# Create reference to the 'Students' node in the realtime database
ref = db.reference('Students')


# Fetching All keys of Students
AllStudentsIDs = ref.get().keys()

print("<table class='table table-bordered table-hover'>")
print("<tr style='background-color:azure'>")
print("<th>Student Name")  
print("<th>Last Name")
print("<th>Year")
print("<th>Hour") 
print("<th>Minute")
print("<th>Second")
print("</tr>")

# Iterate over each student
for student_id in AllStudentsIDs:
    print(f"Student ID: {student_id}")
    rollNo = student_id["Roll Number"]
    StdName = str(student_id["fname"],student_id["lname"])
    
    print("<br><hr>")

    # Fetch Attendance Sheet for the student
    attendance_sheet_ref = ref.child(student_id).child("Attendance Sheet").get()

    # If Attendance Sheet is present
    if attendance_sheet_ref:
        # Iterate over each date in the Attendance Sheet
        for date, attendance_data in attendance_sheet_ref.items():
            print(f"Date: {date}")
            if day == date[2:4] and month == date[:2]:
                # print("date matched!")
            # Iterate over each lecture in the date
                for lecture, status in attendance_data.items():
                    # print(f"Lecture: {lecture}, Status: {status}")
                    
                    print("<tr>")
                    print("<td>%s" %StdName)
                    print("<td>%s" %val[4:8])
                    print("<td>%s" %val[8:10])
                    print("<td>%s" %val[10:12])
                    print("<td>%s" %val[12:14])
                    print("</tr>")

        
            else:
                print(f'No Data Found for Date {day} {month}')
    else:
        print("No Attendance Sheet found for this student")

print("</table>")
print("</div>")