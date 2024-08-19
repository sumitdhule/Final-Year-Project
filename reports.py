#!C:\Users\DELL\AppData\Local\Programs\Python\Python310\python
#import cgi
import pymysql

print("Content-type:text/html")
print()
print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<div class='container'><br>")
con=pymysql.connect(host='bnlexxma2lfq3xh9a90s-mysql.services.clever-cloud.com',user='uxteh95x3dfl49xv',password='4cacwHSLS9DaE8q0ljsp',database='bnlexxma2lfq3xh9a90s')
curs=con.cursor()

curs.execute("select * from Studantdata")
data=curs.fetchall()
print("<h2 class='display-5'> Student Data </h2><hr>")

print("<table class='table table-bordered table-hover'>")
print("<tr style='background-color:azure'>")
print("<th>YearOFAdmission")  
print("<th>StudentName")
print("<th>Department")
print("<th>Roll No") 
#print("<th>gender")
print("</tr>")

for rec in data:
    print("<tr>")
    print("<td>%d" %rec[0])
    print("<td>%s" %rec[1])
    print("<td>%s" %rec[2])
    print("<td>%d" %rec[3])
    #print("<td>%s" %rec[4])
    print("</tr>")

con.close()
print("</table>")
print("</div>")