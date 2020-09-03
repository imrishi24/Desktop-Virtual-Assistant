import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning!!")

    elif hour >=12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("sir I am Jarvis How may I help you?")

def takecommand():
    '''It takes microphone from the user and returns string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        print("Listening...")
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'passwd')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
        
if __name__ == "__main__":
    wishme()
    while True:
        query=takecommand().lower()
         
         # logic to execute tasks

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            Query=query.replace("wikipedia","")
            result=wikipedia.summary(Query,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            speak("Sure opening youtube now")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Sure opening google now")
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            speak("Sure opening stack overflow now")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Lenovo\\Music'
            songs = os.listdir(music_dir)
            # print(songs)    
            speak("Playing music now")
            os.startfile(os.path.join(music_dir, songs[random.randint(0,len(music_dir))]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("Opening code")
            codePath = "C:\\Users\\Lenovo\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            speak("Sure opening chrome now")
            codePath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            os.startfile(codePath)

        elif 'email to rishi' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "sender_email@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry baby. I am not able to send this email")
        elif "love you" in query:
            speak("I love you too..")

        elif 'exit' in query:
            speak("Thank you sir, Have a good day..")
            exit()