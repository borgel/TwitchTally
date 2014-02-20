#!/usr/bin/env python

'''
www.twitchapps.com/tmi


'''

import irc.client

class TwitchParams:
   """Hold constants for connecting to Twitch IRC"""
   """http://www.twitch.tv/twitchplayspokemon"""
   server = "twitch.tv"
   port = 6667
   pokemon = "asd"

class TwitchIn:
   def on_connect(connection, event):
      if irc.client.is_channel(target):
         connection.join(target)
         return
      main_loop(connection)

   def connect(self):
      """Create a server object, connect and join the channel"""
      client = irc.client.IRC()
      try:
         c = client.server().connect(
               TwitchParams.server,
               TwitchParams.port,
               "readerNick")
      except irc.client.ServerConnectionError:
         print(sys.exc_info()[1])
         raise SystemExit(1)

      # install handlers
      # g = lambda x: x**2
      c.add_global_handler("welcome", on_connect)

      ''' fall into the forever loop '''
      client.process_forever()


print 'Starting'

tin = TwitchIn()

tin.connect()

