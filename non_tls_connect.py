#!/usr/bin/env python3

import pydle

# name, irc server, and channel for the bot to join. also setup the list of admin users that can control the bot

botname = 'ampbot'
server = 'irc.quakenet.org'
channel = '#aiur'
adminNick = [ 'booboy', 'booboywork', 'Amp', 'AmpWork']

class aiurBot(pydle.Client):
    """ behold the aiur irc bot! """

    def on_connect(self):
        super().on_connect()
        # Can't greet many people without joining a channel.
        self.join(channel)

    def on_join(self, channel, user):
        super().on_join(channel, user)
        self.message(channel,'Greetings, I am ' + botname)  

    @pydle.coroutine
    def is_admin(self, nickname):
        """
        Check whether or not a user has admin priviledge.
        """
        if nickname in adminNick:
            return True
            #info = yield self.whois(source)
            #admin = info['identified']
        return False

    @pydle.coroutine
    def on_message(self, target, source, message):
        super().on_message(target, source, message)

        # Tell a user if they are an administrator for this bot.
        if message.startswith('!adminstatus'):
            admin = yield self.is_admin(source)

        if admin == True:
            print("User "+source+" is an admin!")
            self.message(channel, 
                    source+': You are an administrator.'
            )
        else:
            print("User "+source+" is not an admin!")
            self.message(channel, 
                    source+': You are not an administrator.', 
            )

client = aiurBot(botname)
client.connect(server, tls=False)
client.handle_forever()

