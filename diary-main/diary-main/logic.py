import speech_recognition as sr

def speach_en():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        pass

def speach_ru():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        
        return r.recognize_google(audio, language='ru-RU')
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        pass