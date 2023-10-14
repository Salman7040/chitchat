import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

# video_capture = cv2.VideoCapture(0)

# elon_child = face_recognition.load_image_file("C:/Users/DELL/Desktop/problemyash/image/elon_child.jpeg")
# face_loc1=face_recognition.face_locations(elon_child)
# elon_child_enco = face_recognition.face_encodings(elon_child,face_loc1)[0]

# elon = face_recognition.load_image_file("C:/Users/DELL/Desktop/problemyash/image/rdj.jpeg")
# face_loc2=face_recognition.face_locations(elon)
# elon_enco = face_recognition.face_encodings(elon,face_loc2)[0]

img_file=[
"image/elon_child.jpeg",
"image/elon.jpeg",
"image/rdj.jpeg",

]

name=[
    "elon_chid",
    "elon",
    "rdj"
]



j=2
for i in range(0,3):
    img_name1=face_recognition.load_image_file(img_file[i])
    img_name_enoc1=face_recognition.face_encodings(img_name1)[0]

    img_name2=face_recognition.load_image_file(img_file[j-i])
    img_name_enoc2=face_recognition.face_encodings(img_name2)[0]


    res=face_recognition.compare_faces([img_name_enoc1],img_name_enoc2)
    if res[0]==True:
        print("img equal :",name[i])
    else:
        print("img not equal :",name[i])





    

    

