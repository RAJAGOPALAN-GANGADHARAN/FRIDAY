from gtts import gTTS
import play_vr
def voice_response(text):
    process_id=3
    vr=(text)
    tts=gTTS(text=vr,lang='en-us')        
    tts.save("speech.wav")
    play_vr.play_vr("speech.wav")
def voice_response1(text,name):
    process_id=3
    vr=(text)
    tts=gTTS(text=vr,lang='en-us')        
    tts.save(name+".wav")
    play_vr.play_vr(name+".wav")

