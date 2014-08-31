# Standard Modules
import wave
import time
import logging

# Modules from the Interweb
import pyaudio

CHUNK = 1024

logging.basicConfig(level=logging.INFO)

class Player:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def play(self, file):
        wf = wave.open(file, 'rb')

        p = pyaudio.PyAudio()

        playStart = time.strftime("%H:%M:%S")
        self.logger.info(playStart + ": Started playing")

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(CHUNK)

        while data != '':
            stream.write(data)
            data = wf.readframes(CHUNK)

        stream.stop_stream()
        stream.close()

        playStop = time.strftime("%H:%M:%S")
        self.logger.info(playStop + ": Stopped playing")

        p.terminate()