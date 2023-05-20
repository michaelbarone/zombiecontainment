import es
import random
import effectlib
import playerlib

# show a beam between attacker and victim if it was a crit shot
beam = 0

# color of the beam
beam_red = 0
beam_blue = 0
beam_green = 0

# how long the beam is visible (in seconds)
beam_duration = 0

# mult   = multiplicator for the damage (standard = 1.0)
# chance = chance in percent a critical shot happens
weapons = {
   'mp5navy': {'mult': 2, 'chance': 100},
   'tmp': {'mult': 2, 'chance': 100},
   'p90': {'mult': 2, 'chance': 100},
   'mac10': {'mult': 2, 'chance': 100},
   'ump45': {'mult': 2, 'chance': 100}
}

# message
# 0 = off, 1 = center, 2 = top, 3 = chat
# %a = attacker name, %u = user name, %d = damage, %w = weapon
msg_option = 0
msg = "%a did a crit shot on %u with %w. He did %d dmg!"

# crit shots can not kill someone (useful for gungame because the weapon is always player_hurt)
no_crit_kill = 0

# plugin information
info = es.AddonInfo() 
info.name     = "Crit Shot SMG" 
info.version  = "0.1" 
info.url      = "http://addons.eventscripts.com/addons/view/critshot" 
info.basename = "critshotsmg" 
info.author   = "Rio"

crit_version = es.ServerVar('crit_version', '0.3')
crit_version.makepublic()
   
def player_hurt(event_var):
   weapon = event_var['weapon']

   # check for fall dmg or he dmg
   if event_var['userid'] != event_var['attacker']:
      if weapons.has_key(weapon):
         rand = random.randint(0, 100)
      
         if weapons[weapon].has_key('mult') and weapons[weapon].has_key('chance'):
            if rand <= weapons[weapon]['chance']:
               # crit shot
               damage = int(event_var['dmg_health']) * int(weapons[weapon]['mult']) - int(event_var['dmg_health'])
               
               # no crit kill
               if no_crit_kill and damage >= event_var['es_userhealth']:
                  if event_var['dmg_health'] >= event_var['es_userhealth']:
                     damage = 0
                  else:
                     damage = int(event_var['es_userhealth']) - int(event_var['dmg_health']) - 1
               
               # beam
               if beam and damage > 0:
                  coord1 = es.getplayerprop(event_var['userid'], 'CBaseEntity.m_vecOrigin')
                  coord2 = es.getplayerprop(event_var['attacker'], 'CBaseEntity.m_vecOrigin')
                  
                  effectlib.drawLine(coord1, coord2, 'materials/sprites/laser.vmt', 'materials/sprites/halo01.vmt', beam_duration, 10, 10, beam_red, beam_green, beam_blue)
               
               # msg   
               if msg_option > 0 and msg_option < 4 and damage > 0:
                  new_msg = msg.replace('%a', event_var['es_attackername'])
                  new_msg = new_msg.replace('%u', event_var['es_username'])
                  new_msg = new_msg.replace('%d', str(damage))
                  new_msg = new_msg.replace('%w', event_var['weapon'].replace('weapon_', ''))
               
                  if msg_option == 1:
                     es.centermsg(new_msg)
                  if msg_option == 2:
                     rplayerlist = playerlib.getPlayerList('#all')
                     for k in rplayerlist:
                        es.toptext(k.userid, 2, '#red', new_msg)
                  if msg_option == 3:
                     es.msg(new_msg)
               
               # dmg
               if damage > 0:
                  es.server.cmd('damage %i %i 32 %i' % (int(event_var['userid']), damage, int(event_var['attacker'])))