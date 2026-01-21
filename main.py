import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import time

engine = pyttsx3.init("sapi5")
engine.setProperty("voice", engine.getProperty("voices")[0].id)
wikipedia.set_lang("pt")


def speak(audio):
    """
    Metodo responsável pelas falas do Bot

    :param audio: Audio que ele irá responder
    """
    engine.say(audio)
    # time.sleep(20)
    print(audio)
    engine.runAndWait()


def getCommand():
    """
    Metodo responsável por receber comandos do user
    """
    response = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        # Tempo que ele aguardará para poder ouvir o user
        response.pause_threshold = 1
        audio = response.listen(source)

        try:
            print("Reconhecendo...")
            command: str = response.recognize_google(audio, language="pt-br")
            print(f"O usuário falou: {command}\n")
            return command
        except Exception as e:
            print(e)


if __name__ == "__main__":
    isRunning: bool = True
    speak("Assistente Alex IA foi ativada!\n Como posso te ajudar?")

    while isRunning:
        command = getCommand().lower()

        if "wikipédia" in command:
            command.replace("wikipédia", "")
            command.replace("procure na", "")
            results = wikipedia.summary(command, sentences=2)
            speak(f"De acordo com a wikipédia: {results}")
        elif "finalizar" in command:
            speak("Encerrando o sistema...")
            isRunning = False
        else:
            speak("Estou te ouvindo em claro e bom tom!")
