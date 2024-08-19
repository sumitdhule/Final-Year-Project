import firebase_admin
from firebase_admin import credentials, db
import json

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionbasedatte-b4a54-default-rtdb.firebaseio.com/"
})

# Access the Database
ref = db.reference('Students')
data = ref.get()
print(data)
from json2table import convert 

with open("1.txt", "r") as file:
    dna = file.read()

print(dna)

# will print ATCAGTGGAAACCCAGTGCTAGAGGATGGAATGACCTTAAATCAGGGACGATATTAAACGGAA

html=convert(json.loads(str(dna)))
print(html)
#print(data.Attendance


# Assume jsonData contains your JSON data
#jsonData = '{"key1": "value1", "key2": "value2", "key3": "value3"}'

# Parse JSON data
#data = json.loads(jsonData)
'''
# Retrieve value of a specific key
desired_key = "Attendance"
if desired_key in data:
    value = data[desired_key]
    print(f"The value of '{desired_key}' is '{value}'")
else:
    print(f"Key '{desired_key}' not found")

# Alternatively, you can use get() method to handle missing keys gracefully
value = data.get(desired_key, "Key not found")
print(f"The value of '{desired_key}' is '{value}'")
'''
'''
for item in data:
    print(item,":")
    #print(data[item],"\n")
    nm=data[item]["fname"]
    rno=int(data[item]["Roll Number"])
    yr=int(data[item]["year"])
    dept=data[item]["Department"]
    
    print("Roll NO : ",rno)
    print("Student Name : ",nm)
    print("Year Of Admission : ",yr)
    print("Department : ",dept)
    
    at=data[item]["Attendance"]
    print("Attendence Record : ",at,"\n\n")
    for val in at:
        print(val[:2],"/",val[2:4],"/",val[4:8],"  Time : ",val[8:10],":",val[10:12],":",val[12:14])
# Prints value corresponding to key 'name' in Dict1


# Prints value corresponding to key 'age' in Dict2
#print(Dict['Dict2']['age'])

#value = ref.get(item, {}).get('Attendence')
'''