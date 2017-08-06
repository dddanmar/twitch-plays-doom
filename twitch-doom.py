'''
Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at
    http://aws.amazon.com/apache2.0/
or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
'''

import sys
import irc.bot
import requests
from rdoom import rDoomAPI
import os

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self):
        self.client_id = os.environ['TWITCH_CLIENT_ID']
        self.token = os.environ['TWTICH_TOKEN']
        self.channel = os.environ['TWTICH_CHANNEL']
        self.user= os.environ['TWITCH_USER']
        rd_port = 6666
        rd_host = "http://localhost"
        self.rda =  rDoomAPI(rd_host, rd_port)

        url = 'https://api.twitch.tv/kraken/users?login=' + self.user
        headers = {'Client-ID': self.client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers=headers).json()
        self.channel_id = r['users'][0]['_id']

        server = 'irc.chat.twitch.tv'
        port = 6667
        print 'Connecting to ' + server + ' on port ' + str(port) + '...'
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:'+self.token)], "dddanmar", "dddanmar")


    def on_welcome(self, c, e):
        print 'Joining ' + self.channel

        # You must request specific capabilities before you can use them
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        commands = ["f","b","l","r","s","d","p","a","1","2","3","4","5","6"]
        command = e.arguments[0]
        if command == "iddqd":
            self.rda.godmode()
            return 
        if len(command)==1:
            if command in commands:
                print("Got command %s" % command)
                if command == "f": self.rda.forward()
                if command == "b": self.rda.backward()
                if command == "l": self.rda.left()
                if command == "r": self.rda.right()
                if command == "s": self.rda.shoot()
                if command == "d": self.rda.activate()
                if command == "p":
                    self.rda.shoot()
                    self.rda.shoot()
                if command == "a": self.rda.activate()
                if command == "1": self.rda.swapweapon(command)
                if command == "2": self.rda.swapweapon(command)
                if command == "3": self.rda.swapweapon(command)
                if command == "4": self.rda.swapweapon(command)
                if command == "5": self.rda.swapweapon(command)
                if command == "6": self.rda.swapweapon(command)



        return

    def do_command(self, e, cmd):
        c = self.connection

        # Poll the API to get current game.
        if cmd == "game":
            url = 'https://api.twitch.tv/kraken/channels/' + self.channel_id
            headers = {'Client-ID': self.client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
            r = requests.get(url, headers=headers).json()
            c.privmsg(self.channel, r['display_name'] + ' is currently playing ' + r['game'])

        # Poll the API the get the current status of the stream
        elif cmd == "title":
            url = 'https://api.twitch.tv/kraken/channels/' + self.channel_id
            headers = {'Client-ID': self.client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
            r = requests.get(url, headers=headers).json()
            c.privmsg(self.channel, r['display_name'] + ' channel title is currently ' + r['status'])

        # Provide basic information to viewers for specific commands
        elif cmd == "raffle":
            message = "This is an example bot, replace this text with your raffle text."
            c.privmsg(self.channel, message)
        elif cmd == "schedule":
            message = "This is an example bot, replace this text with your schedule text."
            c.privmsg(self.channel, message)

        # The command was not recognized
        else:
            c.privmsg(self.channel, "Did not understand command: " + cmd)

def main():
    # if len(sys.argv) != 5:
    #     print("Usage: twitchbot <username> <client id> <token> <channel>")
    #     sys.exit(1)
    #
    # username  = sys.argv[1]
    # client_id = sys.argv[2]
    # token     = sys.argv[3]
    # channel   = sys.argv[4]

    bot = TwitchBot()
    bot.start()

if __name__ == "__main__":
    main()
