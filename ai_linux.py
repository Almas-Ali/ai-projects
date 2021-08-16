import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os

engine = pyttsx3.init('espeak')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[16].id)
engine.setProperty('rate', 150)


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')


greetMe()

speak('Hello Sir, I am Artificial Intelegence Emo!')
speak('How may I help you ?')


def myCommand():

    r = sr.Recognizer()
    r.energy_threshold = 100
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-us')
        print(f'User: {query}\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = myCommand().lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.com')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('mail.google.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing, sir!', 'I am fine, sir!',
                      'Nice, sir!', 'I am nice and full of energy, sir!']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username',
                                    "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')

        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'bye' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            break

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'play music' in query:
            music_folder = '/media/almas/01D7255C662DDE60/Phone_data/My Music/'
            music = ['Hui Malang - Malang 320 Kbps.mp3',
                     'Mujhko Barsaat Bana Lo Full Song with Lyrics _ Junooniyat _ Pulkit Samrat_ Yami Gautam _ T-Series(MP3_160K).mp3', 'Ab_Na_Phir_Se_-_Lyrical_Hacked_Hina_Khan.mp3', 'Tujhe_Hasil_Karunga_Hacker_movie_official_song_out_now_must_watch(256kbps).mp3']

            random_music = os.path.join(music_folder, random.choice(music))
            os.system(f'vlc {random_music}')

            speak('Okay, here is your music! Enjoy!')

        else:
            query = query
            print('Searching...')
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Sir!')
