import pyaudio
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as sourse:
        microfone.adjust_for_ambient_noise(sourse)
        audio = "audiosAssistente/audio_aguradandoComando.mp3"
        language = "pt-br"
        sp = gTTS(text="Aguardando comando.. ", lang=language)
        sp.save(audio)
        playsound(audio)
        os.remove(audio)
        print("Aguardando comando.. ")
        comandoDeVoz = microfone.listen(source)
    try:
        retornoDoComandoDeVoz = microfone.recognize_google(comandoDeVoz,languege="pt-BR")
        print(f'Você disse: {retornoDoComandoDeVoz}')

    except sr.UnkownValueError:
        print(f'Não entendi o que disse, repita o comando por favor!')

    return retornoDoComandoDeVoz

ouvir_microfone()