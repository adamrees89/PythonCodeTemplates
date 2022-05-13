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