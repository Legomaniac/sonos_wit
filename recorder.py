# Standard Modules
import time
import wave
from StringIO import StringIO
# Modules from the Interweb
import pyaudio

# PyAudio settings
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

class Recorder:

    def __init__(self, seconds):
        self.seconds = seconds

    def record(self):
        # Our destination file and the recorder
        output_file = StringIO()
        recorder = pyaudio.PyAudio()

        # Create the stream
        stream = recorder.open(
        format=FORMAT, channels=CHANNELS, rate=RATE,
        input=True, frames_per_buffer=CHUNK)

        # Start the recording
        recStart = time.strftime("%H:%M:%S")
        print(recStart + ": Started recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * self.seconds)):
            data = stream.read(CHUNK)
            frames.append(data)

        # Stop the recording
        recStop = time.strftime("%H:%M:%S")
        print(recStop + ": Stopped recording")

        stream.stop_stream()
        stream.close()
        recorder.terminate()

        # Save the file
        wf = wave.open(output_file, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(recorder.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        # Return the file as output from the function
        return output_file