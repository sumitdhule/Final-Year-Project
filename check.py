#!C:\Users\DELL\AppData\Local\Programs\Python\Python310\python
import cgi
import pymysql

print("Content-type:text/html")
print()

req=cgi.FieldStorage()
id=req.getvalue("uid")
pas=req.getvalue("psw")

#print(id+ pas)
con=pymysql.connect(host='bnlexxma2lfq3xh9a90s-mysql.services.clever-cloud.com',user='uxteh95x3dfl49xv',password='4cacwHSLS9DaE8q0ljsp',database='bnlexxma2lfq3xh9a90s')
curs=con.cursor()

#curs.execute("select * from Authority where LoginID='%s'"%id)
curs.execute("select * from Authority where LoginID='%s' and pasword='%s'"%(id,pas))
data=curs.fetchone()
#print(data)
if data:
    #print("Welcome '%s' At Administrative Page "%id)
    print("<html>")
    print('<head>')
    print("<meta http-equiv='refresh' content='0;url=Admin.html'>")
    print('</head>')
    print("</html>")
else:
    #print("soory '%s' you Are not authenticate user" %id)
    print('<html>')
    print('<head>')
    print("<meta http-equiv='refresh' content='0;url=Error.html'>")
    print('</head>')
    print('</html>')
con.close()