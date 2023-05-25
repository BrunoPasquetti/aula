# instalação: SpeechRecognition e PyAudio 
# para Pyaudio, digite no google "install pyaudio se_sistema_operacional"

import speech_recognition as sr 

#recognizer 
#microphone 
rec = sr.Recognizer ()
#print(sr.Microphone(). list_microphone_names()) #para descobrir qual microfone usar 
with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print(" pode falar que eu que eu vou grava")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
    
