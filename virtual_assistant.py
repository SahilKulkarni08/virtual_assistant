import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import os
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sahil!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sahil!")

    else:
        speak("Good Evening sahil!")

    speak("I am Alpha. Please tell me how may I help you")
def takecommand():
     r=sr.Recognizer()
     with sr.Microphone() as source:
         print("listening..")
         r.pause_threshold=1
         audio=r.listen(source)
     try:
         print("recognising...")
         query=r.recognize_google(audio,language='en-in')
         print(f"User said: {query}\n")
     except Exception as e:
         print("say that again")
         return "None"
     return query
if __name__ == '__main__':
   wishme()
   while True:
      query=takecommand().lower()
      if 'wikipedia' in query:
          speak('searching wikipedia...')
          query=query.replace('wikipedia',"")
          results=wikipedia.summary(query,sentences=2)
          speak("according to wikipedia")
          speak(results)

      elif 'play my favourite song' in query:
          webbrowser.open("https://www.youtube.com/watch?v=0kFGbZ9KrlI")

      elif ' open google' in query:
          webbrowser.open("google.com")

      elif 'open stackoverflow' in query:
          webbrowser.open("stackoverflow.com")


      elif 'open youtube' in query:
          webbrowser.open("youtube.com")

      elif 'play music' in query:
          music_dir='C:\\sahil\\New folder'
          songs=os.listdir(music_dir)
          os.startfile(os.path.join(music_dir,songs[1]))

      elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Sir, the time is {strTime}")
          print(strTime)

      elif 'open vs' in query:
          codePath = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(codePath)