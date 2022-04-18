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


#################PEEER

import math
import zipfile
from PIL import Image, ImageOps, ImageDraw
import pytesseract
import cv2 as cv
import numpy as np
# loading the face detection classifier
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
parsed_img = {}
with zipfile.ZipFile('small_img.zip', 'r') as archive:
    for entry in archive.infolist():
        with archive.open(entry) as file:
            image = Image.open(file).convert('RGB')
            parsed_img[entry.filename] = {'pil_img':image}
for imgName in parsed_img.keys():
    text = pytesseract.image_to_string(parsed_img[imgName]['pil_img'])
    parsed_img[imgName]['text'] = text
for imgName in parsed_img.keys():
    open_cv_image = np.array(parsed_img[imgName]['pil_img']) 
    img = cv.cvtColor(open_cv_image, cv.COLOR_BGR2GRAY)
    faces_bounding_boxes = face_cascade.detectMultiScale(img, 1.3, 5)
    parsed_img[imgName]['faces'] = []
    for x,y,w,h in faces_bounding_boxes:
        face = parsed_img[imgName]['pil_img'].crop((x,y,x+w,y+h))
        parsed_img[imgName]['faces'].append(face)
for imgName in parsed_img.keys():
    for face in parsed_img[imgName]['faces']:
        face.thumbnail((100,100),Image.ANTIALIAS)
def search(keyword):
    for imgName in parsed_img:
        if (keyword in parsed_img[imgName]['text']):
            if(len(parsed_img[imgName]['faces']) != 0):
                print("Result found in file {}".format(imgName))
                h = math.ceil(len(parsed_img[imgName]['faces'])/5)
                sheet=Image.new('RGB',(500, 100*h))
                xc = 0
                yc = 0
                for img in parsed_img[imgName]['faces']:
                    contact_sheet.paste(img, (xc, yc))
                    if xc + 100 == contact_sheet.width:
                        xc = 0
                        yc += 100
                    else:
                        xc += 100
                        
                display(sheet)
            else:
                print("Result found in file {} \nBut there were no faces in that file\n\n".format(img_name))
    return
search('Christopher')

search('Mark')

 
 