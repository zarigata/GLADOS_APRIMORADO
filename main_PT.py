import webbrowser
from time import ctime
import time
import pyttsx3
import speech_recognition as sr
import pyjokes
import playsound
#import pywhatkit
import os
import wikipedia
import geocoder
import random

#=============================================================
# vozes de utilizacao
pt_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0"
en_m_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
#=============================================================


class person:
    name = 'Carlos'

    def setName(self, name):
        self.name = name


############################################
recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', pt_voice_id)

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
            voice_data = recognizer.recognize_google(audio, language='pt-BR') # RECONHECIMENTO DE VOZ, FAZER VARIAVEL QUE PODE MUDAR A LINGUA?
        except sr.UnknownValueError:
            print('perdao, nao entendi')
            talk('perdao, nao entendi')
        except sr.RequestError:
            print('pesso desculpas, mas parece que voce esta sem internet, por favor verifique que a internet esta funcionando')
            talk('pesso desculpas, mas parece que voce esta sem internet, por favor verifique que a internet esta funcionando')
        return voice_data


def respond(voice_data):



    # NAME ok
    if there_exists(["qual é o seu nome", "como voce se chama", "me diga seu nome","como se chama","seu nome","nome"]):
        talk('me chamo Glados')


    # DATE INCOMPLETO
    if there_exists(["que horas sao", "me fala que horas sao", "qual sao as horas"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        talk(time)


    # DEFINE NOME DA PESSOA
    if there_exists(["meu nome e"]):
        person_name = voice_data.replace('meu nome e', '')
        talk("okei, irei lembrar disso " + person_name)
        person.setName(person_name)  # remember name in person object


    # NOME DA PESSOA
    if there_exists(["qual e meu nome"]):
        talk("qual e meu nome" + person.name)
    # How are you doiung
    if 'como você está' in voice_data:
        talk('Estou operacional ' + person.name)



    ####### DARKSPOOK
    if 'dark spook' in voice_data:
        talk('SHUT THE FUCK UP DARKSPOOK YOU DIRTY LITTLE JEW')

    # SEARCH IN THE WEB ok
    if 'procurar' in voice_data:
        talk('o que voce quer procurar?')
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
    if there_exists(["jogar moeda", "cara ou coroa", "atirar moeda"]):
        moves = ["Cara", "Coroa"]
        cmove = random.choice(moves)
        playsound.playsound('MP3/coin.mp3' , True)
        talk("sua moeda foi" + cmove)
    # CALCULADORA
    if there_exists(["mais", "menos", "multiplicar", "dividir", "vezes", "elevado", "+", "-", "*", "/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            talk(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            talk(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiplicar' or 'x' or 'vezes':
            talk(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'dividir':
            talk(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'elevado':
            talk(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            talk("Operador Errado")
    # MUSICA YOUTUBE ok
    if 'tocar' in voice_data:
        ytmusic = voice_data.replace('tocar', '')
        talk('tocando' + ytmusic + 'no youtube')
        # print('music on youtube')
        pywhatkit.playonyt(ytmusic)


    # JOKE NAO PARA PORTUGUES
    #if 'tell me a joke' in voice_data:
    #    talk(pyjokes.get_joke())


    # SPACE ok
    if 'space' in voice_data:
        playsound.playsound('K:\GLADOS_APRIMORADO\MP3\space22.mp3', True)
    # STUKA ok
    if 'Stuka' in voice_data:
        playsound.playsound('K:\PROJETOS PYTHON/stuka.mp3', True)
    # WIKIPEDIA ok
    if 'quem é' in voice_data:
        whois = voice_data.replace('quem é', '')
        wikipedia.set_lang("pt")
        informacaopessoa = wikipedia.summary(whois, 2)
        talk(informacaopessoa)
    # WHERE AM I
    if there_exists(["aonde eu estou", "qual minha posicao", "qual minha localizacao atual", "onde estou?"]):
        g = geocoder.ip('me')
        print(g.lat)
        print(g.lng)
        lati = g.lat
        long = g.lng
        ondeestou = wikipedia.geosearch(lati, long, None, 3)
        talk(ondeestou)

     # COMPRAR NA INTERNET
    if there_exists(["quero comprar", "quero comprar uma ", "comprar"]):
        talk("okei, aqui estao os resultados")
        merlivre = voice_data.replace('quero comprar', '')
        compra = 'https://lista.mercadolivre.com.br/' + merlivre
        webbrowser.get().open(compra)

    # EXIT ok
    if 'sair' in voice_data:
        exit()
    else:
        talk('Hmm, nao entendi, pode repetir por favor?')


time.sleep(1)
playsound.playsound('MP3/pinga.mp3' , True)
talk('Como posso ser de ajuda a você?')
print('Ouvindo')

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
#   |  |'                  GLORIA AO BRASIL
