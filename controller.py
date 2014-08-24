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

        self.player = Player()

        self.soni = soco.discover()
        print("Soni found:")
        if self.soni:
            for sonos in self.soni:
                print("    " + sonos.player_name)
        else:
            print("Couldn't find any Sonos :(")
            sys.exit(0)

    def play(self):
        for sonos in self.soni:
            try:
                sonos.play()
            except soco.exceptions.SoCoUPnPException, error:
                print("nawp " + str(error))
        print("Play selected")

    def pause(self):
        for sonos in self.soni:
            try:
                sonos.pause()
            except soco.exceptions.SoCoUPnPException, error:
                print("nawp " + str(error))
        print("Pause selected")

    def previous(self):
        for sonos in self.soni:
            try:
                sonos.previous()
            except soco.exceptions.SoCoUPnPException, error:
                print("nawp " + str(error))
        print("Previous selected")

    def next(self):
        for sonos in self.soni:
            try:
                sonos.next()
            except soco.exceptions.SoCoUPnPException, error:
                print("nawp " + str(error))
        print("Next selected")

    def adjust_volume_up(self):
        # TO BE IMPLEMENTED
        # for sonos in self.soni:
        #     sonos.
        print("Volume up selected")

    def adjust_volume_down(self):
        # TO BE IMPLEMENTED
        print("Volume down selected")

    def line_in(self):
        for sonos in self.soni:
            try:
                sonos.switch_to_line_in()
                sonos.play()
            except soco.exceptions.SoCoUPnPException, error:
                print("nawp " + str(error))
        ####### Test the player #######
        self.player.play("fully_connected.wav")
        print("Line in selected")

    def get_info(self):
        for sonos in self.soni:
            try:
                info = sonos.get_current_track_info()
                pprint(info)
            except soco.exceptions.SoCoUPnPException, error:
                print("nawp " + str(error))
        print("Info selected")

    def play_pandora(self, station):
        for sonos in self.soni:
            try:
                stationName = station['body']
                try:
                    stationUri = self.stations[stationName]['uri']
                    stationMeta = self.stations[stationName]['uriMeta']
                    sonos.play_uri(stationUri, stationMeta)
                except:
                    print("Didn't understand station name %s, sorry :(" %stationName)
            except soco.exceptions.SoCoUPnPException, error:
                print("nawp " + str(error))

        print("Pandora selected")
