import sys
import keyboard
import speech_recognition as sr
from libs.helpy import translate_it

r = sr.Recognizer()

while True:
    try:
        if keyboard.is_pressed('0'):
            with sr.Microphone() as source:
                print("Talk!!")
                audio_text = r.listen(source)
                print("Translating...")
                try:
                    
                    text = r.recognize_google(audio_text)

                    print(f"you said: {text} \n")
                    translated_word = translate_it(text)

                    print(translated_word, '\n')
                except:
                    print("Sorry, It's not clear.")
        if keyboard.is_pressed('Esc'):
            print("\n Byee...")
            sys.exit(0)
    except:
        break
