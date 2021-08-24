import webbrowser
from time import ctime
import time
import pyttsx3
import speech_recognition as sr
import pyjokes
import playsound
import pywhatkit
import os
import wikipedia
import geocoder




############################################
recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


###########################################

def talk(text):
    engine.say(text)
    engine.runAndWait()

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = recognizer.listen(source)
        try:
            voice_data = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print('sorry, i didnt get that')
            talk('sorry, i didnt get that')
        except sr.RequestError:
            print('I beg your pardom, but it seens that my speech services are down')
            talk('I beg your pardom, but it seens that my speech services are down')
        return voice_data


def respond(voice_data):
    # NAME ok
    if there_exists(["what is your name","what's your name","tell me your name"]):
        talk('My Name Is Glados')
    # DATE INCOMPLETO
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        talk(time)
    # SEARCH IN THE WEB ok
    if 'search' in voice_data:
        search = record_audio('what do you want to search?')
        talk('what you wanna search for?')
        url = 'https://duckduckgo.com/?q=' + search
        webbrowser.get().open(url)
        print('here is what i have found')
        talk('here is what i have found')
    # FIND LOCATION..... NOT DONE
    if 'find location' in voice_data:
        location = record_audio('where do you want to search for?')
        url = 'https://duckduckgo.com/?q=' + search
        webbrowser.get().open(url)
        print('here is what i have found')
    #MUSICA YOUTUBE ok
    if 'play' in voice_data:
        ytmusic = voice_data.replace('play', '')
        talk('playing' + ytmusic + 'on youtube')
        # print('music on youtube')
        pywhatkit.playonyt(ytmusic)
    # JOKE ok
    if 'tell me a joke' in voice_data:
        talk(pyjokes.get_joke())
    # SPACE ok
    if 'space' in voice_data:
        playsound.playsound('K:\PROJETOS PYTHON/space22.mp3', True)
    #STUKA ok
    if 'Stuka' in voice_data:
        playsound.playsound('K:\PROJETOS PYTHON/stuka.mp3', True)
    #WIKIPEDIA ok
    if 'who is' in voice_data:
        whois=voice_data.replace('who is' , '')
        informacaopessoa = wikipedia.summary(whois , 2)
        talk(informacaopessoa)
    if 'where am I' in voice_data:
        g = geocoder.ip('me')
        print(g.lat)
        print(g.lng)
        lati = g.lat
        long = g.lng
        ondeestou = wikipedia.geosearch(lati, long,None,3)
        talk(ondeestou)
    # EXIT ok
    if 'exit' in voice_data:
        exit()


time.sleep(1)
talk('How can i be of service')
print('listening')
while 1:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)






#  .''.
# (~~~~)
#   ||
# __||__
#/______\
#  |  |' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
#  |  |'|o| - - - - - - - - - - - - - - - - - - - - - - - - -||
#  |  |'| |                                                  ||
#  |  |'| |                      . ' .                       ||
#  |  |'| |                  . '       ' .                   ||
#  |  |'| |              . '    .-'"'-.    ' .               ||
#  |  |'| |          . '      ,"______ ".      ' .           ||
#  |  |'| |      . '        /:  \     |  :\        ' .       ||
#  |  |'| |  . '            ;  . \        ;            ' .   ||
#  |  |'| |    ' .          \: . /       :/          . '     ||
#  |  |'| |        ' .        `./_____| ,/       . '         ||
#  |  |'| |            ' .      `-.,,.-'     . '             ||
#  |  |'| |                ' .           . '                 ||
#  |  |'| |                    ' .   . '                     ||
#  |  |'| |                        '                         ||
#  |  |'|o|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_||
#  |  |'
#  |  |'           BRASIL ACIMA DE TUDO
#  |  |'                  DEUS ACIMA DE TODOS
#  |  |