# Standard Modules
import sys
import os
# Modules from the GitHub
from wit import Wit
# The chunks
from recorder import Recorder
from interpreter import Interpreter

# Constants
SECONDS = 4

if __name__ == '__main__':

    # Set the Wit.AI token from an environment variable
    if 'WIT_TOKEN' not in os.environ:
        os.environ['WIT_TOKEN'] = raw_input("Enter your Wit.AI token: ")
    witToken = os.environ['WIT_TOKEN']

    # Instantiate the chunks
    aRecording = Recorder(SECONDS)
    anInterpreting = Interpreter()
    witty = Wit(witToken)

    # Run with it
    audio_file = aRecording.record()
    result = witty.post_speech(audio_file.getvalue())
    anInterpreting.interpret(result)

    # And we're done
    sys.exit(0)