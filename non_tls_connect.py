#!/usr/bin/env python

import pydle

class aiurBot(pydle.Client):
    """ This is a simple bot that will greet people as they join the channel. """

    def on_connect(self):
        super().on_connect()
        # Can't greet many people without joining a channel.
        self.join('#aiur')

    def on_join(self, channel, user):
        super().on_join(channel, user)
        self.message(channel, 'Hey there, {user}!', user=booboywork)

client = aiurBot('aiurbot')
client.connect('irc.quakenet.org', tls=False)
client.handle_forever()
