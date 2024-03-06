import deepl

def translate_text(input_text, key):
    #auth = input("Enter authentication key for DeepL: ")

    env_auth_key = key
    #env_server_url = "https://api-free.deepl.com/v2/translate"

    text = input_text

    translator = deepl.Translator(env_auth_key)
    result = translator.translate_text(text, target_lang = "JA")
    return(result)

"""pog = "Hello, my name is Alice."
print(translate_text(pog))"""
