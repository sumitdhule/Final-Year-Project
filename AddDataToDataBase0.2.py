import os
import firebase_admin
from firebase_admin import credentials, db, storage
import AppendSingleEncoding


def initialize_firebase():
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': "https://facerecognitionbasedatte-b4a54-default-rtdb.firebaseio.com/",
        'storageBucket': "facerecognitionbasedatte-b4a54.appspot.com"
    })


def add_student_to_database(student_rollN, Section, student_Department, student_fname, student_lname, year_of_add,
                            imageId):
    ref = db.reference('Students')
    student_id = create_student_id(student_rollN, Section, student_fname, student_lname, year_of_add,
                                   student_Department)
    ref.child(student_id).set({
        "fname": student_fname,
        "lname": student_lname,
        "year": year_of_add,
        "Roll Number": student_rollN,
        "Section": Section,
        "Department": student_Department,
        "Attendance": {},
        "Attendance Sheet": {}
    })
    return student_id


def create_student_id(student_rollN, Section, student_fname, student_lname, year_of_add, student_Department):
    return str(student_rollN) + Section + student_fname[:1] + student_lname[:1] + str(year_of_add)[2:] + str(
        student_Department)


def upload_image_to_storage(local_img_path, Destination_path):
    bucket = storage.bucket()
    blob = bucket.blob(Destination_path)
    blob.upload_from_filename(local_img_path)


def rename_image(local_img_path, Destination_path):
    os.rename(local_img_path, Destination_path)


def add_new_student():
    try:
        student_rollN = input("Enter student Roll Number: ")
        Section = input("Enter student Section: ")
        student_Department = input("Enter student Department(cse/it/ce/me/ex/ee): ")
        student_fname = input("Enter student First name: ")
        student_lname = input("Enter student Last name: ")
        year_of_add = input("Enter student year of admission : ")
        imageId = input("Enter student image ID : ")
        local_path = 'images/'
        local_img_path = os.path.join(local_path, f"{imageId}.jpg")
        student_id = create_student_id(student_rollN, Section, student_fname, student_lname, year_of_add,
                                       student_Department)
        Destination_path = os.path.join(local_path, f"{student_id}.jpg")

        upload_image_to_storage(local_img_path, Destination_path)

        add_student_to_database(student_rollN, Section, student_Department, student_fname, student_lname, year_of_add,
                                imageId)
        rename_image(local_img_path, Destination_path)
        print(f"Renamed {local_img_path} to {Destination_path}")

        # Append this image encodings to existing .pickle file for face recognition
        AppendSingleEncoding.add_new_encoding(local_img_path, student_id)
        print("Student added successfully!")

    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except Exception as e: 
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    initialize_firebase()
    while True:
        add_new_student_option = input("Do you want to add a new student? (y/n): ")
        if add_new_student_option.lower() == 'y':
            add_new_student()
        else:
            print("Exiting program...")
            break
