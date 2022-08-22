import os
from plyer import notification
import time
import threading
from gtts import gTTS
from playsound import playsound
import schedule

def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="imagens/icopng.ico",
        timeout=2,
    )
def buscaTarefaDataHora():
    while True:
        with open("listaTarefa.txt","r",encoding="utf-8") as listaTarefatxt:
            dtAtual = time.strftime("%d/%m/%Y", time.localtime())
            hrAtual = time.strftime("%H:%M", time.localtime())
            for tarefa in listaTarefatxt:
                # busca tarefa por data e hora
                if dtAtual + hrAtual in tarefa.split(";")[2] + tarefa.split(";")[3]:
                    if __name__ == '__main__':
                        for repeticao in range(2):
                            notifyMe(tarefa.split(";")[0], tarefa.split(";")[5])
                            audio = "audiosAssistente/audio_DeH.mp3"
                            language = "pt-br"
                            sp = gTTS(text= "Alerta agendado" +"/.../"+ tarefa.split(";")[0] +"/.../"+ tarefa.split(";")[5], lang=language)
                            sp.save(audio)
                            playsound(audio)
                            time.sleep(29)
                            os.remove(audio)
def tarefaTodoDia():
    while True:
        with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefatxt:
            hrAtual = time.strftime("%H:%M", time.localtime())
            for tarefa in listaTarefatxt:
                # busca tarefa agendada todos os dias no horário marcado
                if hrAtual + "8" in tarefa.split(";")[3] + tarefa.split(";")[4]:
                    if __name__ == '__main__':
                        for repeticao in range(2):
                            notifyMe(tarefa.split(";")[0], tarefa.split(";")[5])
                            audio = "audiosAssistente/audio_td.mp3"
                            language = "pt-br"
                            sp = gTTS(text= "Alerta diário" +"/.../"+ tarefa.split(";")[0] +"/.../"+ tarefa.split(";")[5], lang=language)
                            sp.save(audio)
                            playsound(audio)
                            time.sleep(29)
                            os.remove(audio)
def tarefaTodoDomingo():
    while True:
        with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefatxt:
            hrAtual = time.strftime("%H:%M", time.localtime())
            diaSemanaAtual = time.strftime("%w", time.localtime())
            if diaSemanaAtual == "0":
                for tarefa in listaTarefatxt:
                    # busca tarefa agendada todos os dias no horário marcado
                    if hrAtual + "1" in tarefa.split(";")[3] + tarefa.split(";")[4]:
                        if __name__ == '__main__':
                            for repeticao in range(2):
                                notifyMe(tarefa.split(";")[0], tarefa.split(";")[5])
                                audio = "audiosAssistente/audio_td_1.mp3"
                                language = "pt-br"
                                sp = gTTS(text= "Alerta" +"/.../"+ tarefa.split(";")[0] +"/.../"+ tarefa.split(";")[5], lang=language)
                                sp.save(audio)
                                playsound(audio)
                                time.sleep(29)
                                os.remove(audio)
def tarefaTodaSegunda():
    while True:
        with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefatxt:
            hrAtual = time.strftime("%H:%M", time.localtime())
            diaSemanaAtual = time.strftime("%w", time.localtime())
            if diaSemanaAtual == "1":
                for tarefa in listaTarefatxt:
                    # busca tarefa agendada todos os dias no horário marcado
                    if hrAtual + "2" in tarefa.split(";")[3] + tarefa.split(";")[4]:
                        if __name__ == '__main__':
                            for repeticao in range(2):
                                notifyMe(tarefa.split(";")[0], tarefa.split(";")[5])
                                audio = "audiosAssistente/audio_td_2.mp3"
                                language = "pt-br"
                                sp = gTTS(text= "Alerta" +"/.../"+ tarefa.split(";")[0] +"/.../"+ tarefa.split(";")[5], lang=language)
                                sp.save(audio)
                                playsound(audio)
                                time.sleep(29)
                                os.remove(audio)
def tarefaTodaTerca():
    while True:
        with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefatxt:
            hrAtual = time.strftime("%H:%M", time.localtime())
            diaSemanaAtual = time.strftime("%w", time.localtime())
            if diaSemanaAtual == "2":
                for tarefa in listaTarefatxt:
                    # busca tarefa agendada todos os dias no horário marcado
                    if hrAtual + "3" in tarefa.split(";")[3] + tarefa.split(";")[4]:
                        if __name__ == '__main__':
                            for repeticao in range(2):
                                notifyMe(tarefa.split(";")[0], tarefa.split(";")[5])
                                audio = "audiosAssistente/audio_td_3.mp3"
                                language = "pt-br"
                                sp = gTTS(text= "Alerta" +"/.../"+ tarefa.split(";")[0] +"/.../"+ tarefa.split(";")[5], lang=language)
                                sp.save(audio)
                                playsound(audio)
                                time.sleep(29)
                                os.remove(audio)
def tarefaTodaQuarta():
    while True:
        with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefatxt:
            hrAtual = time.strftime("%H:%M", time.localtime())
            diaSemanaAtual = time.strftime("%w", time.localtime())
            if diaSemanaAtual == "3":
                for tarefa in listaTarefatxt:
                    # busca tarefa agendada todos os dias no horário marcado
                    if hrAtual + "4" in tarefa.split(";")[3] + tarefa.split(";")[4]:
                        if __name__ == '__main__':
                            for repeticao in range(2):
                                notifyMe(tarefa.split(";")[0], tarefa.split(";")[5])
                                audio = "audiosAssistente/audio_td_4.mp3"
                                language = "pt-br"
                                sp = gTTS(text= "Alerta" +"/.../"+ tarefa.split(";")[0] +"/.../"+ tarefa.split(";")[5], lang=language)
                                sp.save(audio)
                                playsound(audio)
                                time.sleep(29)
                                os.remove(audio)
def tarefaTodaQuinta():
    while True:
        with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefatxt:
            hrAtual = time.strftime("%H:%M", time.localtime())
            diaSemanaAtual = time.strftime("%w", time.localtime())
            if diaSemanaAtual == "4":
                for tarefa in listaTarefatxt:
                    # busca tarefa agendada todos os dias no horário marcado
                    if hrAtual + "5" in tarefa.split(";")[3] + tarefa.split(";")[4]:
                        if __name__ == '__main__':
                            for repeticao in range(2):
                                notifyMe(tarefa.split(";")[0], tarefa.split(";")[5])
                                audio = "audiosAssistente/audio_td_5.mp3"
                                language = "pt-br"
                                sp = gTTS(text= "Alerta" +"/.../"+ tarefa.split(";")[0] +"/.../"+ tarefa.split(";")[5], lang=language)
                                sp.save(audio)
                                playsound(audio)
                                time.sleep(29)
                                os.remove(audio)
def tarefaTodaSexta():
    while True:
        with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefatxt:
            hrAtual = time.strftime("%H:%M", time.localtime())
            diaSemanaAtual = time.strftime("%w", time.localtime())
            if diaSemanaAtual == "5":
                for tarefa in listaTarefatxt:
                    # busca tarefa agendada todos os dias no horário marcado
                    if hrAtual + "6" in tarefa.split(";")[3] + tarefa.split(";")[4]:
                        if __name__ == '__main__':
                            for repeticao in range(2):
                                notifyMe(tarefa.split(";")[0], tarefa.split(";")[5])
                                audio = "audiosAssistente/audio_td_6.mp3"
                                language = "pt-br"
                                sp = gTTS(text= "Alerta" +"/.../"+ tarefa.split(";")[0] +"/.../"+ tarefa.split(";")[5], lang=language)
                                sp.save(audio)
                                playsound(audio)
                                time.sleep(29)
                                os.remove(audio)
def tarefaTodoSabado():
    while True:
        with open("listaTarefa.txt", "r", encoding="utf-8") as listaTarefatxt:
            hrAtual = time.strftime("%H:%M", time.localtime())
            diaSemanaAtual = time.strftime("%w", time.localtime())
            if diaSemanaAtual == "6":
                for tarefa in listaTarefatxt:
                    # busca tarefa agendada todos os dias no horário marcado
                    if hrAtual + "7" in tarefa.split(";")[3] + tarefa.split(";")[4]:
                        if __name__ == '__main__':
                            for repeticao in range(2):
                                notifyMe(tarefa.split(";")[0], tarefa.split(";")[5])
                                audio = "audiosAssistente/audio_td_7.mp3"
                                language = "pt-br"
                                sp = gTTS(text= "Alerta" +"/.../"+ tarefa.split(";")[0] +"/.../"+ tarefa.split(";")[5], lang=language)
                                sp.save(audio)
                                playsound(audio)
                                time.sleep(29)
                                os.remove(audio)

threading.Thread(target=buscaTarefaDataHora).start()
time.sleep(1)
threading.Thread(target=tarefaTodoDia).start()
time.sleep(1)
threading.Thread(target=tarefaTodoDomingo).start()
time.sleep(1)
threading.Thread(target=tarefaTodaSegunda).start()
time.sleep(1)
threading.Thread(target=tarefaTodaTerca).start()
time.sleep(1)
threading.Thread(target=tarefaTodaQuarta).start()
time.sleep(1)
threading.Thread(target=tarefaTodaQuinta).start()
time.sleep(1)
threading.Thread(target=tarefaTodaSexta).start()
time.sleep(1)
threading.Thread(target=tarefaTodoSabado()).start()
time.sleep(1)
