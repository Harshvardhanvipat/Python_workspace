# import translate module to this script so that we can use it
from translate import Translator

# here we are specifiying the language i.e. japanese
translator = Translator(to_lang='ja')

''' using try and except block to catch any exceptions or errors

# step 1 : we open the file with read and write mode specified

# step 2 : read the file that we have opened and thus save the read file in variable text

#  step 3 : using the translator module we translate the text and save that into a new variable
# step 4 :we create a new file that is test-ja.txt with write permission and write the translated text to the file

# step 5 : print the output to the terminal

# keep the test.txt and script_translator.py in the same directory, otherwise change the location of reading the file while reading test.txt(whatever the file path is) 
to get the file path use pwd (present working directory) of the files

# run this file using: python3 script_translator.py
'''
try:
    with open('./test.txt', mode='r+') as my_file:
        text = (my_file.read())
        translation = translator.translate(text)
        with open('./test-ja.text', mode='w') as test_output_file:
            test_output_file.write(translation)

        print(translation)
except FileNotFoundError as e:
    print('check your file path! ')
