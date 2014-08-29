# Standard Modules
import sys
from pprint import pprint
# Modules from GitHub
import soco

import yaml

from player import Player

###########################################
## IMPORTANT:                            ##
##  These functions must have the exact  ##
##  same names as the intents in the     ##
##  instance of Wit.AI being used        ##
###########################################

class Controller:
    def __init__(self):
        self.stations = yaml.load(open("stations.yml", 'r'))
        self.active = yaml.load(open("active.yml", 'r'))
        self.player = Player()

        self.soni = soco.discover()
        print("Soni found:")
        if self.soni:
            for sonos in self.soni:
                print("    " + sonos.player_name)
                if sonos.player_name.lower() == self.active['currentlyActive']:
                    self.activeSonos = sonos
            print("Active player: " + self.activeSonos.player_name)
        else:
            print("Couldn't find any Sonos :(")
            sys.exit(0)

    def play(self):
        try:
            self.activeSonos.play()
        except soco.exceptions.SoCoUPnPException, error:
            print("nawp " + str(error))
        print("Play selected")

    def pause(self):
        try:
            self.activeSonos.pause()
        except soco.exceptions.SoCoUPnPException, error:
            print("nawp " + str(error))
        print("Pause selected")

    def previous(self):
        try:
            self.activeSonos.previous()
        except soco.exceptions.SoCoUPnPException, error:
            print("nawp " + str(error))
        print("Previous selected")

    def next(self):
        try:
            self.activeSonos.next()
        except soco.exceptions.SoCoUPnPException, error:
            print("nawp " + str(error))
        print("Next selected")

    def adjust_volume_up(self):
        # TO BE IMPLEMENTED
        print("Volume up selected")

    def adjust_volume_down(self):
        # TO BE IMPLEMENTED
        print("Volume down selected")

    def play_pandora(self, station):
        stationName = station['body']
        try:
            stationUri = self.stations[stationName]['uri']
            stationMeta = self.stations[stationName]['uriMeta']
            try:
                self.activeSonos.play_uri(stationUri, stationMeta)
            except soco.exceptions.SoCoUPnPException, error:
                print("nawp " + str(error))
        except:
            print("Didn't understand station name %s, sorry :(" %stationName)

        print("Pandora station %s selected" %stationName)

    def line_in(self):
        try:
            self.activeSonos.switch_to_line_in()
            self.activeSonos.play()
        except soco.exceptions.SoCoUPnPException, error:
            print("nawp " + str(error))
        ####### Test the player #######
        self.player.play("fully_connected.wav")
        print("Line in selected")

    def get_info(self):
        try:
            info = self.activeSonos.get_current_track_info()
            pprint(info)
        except soco.exceptions.SoCoUPnPException, error:
            print("nawp " + str(error))
        print("Info selected")

    def control(self, player_name):
        playerName = player_name['value']
        try:
            for sonos in self.soni:
                if playerName.lower() in sonos.player_name.lower():
                    self.activeSonos = sonos
                    data = {'currentlyActive':playerName.lower()}
                    with open('active.yml', 'w') as outfile:
                        outfile.write(yaml.safe_dump(data, default_flow_style=False))
        except soco.exceptions.SoCoUPnPException, error:
            print("nawp " + str(error))
        print("Switched control to: " + playerName)