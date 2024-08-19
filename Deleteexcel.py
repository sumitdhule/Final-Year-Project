#!C:\Users\DELL\AppData\Local\Programs\Python\Python310\python
#import cgi
from pathlib import Path
print("Content-type:text/html")
print()

file_path = Path('./json_files/Student.json')
file_path1 = Path('./xlsx_files/Studentdata.xlsx')
# Delete the file
file_path.unlink()
file_path1.unlink()

print("<a href='Admin.html'>Go Back</a>")