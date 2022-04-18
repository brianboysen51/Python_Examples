import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageEnhance
from PIL import ImageDraw

# Read image and convert to RGB
image = Image.open("readonly/msi_recruitment.gif")
image = image.convert("RGB")

# Initialize draw object, set intensities
draw = ImageDraw.ImageDraw(image)
intensities = [.1, .5, .9]

# Initialize font with size 50
font = ImageFont.truetype("readonly/fanwood-webfont.ttf", 50)

# Create background for text
w, h = image.width, image.height + 50  # dimension of rectangle
rect = Image.new("RGB", (w, h)) 

# Create contact sheet
num_images = 9
contact_sheet = PIL.Image.new(image.mode, (image.width * 3, rect.height * 3))

x = 0
y = 0
c = 0 
for idx in range(num_images):    
    # Set different intensity for each image idx % 3 -> ensures idx to be [0, 1, 2]
    intensity = intensities[idx % 3] 
    # get channels of the image
    r, g, b = image.split()  
    # store in a list to be indexed
    channels = [r, g, b]  
    channels[c] = channels[c].point(lambda i: i * intensity)
    result = Image.merge("RGB", channels)

    # Paste each image to contact sheet
    contact_sheet.paste(rect, (x, y))
    contact_sheet.paste(result, (x, y))
    
    # Draw text on the contact sheet
    draw = ImageDraw.ImageDraw(contact_sheet)
    # Create text with different intensities
    fill = [250, 250, 250] 
    # adjust rgb depending on the current channel & intensity
    fill[c] = int(fill[c] * intensity) 
    # convert to tuple for fill arg
    fill = tuple(fill)  
    # Add 455 to offset height of image
    draw.text((x, y + 455), "channel {} intensity {}".format(c, intensity), fill=fill, font=font)  
    
    # Update x position. Set to 0 if x reaches 3rd column of the contact sheet and update Y to activate next row of contact sheet; update channel index
    if x + image.width == contact_sheet.width:
        x = 0
        y += rect.height
        c += 1
    else:
        x += image.width
        
# Resize and display contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width / 2), int(contact_sheet.height / 2)))
display(contact_sheet)




##### Peer reviwed 1

import PIL

from PIL import Image

from PIL import ImageFont, ImageDraw

from PIL import ImageEnhance

from IPython.display import display

image = Image.open('readonly/msi_recruitment.gif')
image = image.convert('RGB')
font = ImageFont.truetype("readonly/fanwood-webfont.ttf",50)

images = []
lables = []
for i in range(3):
    for j in (0.1,0.5,0.9):
        RGB = image.split()   #seperate to R, G, B
        imgs =RGB[i].point(lambda x:x*j)  # creating images looping R,G,B and intensity 0.1,0.5,0.9
        RGB[i].paste(imgs) # pasting different color intensity to color.
        imgs_merge = Image.merge(image.mode, RGB) # 
        lables.append('channel {} intensity {}'.format(i,j)) 
        images.append(imgs_merge)
print('images = len', len(images))
print('lables = len',len(lables))

first_image=images[0]
#display(first_image)
print(first_image.mode, first_image.size)
contact_sheet = PIL.Image.new(first_image.mode, (first_image.width*3, first_image.height*3+3*50))

x= 0
y= 0
draw = ImageDraw.Draw(contact_sheet)
display(draw)
print(draw)
for sq, img in enumerate(images):
    contact_sheet.paste(img, (x,y))
    draw.text((x, y+first_image.height + 10), lables[sq], font = font)
    if x + first_image.width == contact_sheet.width:
        x = 0
        y = y + first_image.height + 50
    else:
        x = x + first_image.width
        
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)

#### Peer 2 

import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageEnhance
from PIL import ImageDraw



image=Image.open("my_img.JPG")
image=image.convert('RGB')

font_ = ImageFont.truetype(r"C:\Users\System-Pc\Desktop\arial.ttf",50)
images = []
for fact in [0.1,0.5,0.9] :
    my_image = image.copy()
    t1 = 'channel 0 intensity ' + str(fact)
    draw = ImageDraw.Draw(my_image)
    draw.rectangle([0,500,1001,564],fill='black')
    draw.text((2,500),t1,font=font_, align ="left")
    pix = my_image.load()
    for i_width in range(image.width):
        for i_height in range(image.height): 
            pix[i_width,i_height] =(int(fact*pix[i_width,i_height][0]),pix[i_width,i_height][1],pix[i_width,i_height][2])    
    
    images.append(my_image)
 
    
    my_image = image.copy()
    t1 = 'channel 1 intensity ' + str(fact)
    draw = ImageDraw.Draw(my_image)
    draw.rectangle([0,500,1001,564],fill='black')
    draw.text((2,500),t1,font=font_, align ="left")
    pix = my_image.load()
    for i_width in range(image.width):
        for i_height in range(image.height): 
            pix[i_width,i_height]=(pix[i_width,i_height][0],int(fact*pix[i_width,i_height][1]),pix[i_width,i_height][2])
    images.append(my_image)
    
    
    my_image = image.copy()
    t1 = 'channel 2 intensity ' + str(fact)
    draw = ImageDraw.Draw(my_image)
    draw.rectangle([0,500,1001,564],fill='black')
    draw.text((2,500),t1,font=font_, align ="left")    
    pix = my_image.load()
    for i_width in range(image.width):
        for i_height in range(image.height): 
            pix[i_width,i_height]=(pix[i_width,i_height][0],pix[i_width,i_height][1],int(fact*pix[i_width,i_height][2]))
 
    images.append(my_image)

first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
y=0
x=0
for img in images:
    contact_sheet.paste(img, (x, y) )
    if y+first_image.height == contact_sheet.height:
        x=x+first_image.width
        y=0
    else:
        y=y+first_image.height        

contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)

#third peers was trash



