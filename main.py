import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def processCommand(c):
    if 'open google' in c.lower():
        webbrowser.open('https://www.google.com')
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    

def speak(text):
    engine.say(text)
    engine.runAndWait()
if __name__ == "__main__":
    speak("Initializing jarvis..........")
    while True:
    #Listen for the wake word "Navis"
    #obtain audio from the microphone 
    
        r = sr.Recognizer()
        print("Recognizing")

            # recognize speech using sphinx
        try:
            with sr.Microphone() as source:
             print("Listening...")
             audio = r.listen(source , timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Haa Bhaii")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
            
        except Exception as e:
            print("Sphinx error; {0}".format(e))