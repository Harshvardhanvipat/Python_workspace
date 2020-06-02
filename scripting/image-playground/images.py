from PIL import Image, ImageFilter

img = Image.open('./pokedox/image1.jpg')
# filteredImage = img.filter(ImageFilter.SMOOTH)
filtered_image = img.convert('L')
filtered_image.save("blur.png", 'png')


# print(img.format)
# print(img.size)
# print(img.mode)
