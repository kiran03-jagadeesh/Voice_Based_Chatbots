# Voice Based Chatbots
OpenCog is an open-source software framework for artificial general intelligence (AGI) research and development. OpenCog focuses on creating intelligent software agents that can exhibit advanced cognitive abilities, including learning, reasoning, and decision-making. It incorporates a variety of AI techniques, such as probabilistic reasoning, evolutionary learning, and natural language processing, to develop an AGI system
# Pip install
Instructions will be given to install Python 3 and Third-party Libraries using

pip install SpeechRecognition

pip install gTTS

pip install playsound==1.2.2

pip install pyinstaller (Optional: For creating executables in Windows)

pip install pyaudio(from wheel) For Python 3.10 in 64-bit Windows 


# Python Program
~~~
import speech_recognition as sr
import gtts
import random
import playsound
import webbrowser
def speak(txt):
    print(txt)
    tts=gtts.gTTS(text=txt)
    file=str(random.randint(1,10000))+".mp3"
    tts.save(file)
    playsound.playsound(file)
def listen(ask=False):    
    r=sr.Recognizer()
    r.energy_threshold=8000
    if ask:
        speak(ask)
    text=''
    try:
        with sr.Microphone() as src:
            audio=r.listen(src)
            text=r.recognize_google(audio)
    except sr.RequestError:
        print("Unable to Find the Resource")
    except sr.UnknownValueError:
        print("Unable to recognize the audio")
    return text
def respond(query):
    if query=="search" or query=="find":
        search=listen(ask="What do you want to Search?")
        url="https://www.google.com/search?q="+str(search)
        speak("your search for "+search+" is here")
        webbrowser.open(url)
    elif query=="stop" or query=="close" or query=="exit":
        speak("I am Exiting")
        exit()
while True:
    speak("How can I help You?")
    query=listen()
    respond(query)
~~~
