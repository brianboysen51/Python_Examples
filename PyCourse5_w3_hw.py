import zipfile
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
# dictionary of lists indexed with filenames, 0 being PIL image file, 1 being the text in the image
images = {} 
# list of filenames
name_list = []

def unzip_images(zip_name):
    '''
    iterates over images in zipfile and extract/modifies global dictionary for all
    Additionally creates namelist containing names of all images in the zipfile
    '''
    zippyboi = zipfile.ZipFile(zip_name)
    for each in zippyboi.infolist():
        images[each.filename] = [Image.open(zippyboi.open(each.filename))]
        name_list.append(each.filename)

# global data structure, iterates through images.zip to print out the name of file

if __name__ == '__main__':
    unzip_images('readonly/images.zip')
# Iterate through all the names
    for name in name_list:
        #print(name)
        #display(images[name][0])
        img = images[name][0]
# omit line separators "-\n", modify gloabal structure to append text to image, 
        images[name].append(pytesseract.image_to_string(img).replace('-\n',''))
# using 'in' to see if substring exists name list
        if 'Mark' in images[name][1]: 
            print('Results found in file',name)
# try to store bounding boxes of all faces detected and modify global data structure to append faces found in each image
            try:
                faces = (face_cascade.detectMultiScale(np.array(img),1.35,4)).tolist()
                images[name].append(faces)
                faces_in_each = []
# modifying local data structure in each iter to store PIL of faces
                for x,y,w,h in images[name][2]:
                    faces_in_each.append(img.crop((x,y,x+w,y+h)))
# contact sheet mod -> display each iter result
                contact_sheet = Image.new(img.mode, (550,110*int(np.ceil(len(faces_in_each)/5))))
                x = 0
                y = 0
# use PIL.Image.thumbnail function to resize without impacting aspect ratio
                for face in faces_in_each:
                    face.thumbnail((110,110))
                    contact_sheet.paste(face, (x, y))
                    
                    if x+110 == contact_sheet.width:
                        x=0
                        y=y+110
                    else:
                        x=x+110
                        
                display(contact_sheet)
            except:
                print('But there were no faces in that file!')

