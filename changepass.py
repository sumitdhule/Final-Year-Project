#!C:\Users\DELL\AppData\Local\Programs\Python\Python310\python
import cgi
import pymysql

print("Content-type:text/html")
print()

req=cgi.FieldStorage()
id=req.getvalue("uid")
cur=req.getvalue("cur")
nwp=req.getvalue("nwp")
cpp=req.getvalue("cpp")

con=pymysql.connect(host='bnlexxma2lfq3xh9a90s-mysql.services.clever-cloud.com',user='uxteh95x3dfl49xv',password='4cacwHSLS9DaE8q0ljsp',database='bnlexxma2lfq3xh9a90s')
curs=con.cursor()

if nwp==cpp:
    curs.execute("select * from Authority where LoginID='%s' and pasword='%s'" %(id,cur))
    data=curs.fetchone()
    if data:
        curs.execute("update users set pasword='%s' where LoginID='%s'" %(nwp,id))
        con.commit()
        print("Password Changed Successfully..")
    else:
        print("Sorry password Cant Changed..")
else:
    print("New password Mismatched..")

print("<br> <br>")
print("<a href=change.html>Refresh..</a>")