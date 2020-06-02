from PIL import Image, ImageFilter
import sys
import os

# grab the first and the second argument

# check if new/ exists or create it

# loop through Pokedox and convert the images to png and save it to new folder
# folder_Pokedox = '  '
# folder_new = '  '


input_folder = sys.argv[1]
output_folder = sys.argv[2]

print(input_folder, output_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    print(input_folder)
    img = Image.open(f"./{input_folder}{filename}", "rb")
    img.save(f'{output_folder}{filename}', 'png')
    print("all_done")
