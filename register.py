#!C:\Users\DELL\AppData\Local\Programs\Python\Python310\python
import cgi
import pymysql

print("Content-type:text/html")
print()

reqobj=cgi.FieldStorage()
id=reqobj.getvalue("uid")
pas=reqobj.getvalue("pass")
unm=reqobj.getvalue("nm")
gn=reqobj.getvalue("cid")

#print(id+pas)
if (gn=="Prmit"):
    con=pymysql.connect(host='bnlexxma2lfq3xh9a90s-mysql.services.clever-cloud.com',user='uxteh95x3dfl49xv',password='4cacwHSLS9DaE8q0ljsp',database='bnlexxma2lfq3xh9a90s')
    curs=con.cursor()
    try:
        curs.execute("insert into Authority value('%s','%s','%s')" %(id,unm,pas))
        con.commit()
        print("<h3> User Registered Succesfully </h3>")
    except Exception as e:
        print("<h3> Registration Failed </h3>")
        print(e)

    con.close()
    print('<hr>')
else:
    print("Confirmation key is Wrong..")

print("<br><a href='index.html'>Home</a>")