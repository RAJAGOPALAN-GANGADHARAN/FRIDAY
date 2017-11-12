##################
##FRIDAY                  \
##VOICE ASSISTANT \
##################


##########################################
##plan                                            
##1.create gui
##2.read input through mic using pyaudio and stuff
##3.reply using gtts
##4.perform the stuff//talk to me learns expressions control remote
##########################################
import pygame
import speech_recognition as sr
import time
import tkinter
import os
from os import path
from play_vr import play_vr
import threading
from gtts import gTTS
#from appium import webdriver
import soundfile as sf
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "temp.wav")

running_threads=[]
'''
class remote:
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['noReset']=True
        desired_caps['fullReset']=False
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'redmi'
        desired_caps['appPackage'] = 'com.duokan.phone.remotecontroller'
        desired_caps['appActivity'] = 'com.xiaomi.mitv.phone.remotecontroller.HoriWidgetMainActivityV2'
        desired_caps['appWaitActivity'] = 'com.xiaomi.mitv.phone.remotecontroller.HomeActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        elmnt = self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index=1]")
        elmnt.click()
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
 
    def instruct(self,string):
        if string=='volume up':
            singles = self.driver.find_element_by_id('com.duokan.phone.remotecontroller:id/btn_volume_up')
            singles.click()
        elif string=='channel down':
            singles = self.driver.find_element_by_id('com.duokan.phone.remotecontroller:id/btn_channel_up')
            singles.click()


'''
class GUI:
    def main_window(self):
        self.window=tkinter.Tk()
        self.window.geometry("500x100")
        self.window.title("FRIDAY")
    def Entry_box(self):
        self.bar1=tkinter.Entry(self.window,width=80)
        self.bar1.place(x=10,y=10)
    def draw(self):
        self.main_window()
        self.Entry_box()
        self.window.mainloop()


class sound_input:
    def main(self):
        self.r = sr.Recognizer()
        with sr.Microphone() as self.source:
            print("Say something!")
            self.audio = self.r.listen(self.source)
            print("I heard what you said")
        with open("temp.wav", "wb") as self.f:
            self.f.write(self.audio.get_wav_data())
            self.f.close()

class process_input_using_api:
    def main(self,loc,b,run):
        self.hear=""
        self.r = sr.Recognizer()
        with sr.AudioFile(loc) as self.source:
            self.audio = self.r.record(self.source)
        try:
            self.hear=self.r.recognize_google(self.audio)
            b.insert(0, self.hear )
            print(self.hear)
            return True            
        except sr.UnknownValueError:
            print("FRIDAY could not understand your command")
            return True
        except sr.RequestError as e:
            print("Could not request results from API service; {0}".format(e))
class voice_response:
    def main(self,text):
        self.vr=(text)
        self.tts=gTTS(text=self.vr,lang='en-us')        
        self.tts.save(r"english.wav")
##    
##class play_vr:
##    def main(self):
##        pygame.mixer.init()
##        pygame.mixer.music.load(open("D:\english.wav","rb"))
##        pygame.mixer.music.play()
##        while pygame.mixer.music.get_busy():
##            time.sleep(1)
            
window=GUI()
def hi(x):
    print(x)
def listen():
    run=True
    while run:
        si1=sound_input()
        si1.main()  
        pi1=process_input_using_api()
        run=pi1.main(AUDIO_FILE,window.bar1,run)
        vi1=voice_response()
        vi1.main(pi1.hear)
        pv1=play_vr('english.wav')
thread1=threading.Thread(target=window.draw)
thread2=threading.Thread(target=listen)
thread3=threading.Thread(target=hi,args=(1,))
thread1.start()
thread2.start()
thread3.start()


