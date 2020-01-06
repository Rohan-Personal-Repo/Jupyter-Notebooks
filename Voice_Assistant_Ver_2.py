import pyttsx3
import datetime
import speech_recognition as sr

'''
pip install pyttsx3 - Recognize Voices 
pip install speechRecognition - SpeechRecognition Library
pip install PyAudio
if pyAudio does not install then
pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
'''
# sapi5 Audio Library from MS - Read more
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices, voices[0].id, "-", voices[1].id)

# Select Voice from available Options
engine.setProperty('voice', voices[1].id)

# API Keys
WIT_KEY = 'E6S7QU3VSW3VKZQEHKUZONYH5OBAIVHF'

ASSISTANT_CHOSEN = ''

# Assistant speaks
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish the user as per Hour of the day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak('Good Morning Sir')
    elif hour>=12 and hour<16:
        speak('Good Afternoon Sir')
    elif hour>=16 and hour<=22:
        speak('Good Evening Sir')
    else:
        speak('Good Night Sir')

    speak('How may I assist you today?')
'''
Take a command from the user via Microphone 
& return String Output - Speech to Text
pause_threshold - seconds of non-speaking 
audio before a phrase is considered complete

'''

def selectVendor():
    print('Recognizing Vendor')
    opt = input("Choose Vendor : Google(G) or WIT(W) - ")

    if opt.__contains__('G'):
        ASSISTANT_CHOSEN = "Google"
    elif opt.__contains__('W'):
        ASSISTANT_CHOSEN = "Wit"
    else:
        ASSISTANT_CHOSEN = "None!"

    print('You have chosen : ' + ASSISTANT_CHOSEN + " as your Assistant")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("Listening Command!")
        r.pause_threshold = 1
        audio = r.listen(src)
    try:
        print('Recognizing Command')
        if( ASSISTANT_CHOSEN.__contains__("Google")):
            print('In G')
            query = r.recognize_google(audio)
            print(f"Google said: {query}\n")
            return (query)
        elif( ASSISTANT_CHOSEN.__contains__("Wit")):
            print('In W')
            query = r.recognize_wit(audio,key=WIT_KEY)
            print(f"Wit said: {query}\n")
            return (query)
        else:
            return "Invalid"
    except Exception as e:
        # print(e.with_traceback())
        print('Repeat the command please')
        return "None"

# Main Method
if __name__ == '__main__':
    selectVendor()  # Select Vendor
    speak('Voice Assistant Initiating...')
    wishMe() #User Greeting
    while True:
        query = takeCommand().lower()
        if query.__contains__("quit"):
            break
        elif query.__contains__("invalid"):
            speak("Invalid Assistant Selected, Good Bye!")
            break