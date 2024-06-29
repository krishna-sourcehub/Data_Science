

import asyncio
import os

import aiohttp
import pygame
import requests
import speech_recognition as sr
import streamlit as st
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
from streamlit_chat import message

dic = {
    'English': 'en',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Hindi': 'hi',
    'Malayalam': 'ml',
    'Gujarati': 'gu',
    'Kannada': 'kn',
    'Bengali': 'bn',
}

# Define the URL of the Flask backend API
API_URL = "http://127.0.0.1:5000/chat"  # Replace with your Flask backend URL

def refresh_conversation_history():
    # Send a GET request to the backend API to refresh the conversation history
    response = requests.get(API_URL, params={"refresh": "true"})

    # Check the response status
    if response.status_code == 200:
        data = response.json()
        # Reset session state messages
        st.session_state.messages = [{"role": "system", "content": data["response"]}]
        st.success("Conversation history cleared.")
    else:
        st.error("Failed to refresh the conversation history.")
        
# Define an asynchronous function to get a response from the Flask backend API
async def get_chatbot_response(query):
    # Create an asynchronous HTTP client session
    async with aiohttp.ClientSession() as session:
        # Send a GET request to the backend API with the query parameter
        params = {"query": query}
        try:
            async with session.get(API_URL, params=params) as response:
                # Check if the request was successful (HTTP status code 200)
                if response.status == 200:
                    # Parse the JSON response
                    data = await response.json()
                    # Get the chatbot's response from the JSON data
                    chatbot_response = data.get("response")
                    return chatbot_response
                else:
                    # Log an error if the request was not successful
                    print(f"Failed to get a response. HTTP status code: {response.status}")
                    return None
        except Exception as e:
            # Log any exceptions that occur during the request
            print(f"An error occurred while requesting the API: {e}")
            return None

# Initialize Streamlit page configuration
def init():
    st.set_page_config(
        page_title="Makkal Thunaivan Chatbot",
        page_icon="🤖"
    )





flag = 0
# to_lang=None 
# to_langs=None

if "messages" not in st.session_state:
        # Add a system message to the conversation history
        st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]
selectlang = "say your preferred language"
# st.session_state.messages.append({"role": "assistant", "content": selectlang})
# Initialize Streamlit session state

def init():
    st.set_page_config(
        page_title="Makkal Thunaivan Chatbot",
        page_icon="🤖"
    )
    
    # Add a system message to the conversation history
    
# to_lang="english"
response=None

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








def queries(to_langs, statement):
    translator = Translator()
    # Translating from src to dest
    text_to_translate = translator.translate(statement, dest=to_langs)
    print("queries language",to_langs)
    text = text_to_translate.text
    return text 

def voice(text, to_langs):
    if text!="":
        speak = gTTS(text=text, lang=to_langs, slow=False)
        # Save the translated speech in 'capture_voice.mp3'.
        speak.save("captured_voice.mp3")
        # Initialize pygame mixer
        pygame.mixer.init()
        # Load and play the audio
        pygame.mixer.music.load("captured_voice.mp3")
        pygame.mixer.music.play()
        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        # Clean up pygame mixer
        pygame.mixer.quit()

        # Remove the MP3 file if desired
        os.remove('captured_voice.mp3')

        # Print the output
        print(text)

def transenglish(to_langs, statement):
    translator = Translator()
    # Translating from src to dest
    text_to_translate = translator.translate(statement, dest=to_langs)
    text = text_to_translate.text
    return text


def get_voice_input(to_langs):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        with st.spinner("Listening..."):
            r.pause_threshold = 1
            audio_data = r.listen(source)
        try:
            # Convert voice input to text
            query = r.recognize_google(audio_data, language=to_langs)
            print(query)
            return query
        except sr.UnknownValueError:
            st.write("Sorry, I did not understand your voice input.")

            return None
        except sr.RequestError as e:
            st.write(f"Could not request results; {e}")
            return None
        


# Main function
async def main():
    # Initialize the Streamlit app configuration
    init()
    text = ""

    # Initialize message history
    if "messages" not in st.session_state:
        # Add a system message to the conversation history
        st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

    # Set the header for the Streamlit app
    st.header("Makkal Thunaivan Chatbot 🤖")
    
    

    # Sidebar with user input
    with st.sidebar:
        user_input = st.text_input("Your message: ", key="user_input")

        selected_language = st.selectbox("Select language:", list(dic.keys()))
        print(selected_language)
        if selected_language =="english":
            to_lang="en"
        if selected_language =="tamil":
            to_lang="ta"
        if selected_language =="telugu":
            to_lang="te"
        if selected_language =="hindi":
            to_lang="hi"
        if selected_language =="malayalam":
            to_lang="ml"
        if selected_language =="kannada":
            to_lang="ta"
        if selected_language =="gujarati":
            to_lang="kn"
        if selected_language =="bengali":
            to_lang="bn"

        to_langs = to_lang
        
        
        # Store the selected language code in session state
        st.session_state.language_code = dic[selected_language]
        
        # Refresh button to clear the conversation history
        if st.button("Refresh"):
            refresh_conversation_history()
        
        if st.button("Speak"):
            user_input = get_voice_input(to_langs)
            if user_input:
                # Add the user's input to the conversation history
                print(user_input)
                # st.session_state.messages.append({"role": "user", "content": user_input})
                
        # Handle user input
        if user_input:
            user_input=queries(to_langs, user_input)
            st.session_state.messages.append({"role": "user", "content": user_input})
            user_input=transenglish("english", user_input)
            print(user_input)
            # Add the user's input to the conversation history
            

            # Make an asynchronous request to the Flask backend API
            with st.spinner("Thinking..."):
                print(user_input)
                response = await get_chatbot_response(user_input)

            # Add the AI's response to the conversation history
            if response:
                text=queries(to_lang, response)
                st.session_state.messages.append({"role": "assistant", "content": text})
                
                

            # Display message history
    messages = st.session_state.messages
    for i, msg in enumerate(messages[1:]):
        if msg["role"] == "user":
            message(msg["content"], is_user=True, key=f"user_{i}")
        else:
            message(msg["content"], is_user=False, key=f"bot_{i}")
    with st.spinner("Speaking..."):
        voice(text, to_langs)
        # print(response)
            

# Run the Streamlit app
if __name__ == "__main__":
    asyncio.run(main())
    
    
