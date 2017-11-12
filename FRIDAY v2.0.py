import sound_input
import obtain_input
from os import path
import threading
##############
##commands:close learn
##############
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "temp.wav")
#running_threads={}
exp={}

def learn():
    with open("learn.txt","r") as f:
        line=f.readlines()
        for x in line:
            temp=str(x)
            temp=temp.split(':')
            exp[temp[0]]=temp[1]
learn()
print(exp)
while 1:
    sound_input.sound_input()
    obtain_input.obtain_input(AUDIO_FILE,exp,2)

