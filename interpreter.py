from controller import Controller

class Interpreter:
    def __init__(self):
        self.aController = Controller()

    def interpret(self, input):
        request = input
        message = request['msg_body']
        outcome = request['outcome']
        confidence = outcome['confidence']
        entities = outcome['entities']
        intent = outcome['intent']

        print("Wit.AI analysis:")
        print("    Message: " + message)
        print("    Confidence: " + str(confidence))
        print("    Entities: " + str(entities))
        print("    Intent: " + intent)

        if intent == "play_pandora":
            getattr(self.aController, '%s' % intent)(entities['station'])
        else:
            getattr(self.aController, '%s' % intent)()