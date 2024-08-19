#!C:\Users\DELL\AppData\Local\Programs\Python\Python310\python
import cgi
import pymysql

print("Content-type:text/html")
print()

req=cgi.FieldStorage()
id=req.getvalue("uid")
#print(id)
con=pymysql.connect(host='bnlexxma2lfq3xh9a90s-mysql.services.clever-cloud.com',user='uxteh95x3dfl49xv',password='4cacwHSLS9DaE8q0ljsp',database='bnlexxma2lfq3xh9a90s')
curs=con.cursor()

curs.execute("select * from users where LoginID='%s'" %id)
data=curs.fetchone()

if data:
    print("<span style='color:red'>Sorry LoginID %s already taken</span>" %id)
else:
    print("<span style='color:green'>Congrats LoginID %s is available</span>" %id)

con.close()
