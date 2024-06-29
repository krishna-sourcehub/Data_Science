from googletrans import Translator
from gtts import gTTS
import os
import pygame
from playsound import playsound 
flag = 0
import speech_recognition as sr 

selectlang="say your preferred language"

dic = {
    'english': 'en',
    'tamil': 'ta',
    'telugu': 'te',
    'hindi': 'hi',
    'malayalam': 'ml',
    'gujarati': 'gu',
    'kannada': 'kn',
    'bengali': 'bn',
}

dic1 = ('afrikaans', 'af', 'albanian', 'sq',  
       'amharic', 'am', 'arabic', 'ar', 
       'armenian', 'hy', 'azerbaijani', 'az',  
       'basque', 'eu', 'belarusian', 'be', 
       'bengali', 'bn', 'bosnian', 'bs', 'bulgarian', 
       'bg', 'catalan', 'ca', 'cebuano', 
       'ceb', 'chichewa', 'ny', 'chinese (simplified)', 
       'zh-cn', 'chinese (traditional)', 
       'zh-tw', 'corsican', 'co', 'croatian', 'hr', 
       'czech', 'cs', 'danish', 'da', 'dutch', 
       'nl', 'english', 'en', 'esperanto', 'eo',  
       'estonian', 'et', 'filipino', 'tl', 'finnish', 
       'fi', 'french', 'fr', 'frisian', 'fy', 'galician', 
       'gl', 'georgian', 'ka', 'german', 
       'de', 'greek', 'el', 'gujarati', 'gu', 
       'haitian creole', 'ht', 'hausa', 'ha', 
       'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 
       'hi', 'hmong', 'hmn', 'hungarian', 
       'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',  
       'id', 'irish', 'ga', 'italian', 
       'it', 'japanese', 'ja', 'javanese', 'jw', 
       'kannada', 'kn', 'kazakh', 'kk', 'khmer', 
       'km', 'korean', 'ko', 'kurdish (kurmanji)',  
       'ku', 'kyrgyz', 'ky', 'lao', 'lo', 
       'latin', 'la', 'latvian', 'lv', 'lithuanian', 
       'lt', 'luxembourgish', 'lb', 
       'macedonian', 'mk', 'malagasy', 'mg', 'malay', 
       'ms', 'malayalam', 'ml', 'maltese', 
       'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian', 
       'mn', 'myanmar (burmese)', 'my', 
       'nepali', 'ne', 'norwegian', 'no', 'odia', 'or', 
       'pashto', 'ps', 'persian', 'fa', 
       'polish', 'pl', 'portuguese', 'pt', 'punjabi',  
       'pa', 'romanian', 'ro', 'russian', 
       'ru', 'samoan', 'sm', 'scots gaelic', 'gd', 
       'serbian', 'sr', 'sesotho', 'st', 
       'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si', 
       'slovak', 'sk', 'slovenian', 'sl', 
       'somali', 'so', 'spanish', 'es', 'sundanese', 
       'su', 'swahili', 'sw', 'swedish', 
       'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu', 
       'te', 'thai', 'th', 'turkish', 
       'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 
       'ug', 'uzbek',  'uz', 
       'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh', 
       'yiddish', 'yi', 'yoruba', 
       'yo', 'zulu', 'zu')

def langinitial(lang,statement):
    # invoking Translator
    translator = Translator()
    
    # Prompt to ask the user about their preferred language
    query = statement
    
    # Translating the prompt to the specified language
    text_to_translate = translator.translate(query, dest=dic[lang])
    text = text_to_translate.text
    
    # Using Google-Text-to-Speech ie, gTTS() method to speak the translated text
    speak = gTTS(text=text, lang=dic[lang], slow=False)
    
    # Using save() method to save the translated speech in captured_voice.mp3
    speak.save("captured_voice.mp3")
    
    # Using Pygame to play the audio
    pygame.mixer.init()
    pygame.mixer.music.load("captured_voice.mp3")
    pygame.mixer.music.play()
    
    # Wait for the audio to finish playing
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(10)
    
    # Clean up
    pygame.mixer.quit()
    os.remove('captured_voice.mp3')

# Ask the user to select a language
langinitial("english",selectlang)
#langinitial("tamil",selectlang)
#langinitial("telugu",selectlang)
#langinitial("hindi",selectlang)
#langinitial("malayalam",selectlang)
#langinitial("gujarati",selectlang)
#langinitial("kannada",selectlang)
#langinitial("bengali",selectlang)

def takecommand():   
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        print("listening.....") 
        r.pause_threshold = 1
        audio = r.listen(source) 

    try: 
        print("Recognizing.....") 
        query = r.recognize_google(audio, language='en-in') 
        print(f"The User said {query}\n") 
    except Exception as e: 
        print("Say that again please.....") 
        query = takecommand()
    
    return query 

  
# Input from user 
# Make input to lowercase 
#query = takecommand() 
#while (query == "None"): 
 #  query = takecommand() 
  
  
def destination_language(): 
    print("Enter the language in which you \want to convert : Ex. Hindi , English , etc.") 
    print() 
      
    # Input destination language in 
    # which the user wants to translate 
    to_lang = takecommand() 
    while (to_lang == "None"): 
        to_lang = takecommand() 
    to_lang = to_lang.lower() 
    return to_lang 
  
to_lang = destination_language() 
  
# Mapping it with the code 
while (to_lang not in dic1): 
    print("Language in which you are trying \to convert is currently not available ,\please input some other language") 
    print() 
    to_lang = destination_language() 
  
to_langs = dic1[dic1.index(to_lang)+1]


def takecommands(to_langs):   
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        print("listening.....") 
        r.pause_threshold = 1
        audio = r.listen(source) 

    try: 
        print("Recognizing.....") 
        query = r.recognize_google(audio, language=to_langs) 
        print(f"The User said {query}\n") 
    except Exception as e: 
        print("Say that again please.....") 
        query = takecommands(to_langs)
    
    return query

def queries(to_langs, statement):
    translator = Translator()
    # Translating from src to dest
    text_to_translate = translator.translate(statement, dest=to_langs)
    text = text_to_translate.text
    # Using Google-Text-to-Speech ie, gTTS() method
    # to speak the translated text into the # destination language which is stored in to_lang.
    # Also, we have given 3rd argument as False because
    # by default it speaks very slowly
    speak = gTTS(text=text, lang=to_langs, slow=False)
    # Using save() method to save the translated
    # speech in capture_voice.mp3
    speak.save("captured_voice.mp3")
    # Using OS module to run the translated voice.
    playsound('captured_voice.mp3')
    os.remove('captured_voice.mp3')
    # Printing Output
    print(text) 

def transenglish(to_langs, statement):
    translator = Translator()
    # Translating from src to dest
    text_to_translate = translator.translate(statement, dest=to_langs)
    text = text_to_translate.text
    return text

def sharelocation():
    queries(to_langs, "Provide the accurate location of the issue.")
    queries(to_langs, "Are you currently at that location? Respond with yes or no.")
    queries(to_langs, "If the response is yes, I will instantly retrieve the current location using GPS, If not, please share the precise location of the problem using a map")
    confirm = takecommands(to_langs)
    queries(to_langs, confirm)
    confirm = transenglish("english", confirm)
    print(confirm)
    if confirm.lower() == "right" or "ok" or "okay" or "yes":
        queries(to_langs, "Please confirm the location?")
        confirm = takecommands(to_langs)
        queries(to_langs, confirm)
        confirm = transenglish("english", confirm)
        print(confirm)
        if confirm.lower() == "right" or "ok" or "okay" or "yes":
            queries(to_langs, "Please confirm the location?")
            queries(to_langs, "Thank you for sharing the problem")
            takeimages()
        else:
            sharelocation()
    else:
        queries(to_langs, "Are you certain about this location?")
        confirm = takecommands(to_langs)
        if confirm.lower() == "right" or "ok" or "okay" or "yes":
            confirm = takecommands(to_langs)
            queries(to_langs, confirm)
            confirm = transenglish("english", confirm)
            print(confirm)
            queries(to_langs, "Thank you for share location")
            takeimages()
        else:
            sharelocation()
                    
def takeimages():
    queries(to_langs, "Alright, could you share images related to the issue?")
    queries(to_langs, "Sure, is it possible to share images of the issue?")
    queries(to_langs, "Please respond with 'yes' or 'no.")
    confirm = takecommands(to_langs)
    queries(to_langs, confirm)
    confirm = transenglish("english", confirm)
    print(confirm)
    if confirm.lower() == "right" or "ok" or "okay" or "yes":
        queries(to_langs, "Okay, please confirm if you want to shared images related to the problem. Respond with 'yes' or 'no.'")
        confirm = takecommands(to_langs)
        queries(to_langs, confirm)
        confirm = transenglish("english", confirm)
        print(confirm)
        if confirm.lower() == "right" or "ok" or "okay" or "yes":
            endconversation()
        else:
            takeimages()
    else:
        queries(to_langs, "Alright, no problem. I will register the problem with our team to resolve the issue soon.")
        endconversation()

    
def endconversation():
    queries(to_langs, "Thank you for providing the details of the problem.")
    queries(to_langs, "Your problem has been registered,")
    queries(to_langs, "and we aim to resolve it within approximately two to three days.")
    
    
def problemstatements():
    problem = takecommands(to_langs)
    print(problem)
    queries(to_langs, problem)
    queries(to_langs, "Confirm your complaint? Say right or wrong")
    confirm = takecommands(to_langs)
    queries(to_langs, confirm)
    confirm = transenglish("english", confirm)
    print(confirm)
    if confirm.lower() == "right" or "ok":
        sharelocation()
    else:
        queries(to_langs, "Please share your correct problem?")
        problemstatements()


queries(to_langs,"hello Mithun")
queries(to_langs,"I am your friend, Please share problem?")
problemstatements()


