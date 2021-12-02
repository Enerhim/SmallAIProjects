import speech_recognition as sr

def GetAudio(time = 4):
    r = sr.Recognizer()

    mic = sr.Microphone()

    with mic as source:
        audio = r.listen(source, phrase_time_limit = time)
        
        try:
            text = r.recognize_google(audio)
            # print(text)
            return (text)
        except sr.UnknownValueError: 
            # print("")
            return None
        except sr.RequestError: 
            # print("")
            return None
        except:
            # print(stop" ")
            return None