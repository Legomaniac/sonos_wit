import logging

from controller import Controller

logging.basicConfig(level=logging.INFO)

class Interpreter:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.aController = Controller()

    def interpret(self, input):
        request = input
        message = request['msg_body']
        outcome = request['outcome']
        confidence = outcome['confidence']
        entities = outcome['entities']
        intent = outcome['intent']

        self.logger.info("Wit.AI analysis:")
        self.logger.info("    Message: " + message)
        self.logger.info("    Confidence: " + str(confidence))
        self.logger.info("    Entities: " + str(entities))
        self.logger.info("    Intent: " + intent)

        if intent == "play_pandora":
            getattr(self.aController, '%s' % intent)(entities['station'])
        elif intent == "control":
            getattr(self.aController, '%s' % intent)(entities['player_name'])
        else:
            getattr(self.aController, '%s' % intent)()