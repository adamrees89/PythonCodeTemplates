## Credit to Haider Imtiaz

# Image Editor
# pip install pillow
from PIL import Image
from PIL import ImageDraw
# Combine Image
img1 = Image.open('img101.jpg')
img2 = Image.open('img102.jpg')
combine = Image.blend(img1, img2, 0.5)
# Resize Image
resize = Image.open('img101.jpg')
resize = resize.resize((300, 300))
# Flip an Image 
flip_image = Image.open('img101.jpg')
flip_image = flip_image.transpose(Image.FLIP_LEFT_RIGHT)
# Blur an Image
blur_image = Image.open('img101.jpg')
blur_image = blur_image.filter(Image.BLUR)
# Add Drop Shadow
shadow_image = Image.open('img101.jpg')
shadow_image = shadow_image.filter(Image.EDGE_ENHANCE_MORE)
# Crop an Image
crop_image = Image.open('img101.jpg')
crop_image = crop_image.crop((50, 50, 300, 200))
#Add Brightness
bright_image = Image.open('img101.jpg')
bright_image = bright_image.point(lambda p: p + 50)
# Add Text to Image
text_image = Image.open('img101.jpg')
text_image = text_image.convert('RGB')
draw = ImageDraw.Draw(text_image)
draw.text((10, 10), "Hello World", (255, 255, 255))
# Rotate an Image
rotate_image = Image.open('img101.jpg')
rotate_image = rotate_image.rotate(90)
# Save Image
img1.save('img101.jpg')

#---------------------------------------------------

## Credit to Haider Imtiaz
# Install this Library  "pip install opencv-python"
import cv2
 
original_img = cv2.imread('img_500x326.jpg', 1)
water_mark = cv2.imread('watermark_500x326.jpg', 1)
 
img = cv2.addWeighted(water_mark, 0.1, original_img, 1.0, 0)
 
cv2.imwrite('Watermark.png',img)
 
cv2.waitKey(0)
 
cv2.destroyAllWindows()

#---------------------------------------------------

## Credit to Haider Imtiaz
#Resize an image
import cv2
 
img = cv2.imread('Image.jpg', cv2.IMREAD_UNCHANGED)
scale_percent = 50 # change accordingly
 
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
 
dimension = (width, height)
resized = cv2.resize(img, dimension, interpolation = cv2.INTER_AREA)
cv2.imwrite('resized.jpg', resized) # Image saved
cv2.waitKey(0)
cv2.destroyAllWindows()

#---------------------------------------------------

## Credit to Haider Imtiaz
#Convert HTML to image
# Install this library "pip install html2image"
from html2image import Html2Image
 
html = Html2Image()
 
html.screenshot(url="https://www.medium.com", save_as="screen.png")

#---------------------------------------------------

## Credit to Haider Imtiaz
# Create QR CODE
import pyqrcode
 
Str = 'www.medium.com'
 
Qr_Code = pyqrcode.create(Str)
 
Qr_Code.svg('qr.svg', scale=8)

#---------------------------------------------------

## Credit to Haider Imtiaz
# Image to GrayScale
# install this library  "pip install pillow"
from PIL import Image
img = Image.open('image.jpg').convert('L')
img.save('greyscale.jpg')