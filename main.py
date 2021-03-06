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
import random


class person:
    name = 'Charles'

    def setName(self, name):
        self.name = name


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
        # sr.Microfone.adjust_for_ambient_noise(source) DESENVOLVER
        try:
            voice_data = recognizer.recognize_google(audio, language='pt-BR')
        except sr.UnknownValueError:
            print('sorry, i didnt get that')
            talk('sorry, i didnt get that')
        except sr.RequestError:
            print('I beg your pardom, but it seens that my speech services are down')
            talk('I beg your pardom, but it seens that my speech services are down')
        return voice_data


def respond(voice_data):
    # NAME ok
    if there_exists(["what is your name", "what's your name", "tell me your name"]):
        talk('My Name Is Glados')
    # DATE INCOMPLETO
    if there_exists(["what's the time", "tell me the time", "what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        talk(time)
    # DEFINE NOME DA PESSOA
    if there_exists(["my name is"]):
        person_name = voice_data.replace('my name is', '')
        talk("okay, i will remember that " + person_name)
        person.setName(person_name)  # remember name in person object
    # NOME DA PESSOA
    if there_exists(["what is my name"]):
        talk("Your name must be " + person.name)
    # How are you doiung
    if 'how are you doing' in voice_data:
        talk('im doing fine, im glad you asked ' + person.name)

    ####### DARKSPOOK
    if 'dark spook' in voice_data:
        talk('SHUT THE FUCK UP DARKSPOOK YOU DIRTY LITTLE JEW')

    # SEARCH IN THE WEB ok
    if 'search' in voice_data:
        talk('what you wanna search for?')
        search = record_audio('what do you want to search?')
        url = 'https://duckduckgo.com/?q=' + search
        webbrowser.get().open(url)
        talk('here is what i have found')
    # FIND LOCATION..... NOT DONE
    if 'find location' in voice_data:
        location = record_audio('where do you want to search for?')
        url = 'https://duckduckgo.com/?q=' + search
        webbrowser.get().open(url)
        print('here is what i have found')
    # MOEDA
    if there_exists(["toss", "flip", "coin"]):
        moves = ["head", "tails"]
        cmove = random.choice(moves)
        # playsound.playsound('K:\GLADOS_APRIMORADO/coin.mp3' , True)
        talk("it became " + cmove)
    # CALCULADORA
    if there_exists(["plus", "minus", "multiply", "divide", "times", "power", "+", "-", "*", "/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            talk(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            talk(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply' or 'x' or 'times':
            talk(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            talk(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            talk(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            talk("Wrong Operator")
    # MUSICA YOUTUBE ok
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
        playsound.playsound('K:\GLADOS_APRIMORADO\MP3\space22.mp3', True)
    # STUKA ok
    if 'Stuka' in voice_data:
        playsound.playsound('K:\_____ PYTHON ______\GLADOS_APRIMORADO\stuka.mp3', True)
    # WIKIPEDIA ok
    if 'who is' in voice_data:
        whois = voice_data.replace('who is', '')
        informacaopessoa = wikipedia.summary(whois, 2)
        talk(informacaopessoa)
    # WHERE AM I
    if 'where am I' in voice_data:
        g = geocoder.ip('me')
        print(g.lat)
        print(g.lng)
        lati = g.lat
        long = g.lng
        ondeestou = wikipedia.geosearch(lati, long, None, 3)
        talk(ondeestou)
    # EXIT ok
    if 'exit' in voice_data:
        exit()
    else:
        talk('hmmm. didnt get that, can you say it again?')


time.sleep(1)
talk('How can i be of service')
print('listening')
while 1:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)

#   .''.
#  (~~~~)
#    ||
#  __||__
# /______\
#   |  |' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
#   |  |'|o| - - - - - - - - - - - - - - - - - - - - - - - - -||
#   |  |'| |                                                  ||
#   |  |'| |                      . ' .                       ||
#   |  |'| |                  . '       ' .                   ||
#   |  |'| |              . '    .-'"'-.    ' .               ||
#   |  |'| |          . '      ,"______ ".      ' .           ||
#   |  |'| |      . '        /:  \     |  :\        ' .       ||
#   |  |'| |  . '            ;  . \        ;            ' .   ||
#   |  |'| |    ' .          \: . /       :/          . '     ||
#   |  |'| |        ' .        `./_____| ,/       . '         ||
#   |  |'| |            ' .      `-.,,.-'     . '             ||
#   |  |'| |                ' .           . '                 ||
#   |  |'| |                    ' .   . '                     ||
#   |  |'| |                        '                         ||
#   |  |'|o|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_||
#   |  |'
#   |  |'           BRASIL ACIMA DE TUDO
#   |  |'                  DEUS ACIMA DE TODOS
#   |  |'           MORTE AO COMUNISMO
#   |  |'                  GLORIA AO INTEGRALISMO
