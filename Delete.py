#!C:\Users\DELL\AppData\Local\Programs\Python\Python310\python
import cgi
import pymysql

print("Content-type:text/html")
print()

req=cgi.FieldStorage()
tan=int(req.getvalue("bno"))

con=pymysql.connect(host='bnlexxma2lfq3xh9a90s-mysql.services.clever-cloud.com',user='uxteh95x3dfl49xv',password='4cacwHSLS9DaE8q0ljsp',database='bnlexxma2lfq3xh9a90s')
curs=con.cursor()

data=curs.execute("select * from Studentdata where StudentID=%d"%tan)
#print(data)
if data:
    try:
        curs.execute("delete from StudentData where StudentID=%d"%tan)
        con.commit()
        print("<h2> Data Deleted Successfully</h2>")
    except Exception as e:
        print(e)

else:
    print("<h2>Invalid Student ID</h2>")

con.close()

print('<hr>')

print("<br><a href='Admin.html'>Refresh..</a>")
