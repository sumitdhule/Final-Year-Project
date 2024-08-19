#!C:\Users\DELL\AppData\Local\Programs\Python\Python310\python
import cgi
import pymysql

print("Content-type:text/html")
print() 

print("<link rel='stylesheet' href='bootstrap.min.css'")
print("<div class='container'>")
req=cgi.FieldStorage()
bno=int(req.getvalue("bno"))

con=pymysql.connect(host='bnlexxma2lfq3xh9a90s-mysql.services.clever-cloud.com',user='uxteh95x3dfl49xv',password='4cacwHSLS9DaE8q0ljsp',database='bnlexxma2lfq3xh9a90s')
curs=con.cursor()

try:
    curs.execute("select * from Studantdata where rollno=%d" %bno)
    data=curs.fetchone()
    print("<h3>")
    print("Name : ",data[1],"::","Roll No. : ",data[3],"::")
    print("Year OF Admission : ",data[0],"::","Department : ",data[2])

    print("</h3>")
except Exception as e:
    #print(e)
    print(" Not Found...")

con.close()
print('<hr>') 

print("<br><a href='Admin.html'>Home..</a>")

print("</div>")