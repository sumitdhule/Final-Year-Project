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
dt=req.getvalue("dt")
mt=req.getvalue("mt")
yr=req.getvalue("yr")


# Access the Database
ref = db.reference('Students')
data = ref.get()
print("<table class='table table-bordered table-hover'>")
print("<tr style='background-color:azure'>")
print("<th>First Name")  
print("<th>Last Name")
print("<th>Year")
print("<th>Hour") 
print("<th>Minute")
print("<th>Second")
print("</tr>")
for item in data:
    nm=data[item]["fname"]
    nm1=data[item]["lname"]
    rno=int(data[item]["Roll Number"])
    print("Roll NO : ",rno,"||")
    print("Student Name : ",nm)
    print("<br><hr>")
    at=data[item]["Attendance"]
    for val in at:
        if dt==val[2:4] and mt==val[:2]:
        #print(val[:2],"/",val[2:4],"/",val[4:8],"  Time : ",val[8:10],":",val[10:12],":",val[12:14],)
            print("<tr>")
            print("<td>%s" %nm)
            print("<td>%s" %nm1)
            print("<td>%s" %val[4:8])
            print("<td>%s" %val[8:10])
            print("<td>%s" %val[10:12])
            print("<td>%s" %val[12:14])
    #print("<td>%s" %rec[4])
            print("</tr>")

#con.close()
print("</table>")
print("</div>")