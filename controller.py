# Standard Modules
import sys
# Modules from GitHub
import soco

###########################################
## IMPORTANT:                            ##
##  These functions must have the exact  ##
##  same names as the intents in the     ##
##  instance of Wit.AI being used        ##
###########################################

class Controller:
    def __init__(self):
        self.players = soco.discover()
        print("Sonos players found:")
        if self.players:
            for player in self.players:
                print("    " + player.player_name)
        else:
            print("Couldn't find any Sonos :(")
            sys.exit(0)

    def play(self):
        for player in self.players:
            try:
                player.play()
            except soco.exceptions.SoCoUPnPException, error:
                print("nawp " + str(error))
        print("Play selected")

    def pause(self):
        for player in self.players:
            try:
                player.pause()
            except soco.exceptions.SoCoUPnPException, error:
                print("nawp " + str(error))
        print("Pause selected")

    def previous(self):
        # TO BE IMPLEMENTED
        print("Previous selected")

    def next(self):
        for player in self.players:
            try:
                player.next()
            except soco.exceptions.SoCoUPnPException, error:
                print("nawp " + str(error))
        print("Next selected")

    def adjust_volume_up(self):
        # TO BE IMPLEMENTED
        # for player in self.players:
        #     player.
        print("Volume up selected")

    def adjust_volume_down(self):
        # TO BE IMPLEMENTED
        print("Volume down selected")