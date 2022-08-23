from PIL import Image , ImageEnhance

img1 = Image.open('Image\somlalit.jpg')
# img1.show()
Max_zise = (1080,480)
img1.thumbnail(Max_zise)
img1.show()
