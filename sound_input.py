import speech_recognition as sr
def sound_input():
    process_id=1
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)
        print("hi")
    with open("temp.wav", "wb") as f:    
        f.write(audio.get_wav_data())
        f.close()
