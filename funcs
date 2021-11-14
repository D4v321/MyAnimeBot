from langdetect import detect as detect
from translate import Translator
from langdetect import DetectorFactory
DetectorFactory.seed = 0

def detect_language(input):
  lang = detect(input)
  if lang == 'en' or lang =='ca':
    lang = 'en'
    return [input, lang]
  if lang == 'nl' or lang == 'af':
    lang = 'nl'
    return [input, lang]
  else:
    return [0,lang]

def translate_input(input_lang):
    input = input_lang[0]
    lang = input_lang[1]
    translator_en = Translator(from_lang = "nl", to_lang="en") # translates phrase to english
    if lang == 'en' or lang =='ca':
      lang = 'en'
      return [input, lang]
    if lang == 'nl' or lang == 'af':
      input = translator_en.translate(input)
      lang = 'nl'
      return [input, lang]
    else:
      return[0,lang]

def translate_output(output):
  chatbot_output, lang = output[0], output[1]
  if lang == 'en'  or lang =='ca':
    translated = 0
  elif lang == 'nl' or lang == 'af':
    translated = 1
  else:
    return 0
  if translated == 0:   #input was in English, so leave output in English
    return chatbot_output
  elif translated == 1:
    translator_nl = Translator(from_lang = "en", to_lang="nl") # translates phrase to dutch
    translated = 0
    chatbot_output = translator_nl.translate(chatbot_output)
    return chatbot_output
