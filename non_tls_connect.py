#!/usr/bin/env python

import pydle

# name, irc server, and channel for the bot to join. also setup the list of admin users that can control the bot

botname = 'aiurbot'
server = 'irc.quakenet.org'
channel = '#aiur'
admin_nicks = [ 'booboy', 'booboywork', 'Amp', 'AmpWork' ]

class aiurBot(pydle.Client):
    """ behold the aiur irc bot! """

    def on_connect(self):
        super().on_connect()
        # Can't greet many people without joining a channel.
        self.join(channel)

    def on_join(self, channel, user):
        super().on_join(channel, user)
        self.message(channel,'Greetings, I am ' + botname)  

client = aiurBot(botname)
client.connect(server, tls=False)
client.handle_forever()

