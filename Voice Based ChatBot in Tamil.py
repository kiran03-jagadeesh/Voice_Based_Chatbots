import speech_recognition as sr
import gtts
import time
from time import ctime
import playsound
import webbrowser
import random
import os
def record_audio(ask=False):
    r=sr.Recognizer()
    r.energy_threshold = 6000
    voicedata=''
    if ask:
        simplyspeak(ask)
    try:
        with sr.Microphone() as source:
            audio=r.listen(source)
            voicedata=r.recognize_google(audio,language='ta-IN')            
    except sr.UnknownValueError:
        print("Unable to Recognize Audio")
    except sr.RequestError:
        print("Unable to find the Resource")
    return voicedata
def simplyspeak(stringdata):
    print(stringdata)
    tts=gtts.gTTS(text=stringdata,lang='ta')
    r=random.randint(1,100000)
    audiofile="audio-"+str(r)+".mp3"
    tts.save(audiofile)
    playsound.playsound(audiofile)
    os.remove(audiofile)
def respond(query):
    s1=["என்னுடைய பெயர் என்ன","எனது பெயர் என்ன"]
    s2=["உனது பெயர் என்ன","உன்னுடைய பெயர் என்ன"]
    if  (s1[0]  in query) or (s1[1] in query):
        name=record_audio(ask="உனது பெயரை தமிழில்  உரைக்கவும்")
        simplyspeak("உனது பெயர் "+str(name))
    elif (s2[0]  in query) or (s2[1] in query):
        name="கூகிள் உதவியாளர்"
        simplyspeak("எனது பெயர் "+str(name))
    elif "முதலாளியின் பெயர் என்ன" in query:
        simplyspeak("என்னுடைய முதலாளியின் பெயர் சரவணன் நடராஜன்")
    elif "நேரம்" in query:
        simplyspeak(ctime())
    elif "தேடு" in query:
        search=record_audio(ask="என்ன தேட விரும்புகிறீர்கள்")
        url="https://google.com/search?q="+str(search)
        webbrowser.get().open(url)
        simplyspeak("நீங்கள் தேடியது இதோ")        
    elif "நிறுத்து" in query:
        simplyspeak("நான் வெளியேறுகிரேன்")
        exit()
while True:
    simplyspeak("நான் உங்களுக்கு எவ்வாறு உதவி செய்ய முடியும் ")
    query=record_audio()
    respond(query)
