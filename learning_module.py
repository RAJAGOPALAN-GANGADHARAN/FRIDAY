import sound_input
from os import path
import obtain_input 
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "temp.wav")
def main(exp):
    sound_input.sound_input()
    temp=obtain_input.obtain_input(AUDIO_FILE,exp,1)
    print(temp)
    try:
        temp=temp[3:].split("then")
    except TypeError:
        print("learning mode closed")
    print(temp)
    temp=":".join(temp)
    temp.insert(0,":")
    print(temp)
    f=open("learn.txt","a")
    
     
