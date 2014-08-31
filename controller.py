# Standard Modules
import sys
from pprint import pprint
import logging
# Modules from GitHub
import soco

import yaml

from player import Player

logging.basicConfig(level=logging.INFO)

###########################################
## IMPORTANT:                            ##
##  These functions must have the exact  ##
##  same names as the intents in the     ##
##  instance of Wit.AI being used        ##
###########################################

class Controller:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.stations = yaml.load(open("stations.yml", 'r'))
        self.active = yaml.load(open("active.yml", 'r'))
        self.player = Player()

        self.soni = soco.discover()
        self.logger.info("Soni found:")
        if self.soni:
            for sonos in self.soni:
                self.logger.info("    " + sonos.player_name)
                if sonos.player_name.lower() == self.active['currentlyActive']:
                    self.activeSonos = sonos
            self.logger.info("Active player: " + self.activeSonos.player_name)
        else:
            self.logger.info("Couldn't find any Sonos :(")
            sys.exit(0)

    def play(self):
        try:
            self.activeSonos.play()
        except soco.exceptions.SoCoUPnPException, error:
            self.logger.info("nawp " + str(error))
        self.logger.info("Play selected")

    def pause(self):
        try:
            self.activeSonos.pause()
        except soco.exceptions.SoCoUPnPException, error:
            self.logger.info("nawp " + str(error))
        self.logger.info("Pause selected")

    def previous(self):
        try:
            self.activeSonos.previous()
        except soco.exceptions.SoCoUPnPException, error:
            self.logger.info("nawp " + str(error))
        self.logger.info("Previous selected")

    def next(self):
        try:
            self.activeSonos.next()
        except soco.exceptions.SoCoUPnPException, error:
            self.logger.info("nawp " + str(error))
        self.logger.info("Next selected")

    def adjust_volume_up(self):
        try:
            self.activeSonos.volume += 10
        except soco.exceptions.SoCoUPnPException, error:
            self.logger.info("nawp " + str(error))
        self.logger.info("Volume up selected")

    def adjust_volume_down(self):
        try:
            self.activeSonos.volume -= 10
        except soco.exceptions.SoCoUPnPException, error:
            self.logger.info("nawp " + str(error))
        self.logger.info("Volume down selected")

    def play_pandora(self, station):
        stationName = station['body']
        try:
            stationUri = self.stations[stationName]['uri']
            stationMeta = self.stations[stationName]['uriMeta']
            try:
                self.activeSonos.play_uri(stationUri, stationMeta)
            except soco.exceptions.SoCoUPnPException, error:
                self.logger.info("nawp " + str(error))
        except:
            self.logger.info("Didn't understand station name %s, sorry :(" %stationName)

        self.logger.info("Pandora station %s selected" %stationName)

    def line_in(self):
        try:
            self.activeSonos.switch_to_line_in()
            self.activeSonos.play()
        except soco.exceptions.SoCoUPnPException, error:
            self.logger.info("nawp " + str(error))
        ####### Test the player #######
        self.player.play("fully_connected.wav")
        self.logger.info("Line in selected")

    def get_info(self):
        try:
            info = self.activeSonos.get_current_track_info()
            prettystring = pprint(info)
            self.logger.info(prettystring)
        except soco.exceptions.SoCoUPnPException, error:
            self.logger.info("nawp " + str(error))
        self.logger.info("Info selected")

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
            self.logger.info("nawp " + str(error))
        self.logger.info("Switched control to: " + playerName)