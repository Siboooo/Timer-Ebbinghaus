import datetime
import time
import pyaudio
import wave

def playMusic(path):
    CHUNK = 1024
    wf = wave.open(path, 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)
    data = wf.readframes(CHUNK)
    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()


if __name__ == "__main__":
    p = pyaudio.PyAudio()
    print("Start lerning at ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("Start in 5 seconds.")
    time.sleep(2)
    playMusic("sound/start.wav")
    print("Start unit: 1")
    for i in range(30):
        if i%6 == 5:
            #play review sound
            playMusic("sound/changeStatus.wav")
            print("Review unit: ", i//6+1)
            for j in range(9):
                time.sleep(5.5)
                print("Next")
                playMusic("sound/dot.wav")
            time.sleep(5.5)
            if i != 29:
                print("Start unit: ", i//6+2)
                #play new unit sound
                playMusic("sound/changeStatus.wav")
        else:
            print("New word -->", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            time.sleep(29)
            playMusic("sound/learningDot.wav")
            print("New word -->", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            time.sleep(29)
            if i%6 != 4:
                playMusic("sound/learningDot.wav")
                pass
    #play end sound
    playMusic("sound/end.wav")
    print("Time out, review each list.", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    p.terminate()
