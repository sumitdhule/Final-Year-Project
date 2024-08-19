#!C:\Users\DELL\AppData\Local\Programs\Python\Python310\python
import cgi
import pymysql

print("Content-type:text/html")
print()

req=cgi.FieldStorage()
ano=int(req.getvalue("bno"))
anm=req.getvalue("bnm")
aut=req.getvalue("aut")
bal=float(req.getvalue("pc"))
atyp=req.getvalue("btyp")


con=pymysql.connect(host='bnlexxma2lfq3xh9a90s-mysql.services.clever-cloud.com',user='uxteh95x3dfl49xv',password='4cacwHSLS9DaE8q0ljsp',database='bnlexxma2lfq3xh9a90s')
curs=con.cursor()

try:
    curs.execute("insert into Studentdata values(%d,'%s','%s',%.2f,'%s')"%(ano,anm,aut,bal,atyp))
    con.commit()
    print("<h2>Data Inserted Successfully...</h2>")
except Exception as e:
    print("Error : ",e) 

con.close()
print('<hr>')

print("<br><a href='Admin.html'>Refresh..</a>")