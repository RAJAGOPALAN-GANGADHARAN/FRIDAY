import speech_recognition as sr
import sys
import voice_response
import interpret
import play_vr
def obtain_input(loc,exp,tag):
    process_id=2
    hear=""
    r = sr.Recognizer()
    with sr.AudioFile(loc) as source:
        audio = r.record(source)
    try:
        hear=r.recognize_google(audio)
        print(hear)
        if tag!=1:
            interpret.interpret(hear,exp)
        if tag==1:
            return hear
        #with open()
    except sr.UnknownValueError:
        print("------------------------------------------IDLE----------------------------------")
    except sr.RequestError as e:
        print("Could not request results from API service: {0}".format(e))
        play_vr.play_vr("no_internet.wav")
