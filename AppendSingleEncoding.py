import cv2
import face_recognition
import pickle
import os


def add_new_encoding(new_image_path, new_image_id, encode_file_path="EncodeFile.p"):
    """
    Adds a new face encoding to an existing .p file containing face encodings.

    Args:
    - new_image_path: Path to the new image file.
    - new_image_id: Unique identifier for the new image.
    - encode_file_path: Path to the .p file containing the face encodings (default is "EncodeFile.p").

    Returns:
    None
    """
    # Load existing face encodings from the .p file
    try:
        with open(encode_file_path, 'rb') as file:
            encodeListKnownWithIds = pickle.load(file)
        encodingsKnown, studentIds = encodeListKnownWithIds
    except FileNotFoundError:
        encodingsKnown, studentIds = [], []

    # Add a new image and its encoding
    new_image = cv2.imread(new_image_path)
    new_encoding = face_recognition.face_encodings(new_image)[0]
    encodingsKnown.append(new_encoding)
    studentIds.append(new_image_id)

    # Save the updated encodings back to the .p file
    encodeListKnownWithIds = [encodingsKnown, studentIds]
    with open(encode_file_path, 'wb') as file:
        pickle.dump(encodeListKnownWithIds, file)

    print("File Updated")


# Example usage
new_image_path = 'Images/3879.jpg'
new_image_id = '3879'
add_new_encoding(new_image_path, new_image_id)
