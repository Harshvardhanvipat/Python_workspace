from PIL import Image, ImageFilter

# img = Image.open('./pokedox/image1.jpg')
# filteredImage = img.filter(ImageFilter.SMOOTH)
# filtered_image = img.convert('L')
# filtered_image.save("grey.png", 'png')
# filtered_image.show()
# filtered_image.resize((200, 200))
# rotated_image = filtered_image.rotate(90)
# rotated_image.show()

# print(img.format)
# print(img.size)
# print(img.mode)

img = Image.open('./pokedox/astro.jpg')
# new_img = img.resize((400, 400)) # using resize doesnot keep the aspect ratio

# thus we use thumbnail, as it keeps the aspect ratio intact. And one more thing is that thumbnail method doesnot return a new image, it modifies the old image
img.thumbnail((400, 400))  # here we are using thumbnail
img.save('thumbnail.jpeg')  # modifing the same image
