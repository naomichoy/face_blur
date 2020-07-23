from PIL import Image
import face_recognition
import cv2
import os

PROCESSED_DIR = './processed/'
DIR_PATH = './photos/'
PROCESSED_FILE = ''
file_count = 0

for filename in os.listdir(DIR_PATH):
    
    photo_full_path = DIR_PATH + filename   
    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file(photo_full_path)

    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
    # See also: find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image)

    # print("I found {} face(s) in this photograph.".format(len(face_locations)))

    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]
        # pil_image = Image.fromarray(face_image)
        # pil_image.show()

        #blur image and save to original
        image_blur = cv2.GaussianBlur(face_image, (99, 99), 30)
        image[top:bottom, left:right] = image_blur

    pil_image = Image.fromarray(image)

    # PROCESSED_FILE = "../processed/" + str(file_count) + ".jpg"
    PROCESSED_FILE = PROCESSED_DIR + "blured_" + str(file_count) + ".jpg"
    print("saving file " + PROCESSED_FILE)
    pil_image.save(PROCESSED_FILE)

    file_count += 1

