# NadeSlay release 4 by David Bowland
# ./addons/eventscripts/nadeslay/nadeslay.py

# >>> To configure this addon please see nadeslay.cfg <<<

"""
Alters the damage and radius of HE grenades and slays players struck with a flashbang or smoke grenade. Requires only ES 2.0+
"""


import es
import gamethread
import os.path
import random
import string


info = es.AddonInfo()
info.name = 'NadeSlay'
info.version = '4'
info.url = 'http://addons.eventscripts.com/addons/view/nadeslay'
info.basename = 'nadeslay'
info.author = 'SuperDave'


int_noisy = 0

dict_options = {'nadeslay_hegrenade_damage':[250, 'Damage done by the hegrenade--normal is 100'], 'nadeslay_hegrenade_radius':[500, 'Radius of the hegrenade--normal is 350'], 'nadeslay_hegrenade_explodeonimpact':[1, '0 = no change, 1 = HE grenades explode on impact but count as env_explosion kills'], 'nadeslay_flashbang_slay':[1, '0 = no change, 1 = Players struck by a flashbang will be killed'], 'nadeslay_smokegrenade_slay':[1, '0 = no change, 1 = Players struck by a smoke grenade will be killed']}


def load():
   """
   Checks to make sure critical server variables are created by the config
   Turns on eventscripts_noisy if necessary
   """
   global int_noisy

   for str_option in dict_options:
      es.ServerVar(str_option, dict_options[str_option][0], dict_options[str_option][1])
   if os.path.isfile(es.getAddonPath('nadeslay') + '/nadeslay.cfg'):
      es.server.cmd('es_xmexec ../addons/eventscripts/nadeslay/nadeslay.cfg')
   else:
      es.dbgmsg(0, 'NadeSlay: Unable to load nadeslay.cfg! Please ensure it is in the ./nadeslay/ directory.')

   if es.ServerVar('nadeslay_hegrenade_damage') <> 100 or es.ServerVar('nadeslay_hegrenade_radius') <> 350:
      es.doblock('corelib/noisy_on')
      if int(es.ServerVar('eventscripts_noisy')):
         int_noisy = 1
      else:
         es.ServerVar('eventscripts_noisy').set(1)
         int_noisy = 2


def round_start(event_var):
   """Removes env_explosion entities to prevent multiple explosions later"""
   int_userid = es.getuserid()
   if int_userid:
      es.server.cmd('es_xfire %s env_explosion kill' % int_userid)


def grenade_bounce(event_var):
   """
   Detonates any hegrenade projectiles beloning to the player who triggered grenade_bounce if necessary
   Calls test_hit for flashbangs if necessary
   Calls test_hit for smoke grenades if necessary
   """
   str_userid = event_var['userid']
   str_player_handle = es.getplayerhandle(str_userid)
   dict_player_list = es.createplayerlist()

   if int(es.ServerVar('nadeslay_hegrenade_explodeonimpact')):
      dict_entity_list = es.createentitylist('hegrenade_projectile')
      for int_index in dict_entity_list:
         if str_player_handle == es.getindexprop(int_index, 'CBaseEntity.m_hOwnerEntity'):
            es.server.cmd('es_xgive %s env_explosion' % str_userid)
            es.server.cmd('es_xfire %s env_explosion addoutput \"imagnitude %s\"' % (str_userid, es.ServerVar('nadeslay_hegrenade_damage')))
            es.server.cmd('es_xfire %s env_explosion addoutput \"iradiusoverride %s\"' % (str_userid, es.ServerVar('nadeslay_hegrenade_radius')))
            es.setindexprop(es.ServerVar('eventscripts_lastgive'), 'CBaseEntity.m_vecOrigin', es.getindexprop(int_index, 'CBaseEntity.m_vecOrigin'))
            es.setindexprop(es.ServerVar('eventscripts_lastgive'), 'CBaseEntity.m_hOwnerEntity', str_player_handle)
            es.server.cmd('es_xfire %s env_explosion explode' % str_userid)
            es.emitsound('entity', int_index, 'weapons/hegrenade/explode%s.wav' % random.randint(3, 5), 1.0, 0.85)
            es.server.cmd('es_xfire %s env_explosion kill' % str_userid)
            es.server.cmd('es_xremove %s' % int_index)

   if int(es.ServerVar('nadeslay_flashbang_slay')):
      test_hit(es.createentitylist('flashbang_projectile'), dict_player_list, str_userid, str_player_handle)

   if int(es.ServerVar('nadeslay_smokegrenade_slay')):
      test_hit(es.createentitylist('smokegrenade_projectile'), dict_player_list, str_userid, str_player_handle)


def player_hurt(event_var):
   """Executes slay_play if the play was hurt by a flashbang or smokegrenade if necessary"""
   str_userid = event_var['userid']
   str_attackerid = event_var['attacker']
   str_weapon = event_var['weapon']

   if str_weapon == 'flashbang' and int(es.ServerVar('nadeslay_flashbang_slay')):
      slay_player(str_userid, str_attackerid)
   elif str_weapon == 'smokegrenade' and int(es.ServerVar('nadeslay_smokegrenade_slay')):
      slay_player(str_userid, str_attackerid)


def weapon_fire(event_var):
   """Calls modify_hegrenade in 0.1 seconds if necessary"""
   if event_var['weapon'] == 'hegrenade':
      gamethread.delayed(0.3, modify_hegrenade, event_var['userid'])


def unload():
   """Removes eventscripts_noisy"""
   if int_noisy == 1:
      es.doblock('corelib/noisy_off')
   elif int_noisy == 2:
      es.ServerVar('eventscripts_noisy').set(0)

   for str_option in dict_options:
      es.ServerVar(str_option).set(0)


def test_hit(dict_entity_list, dict_player_list, str_userid, str_player_handle):
   """Slays any player in dict_player_list that comes in contact with an entity in dict_entity_list belonging to str_userid"""
   for int_index in dict_entity_list:
      if str_player_handle == es.getindexprop(int_index, 'CBaseEntity.m_hOwnerEntity'):
         list_grenade_location = string.split(es.getindexprop(int_index, 'CBaseEntity.m_vecOrigin'), ',')
         for int_loop_userid in dict_player_list:
            if int(es.getplayerprop(int_loop_userid, 'CBasePlayer.localdata.m_Local.m_bDucked')):
               if pow(pow(float(list_grenade_location[0]) - float(dict_player_list[int_loop_userid]['x']), 2) + pow(float(list_grenade_location[1]) - float(dict_player_list[int_loop_userid]['y']), 2), 0.5) <= 30 and abs(float(list_grenade_location[2]) - float(dict_player_list[int_loop_userid]['z'])) <= 45:
                  slay_player(str(int_loop_userid), str_userid)
            else:
               if pow(pow(float(list_grenade_location[0]) - float(dict_player_list[int_loop_userid]['x']), 2) + pow(float(list_grenade_location[1]) - float(dict_player_list[int_loop_userid]['y']), 2), 0.5) <= 30 and abs(float(list_grenade_location[2]) - float(dict_player_list[int_loop_userid]['z'])) <= 55:
                  slay_player(str(int_loop_userid), str_userid)


def slay_player(str_userid, str_attackerid):
   """Slays str_userid with a point_hurt giving credit to str_attackerid"""
   es.server.cmd('es_xfire %s !self addoutput \"targetname slayme\"' % str_userid)

   es.server.cmd('es_xfire %s point_hurt kill' % str_attackerid)
   es.server.cmd('es_xgive %s point_hurt' % str_attackerid)
   es.server.cmd('es_xfire %s point_hurt addoutput \"damagetarget slayme\"' % str_attackerid)
   es.server.cmd('es_xfire %s point_hurt addoutput \"damage %s\"' % (str_attackerid, es.getplayerprop(str_userid, 'CBasePlayer.m_iHealth')))
   es.server.cmd('es_xfire %s point_hurt addoutput \"damagetype 32\"' % str_attackerid)
   es.server.cmd('es_xfire %s point_hurt hurt' % str_attackerid)

   es.server.cmd('es_xfire %s !self addoutput \"targetname none\"' % str_userid)


def modify_hegrenade(str_userid):
   """Modifies the damage and radius properties of any hegrenade belonging to str_userid"""
   dict_entity_list = es.createentitylist('hegrenade_projectile')
   str_player_handle = es.getplayerhandle(str_userid)

   for int_index in dict_entity_list:
      if str_player_handle == es.getindexprop(int_index, 'CBaseEntity.m_hOwnerEntity'):
         es.setindexprop(int_index, 'CBaseGrenade.m_flDamage', es.ServerVar('nadeslay_hegrenade_damage'))
         es.setindexprop(int_index, 'CBaseGrenade.m_DmgRadius', es.ServerVar('nadeslay_hegrenade_radius'))