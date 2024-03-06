from googletrans import Translator
#print(googletrans.LANGCODES)
#'japanese': 'ja'

def translate(text):
    translator = Translator()
    text1 = text

    result = str(translator.translate(text1, src = 'en', dest = 'ja'))
    result_list = result.split(',')
    translated_result = result_list[2][6::]
    
    return translated_result



