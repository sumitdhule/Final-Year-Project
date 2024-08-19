import firebase_admin
from firebase_admin import credentials, db
#import jsontosql

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionbasedatte-b4a54-default-rtdb.firebaseio.com/"
})

# Access the Database
ref = db.reference('Students')

data = ref.get()
#print(data)
class AttendanceTracker:
    def __init__(self, students):
        self.students = students
        self.attendance_record = {student: [] for student in students}

    def mark_attendance(self, lecture_number, present_students):
        for student in self.students:
            if student in present_students:
                self.attendance_record[student].append(lecture_number)
            else:
                self.attendance_record[student].append(0)  # Mark absent if not present

    def display_attendance(self):
        print("Attendance Record:")
        for student, attendance_list in self.attendance_record.items():
            print(f"{student}: {attendance_list}")

print(data)
            
students = []
for item in data:
    nm=data[item]['fname']
    print(nm)
    #print(type(nm))
    #students.append(str(nm))
print(students)
'''
attendance_tracker = AttendanceTracker(students)

# Mark attendance for lecture 1
attendance_tracker.mark_attendance(1, ["Alice", "Bob", "Charlie"])

# Mark attendance for lecture 2
attendance_tracker.mark_attendance(2, ["Alice", "Charlie", "David"])

# Display the attendance record
attendance_tracker.display_attendance()

'''