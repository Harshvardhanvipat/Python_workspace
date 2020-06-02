# import translate
from translate import Translator

translator = Translator(to_lang='ja')
try:
    with open('./test.txt', mode='r+') as my_file:
        text = (my_file.read())
        translation = translator.translate(text)
        with open('./test-ja.text', mode='w') as test_output_file:
            test_output_file.write(translation)

        print(translation)
except FileNotFoundError as e:
    print('check your file path! ')
