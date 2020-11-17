from PIL import Image
import face_recognition
import cv2
import os
# import piexif

PROCESSED_DIR = './processed/'
DIR_PATH = './photos/'
PROCESSED_FILE = ''
file_count = 0
error_log = open("error_log.txt", "a")

def locate_and_blur (image, face_locations):

    for face_location in face_locations:

        # Print the location of each face in this image
        top, right, bottom, left = face_location

        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]

        #blur image and save to original
        image_blur = cv2.GaussianBlur(face_image, (99, 99), 30)
        image[top:bottom, left:right] = image_blur

# load exif data
# exif_dict = piexif.load(im.info["exif"])
# exif_bytes = piexif.dump(exif_dict)

for filename in os.listdir(DIR_PATH):
	try:
		print ("processing " + filename)
		photo_full_path = DIR_PATH + filename

		# load exif data, without piexif lib
		im = Image.open(photo_full_path)
		exif = im.info['exif']
		
		image = face_recognition.load_image_file(photo_full_path) # Load the jpg file into a numpy array
		face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
		locate_and_blur (image, face_locations)

		# 2nd screening with HOG model
		face_locations = face_recognition.face_locations(image)
		locate_and_blur (image, face_locations)

		pil_image = Image.fromarray(image)

		# PROCESSED_FILE = "../processed/" + str(file_count)
		PROCESSED_FILE = PROCESSED_DIR + str(file_count) + "_blured_"  + filename
		print("saving file " + PROCESSED_FILE)
		pil_image.save(PROCESSED_FILE, exif=exif)

		file_count += 1

	except Exception as e:
		print (e)
		# append error to file
		error_log.write(str(e) + " on " + filename + "\n")

error_log.close()
