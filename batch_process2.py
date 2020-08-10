from PIL import Image
import face_recognition
import cv2
import os

PROCESSED_DIR = './processed/'
DIR_PATH = './photos/'
PROCESSED_FILE = ''
file_count = 0

def locate_and_blur (image, face_locations):

    for face_location in face_locations:

        # Print the location of each face in this image
        top, right, bottom, left = face_location

        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]

        #blur image and save to original
        image_blur = cv2.GaussianBlur(face_image, (99, 99), 30)
        image[top:bottom, left:right] = image_blur


for filename in os.listdir(DIR_PATH):
	try:
		print ("processing " + filename)
		photo_full_path = DIR_PATH + filename   
		image = face_recognition.load_image_file(photo_full_path) # Load the jpg file into a numpy array
		face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
		locate_and_blur (image, face_locations)

		# 2nd screening with HOG model
		face_locations = face_recognition.face_locations(image)
		locate_and_blur (image, face_locations)

		pil_image = Image.fromarray(image)

		# PROCESSED_FILE = "../processed/" + str(file_count) + ".jpg"
		PROCESSED_FILE = PROCESSED_DIR + filename + "_blured_" + str(file_count) + ".jpg"
		print("saving file " + PROCESSED_FILE)
		pil_image.save(PROCESSED_FILE)

		file_count += 1

	except Exception as e:
		print (e)
