#!/usr/bin/env python

'''
www.twitchapps.com/tmi


'''

import irc.client

from sekrit import *

class TwitchParams:
   """Hold constants for connecting to Twitch IRC"""
   """http://www.twitch.tv/twitchplayspokemon"""
   server = "irc.twitch.tv"
   port = 6667
   pokemon = "twitchplayspokemon"

class TwitchIn:
   global TWITCH_USER
   global TWITCH_PASS

   def on_connect(connection, event):
      print 'connection'
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
               TWITCH_USER)
      except irc.client.ServerConnectionError:
         print(sys.exc_info()[1])
         raise SystemExit(1)

      # install handlers
      # g = lambda x: x**2
      c.add_global_handler("welcome", self.on_connect)

      # send password
      c.pass_(TWITCH_PASS)

      # join channel? TODO
      c.join(TwitchParams.pokemon)

      print 'about to start forever loop'

      ''' fall into the forever loop '''
      client.process_forever()


print 'Starting'

tin = TwitchIn()

tin.connect()

