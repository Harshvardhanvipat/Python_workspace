
# grab the first and the second argument

# check if new/ exists or create it

# loop through Pokedox and convert the images to png and save it to new folder
# folder_Pokedox = '  '
# folder_new = '  '


# input_folder = sys.argv[1]
# output_folder = sys.argv[2]

# print(input_folder, output_folder)

# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

import sys
import os
from PIL import Image

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)


for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{path}{filename}')
    # added the / in case user doesn't enter it. You may want to check for this and add or remover it.
    img.save(f'{directory}/{clean_name}.png', 'png')
    print('all done!')

    # print(input_folder)
    # img = Image.open(f"./{input_folder}{filename}", "rb")
    # img.save(f'{output_folder}{filename}', 'png')
    # print("all_done")
