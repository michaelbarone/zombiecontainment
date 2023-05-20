# HealthRegen release 5 by David Bowland
# ./addons/eventscripts/healthregen/healthregen.py

# >>> To configure this addon please see healthregen.cfg (created whent he addon is first loaded) <<<

"""
Provides steady health regeneration for all players up to an optional, maximum amount. Requires only ES 2.0+
"""


import cfglib
import es
import gamethread

import psyco
psyco.full()


info = es.AddonInfo()
info.name     = 'HealthRegen'
info.version  = '6'
info.basename = 'healthregen'
info.url      = 'http://addons.eventscripts.com/addons/view/' + info.basename
info.author   = 'SuperDave'
zombiecontainment = 'zombiecontainment'

###


## config = cfglib.AddonCFG(es.getAddonPath(zombiecontainment + '/' + info.basename) + '/' + info.basename + '.cfg')
config = cfglib.AddonCFG(es.getAddonPath(zombiecontainment) + '/' + info.basename + '.cfg')


config.text(info.name + ' release %s options' % info.version)
config.text('./addons/eventscripts/zombiecontainment/%(basename)s.cfg' % {'basename':info.basename})
config.text(info.url)
config.text('')
config.text('Load this addon with: es_load ' + info.basename)
config.text('\n')

config.text('***** General options *****')
cvar_threshold = config.cvar('healthregen_threshold', 300, 'Maximum health that can be achieved with regeneration. default = 300')
cvar_roundmax  = config.cvar('healthregen_roundmax',  0,  'Maximum amount of health that can be regenerated in a round--set to 0 for no limit. default = 0')
cvar_team      = config.cvar('healthregen_team',      2,  '0 = all players regenerate, 1 = only Terrorists regenerate, 2 = only Counter-Terrorists regenerate')
config.text('\n')

config.text('***** Regeneration start options *****')
cvar_start_delay  = config.cvar('healthregen_start_delay',  7,  'Number of seconds a player must remain unhurt to start regeneration--set to 0 for continuous regeneration. default = 7')
cvar_start_health = config.cvar('healthregen_start_health', 0, 'Minimum amount of health players will have after the first regeneration iteration--set to 0 for no minimum. default = 0')
config.text('\n')

config.text('***** Regeneration iteration options *****')
cvar_iteration_delay  = config.cvar('healthregen_iteration_delay',  2, 'Seconds between regeneration iterations. default = 2')
cvar_iteration_amount = config.cvar('healthregen_iteration_amount', 4, 'Amount of health to regenerate each iteration. default = 4')

config.write()


###


class RegenManager(object):
   has_delay = False

   def __init__(self, userid):
      """
      Stores userid for the instance
      Sets the maximum amount of health the player can regenerate
      """
      self.userid = userid

      round_max      = int(cvar_roundmax)
      self.remaining = round_max if round_max else -1

   def playerHurt(self):
      """Creates a delay to regenerate health for the player"""
      self.removeDelay()

      if self.remaining:
         self.has_delay = True

         delay = float(cvar_start_delay)
         gamethread.delayedname(delay if delay else float(cvar_iteration_delay), 'healthregen_%s' % self.userid, self._executeRegen)

   def removeDelay(self):
      """Removes the delay corresponding to the player"""
      if self.has_delay:
         gamethread.cancelDelayed('healthregen_%s' % self.userid)
         self.has_delay = False

   def _executeRegen(self):
      """
      Checks to make sure the player still needs health
      Adds the required health to the player and executes another iteration if the player needs health after addition
      """
      health_now = es.getplayerprop(self.userid, 'CBasePlayer.m_iHealth')
      health_max = int(cvar_threshold)

      if health_max > health_now:
         health_addition = int(cvar_iteration_amount)
         health_addition = health_addition if self.remaining == -1 else min(health_addition, self.remaining)

         health_now += health_addition
         if self.remaining <> -1:
            self.remaining -= health_addition

         if health_max > health_now:
            health_min = int(cvar_start_health)
            if self.remaining <> -1:
               if health_min - health_now > self.remaining:
                  health_min     = health_now + self.remaining
                  self.remaining = 0

               elif health_min - health_now > 0:
                  self.remaining -= health_min - health_now

            es.setplayerprop(self.userid, 'CBasePlayer.m_iHealth', health_min if health_min > health_now else health_now)

            if self.remaining:
               gamethread.delayedname(cvar_iteration_delay, 'healthregen_%s' % self.userid, self._executeRegen)

            else:
               self.has_delay = False

         else:
            es.setplayerprop(self.userid, 'CBasePlayer.m_iHealth', health_max)
            self.has_delay = False

      else:
         self.has_delay = False


players = {}


def getPlayer(userid):
   """Returns a RegenManager instance based on userid"""
   userid = int(userid)
   if not players.has_key(userid):
      players[userid] = RegenManager(userid)

   return players[userid]


def removePlayer(userid):
   """Removes a RegenManager instance based on userid"""
   userid = int(userid)
   if players.has_key(userid):
      players[userid].removeDelay()
      del players[userid]


def clearPlayers():
   """
   Removes all player delays
   Clears RegenManager instances
   """
   for userid in players:
      players[userid].removeDelay()
   players.clear()


###


def load():
   """
   Checks to make sure critical server variables are created by the config
   """
   config.execute()


def es_map_start(event_var):
   clearPlayers()


def round_start(event_var):
   clearPlayers()


def player_hurt(event_var):
   if cvar_threshold > int(event_var['es_userhealth']):
      player_team = int(event_var['es_userteam'])
      regen_team  = int(cvar_team)
      if regen_team not in (1, 2) or player_team == regen_team + 1:
         getPlayer(event_var['userid']).playerHurt()


def player_death(event_var):
   removePlayer(event_var['userid'])


def player_disconnect(event_var):
   removePlayer(event_var['userid'])


def unload():
   clearPlayers()

   for cvar in config.getCvars():
      es.ServerVar(cvar).set(0)