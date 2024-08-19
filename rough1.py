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
    if rno==bno:
        print("Roll NO : ",rno,"||")
        print("Student Name : ",nm)
        print("<br><hr>")
        at=data[item]["Attendance"]
        for val in at:
            print("<tr>")
            print("<td>%s" %val[:2])
            print("<td>%s" %val[2:4])
            print("<td>%s" %val[4:8])
            
            #print("<td>%s" %)
            #print("<td>%s" %)
    #print("<td>%s" %rec[4])
            
            #print(val[:2],"/",val[2:4],"/",val[4:8],"  Time : ",val[8:10],":",val[10:12],":",val[12:14],)
            if val[8:10]=='13':
                print("<td>%s" %pr)
                print("<td>%s" %pr)
                print("<td>%s" %pr)
            else:
                print("<td>%s" %ab)
                #print("p")
                #continue
            if val[8:10]=='16':
                print("<td>%s" %pr)
                print("<td>%s" %pr)
            #else:
                #print("<td>%s" %ab)
                #print("p")
                #continue
            if val[8:10]=='18':
                print("<td>%s" %pr)
            #else:
                #print("<td>%s" %ab)
                #print("p")
                #continue
            print("</tr>")
    
print("</table>")
print("</div>")

           