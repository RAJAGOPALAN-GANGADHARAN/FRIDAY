import play_vr
import voice_response
import learning_module
import sys
def interpret(hear,exp):
    if hear=='close':
        play_vr.play_vr("goodbye.wav")
        sys.exit()
    elif hear in exp:
        voice_response.voice_response(exp[hear])
    elif hear=='learn':
        play_vr.play_vr("start learn.wav")
        play_vr.play_vr("teach stuff.wav")
        learning_module.main(exp)
    else:
        print("Can you repeat it clearly")
        voice_response.voice_response("Can you repeat it clearly")

