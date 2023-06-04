import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source, duration=1)
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
        speak(f"{query}")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('dhananjay08prajapati@gmail.com','Dh@n@n08j@y')
#     server.sendmail('dhananjay08prajapati@gmail.com',to,content)
#     server.close()

if __name__ == '__main__':
    # speak("Dhananjay is good boy")
    wishMe()
    while True:
        query = takeCommand().lower()

    # logic for excuting tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia.....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening youtube.....")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening google.....")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening youtube.....")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Dhananjay\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            print("Which code editor do you like to open sir, like visual studio or notepadd++ or sublime text editor")
            speak("Which code editor do you like to open sir, like visual studio or notepadd++ or sublime text editor")
            query1 = takeCommand().lower()
            if 'visual' in query1:
                codePath = "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            elif 'notepad' in query1:
                codePath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
                os.startfile(codePath)

            elif 'sublime' in query1:
                codePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
                os.startfile(codePath)

            # elif 'email to dhananjay' in query:
            #     try:
            #         speak("What should I say ?")
            #         content = takeCommand()
            #         to = "dhananjay08prajapati@gmail.com"
            #         sendEmail(to,content)
            #         speak("Email has been send!")
            #     except Exception as e:
            #         print(e)
            #         speak("Sorry sir, I am not able to send this email")


        elif 'exit' in query:
            exit()