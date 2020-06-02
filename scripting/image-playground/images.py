from PIL import Image, ImageFilter

img = Image.open('./pokedox/image1.jpg')
# filteredImage = img.filter(ImageFilter.SMOOTH)
filtered_image = img.convert('L')
filtered_image.save("grey.png", 'png')
filtered_image.show()
filtered_image.resize((200, 200))
rotated_image = filtered_image.rotate(90)
rotated_image.show()

# print(img.format)
# print(img.size)
# print(img.mode)
