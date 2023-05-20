import es, popuplib, gamethread, usermsg, playerlib
## =========================
## infopopup
## initial idea taken from [thecheb]AnOmaly's script: readrules
## converted to python and modified for use with zombiecontainment by "el_cabong"
## =========================
## Brief Description:
## This script displays information about el_cabong's mod zombiecontainment.


  ## command to bring popup up in game.
command = "!info"

  ## INFO Popup.
title1 = "      el_cabong's"
title2 = "Zombie Containment"

  ## INFO list
infolist = (
	'Story Mode', 
	'Survival Mode',            
	'Say Commands',      
	'Supply Drops',             
	'Change Maps',           
	'!info command'
	) 

  ## detailedinfo info exoanding on above, will be shown when a player selects an option above. Just set any to "" if you want the option disabled.
  ## add additional lines below for every option above.
  ## spacing-----start|--------------------------------------------------------------------\n--------------------------------------------------------------------|end
detailedinfo = {
	'Story Mode': "The dead have started coming back to life in search of human flesh,\n try to stay alive and find or create a zombie free zone.", 
	'Survival Mode': "See how many zombies your team can kill before becoming over run.",           
	'Say Commands': "Say Commands: !gametype, !difficulty, !infection, !respawn, !bothelp, !info",     
	'Supply Drops': "The ARMY is flying overhead dropping supplies where they see \n survivors. Use smoke grenades to signal for a supply drop.",            
	'Change Maps': "Say !gtfo in story mode or !maps in survival mode.",       
	'!info command': "Saying !info during gameplay will display this popup"
	}

################################
## end of config              ##
## Dont edit below this line  ##
################################

                    

def load():
	infopopup = popuplib.easymenu('infomenu', '_popup_choice', info_menuselect)
	infopopup.settitle('%s \n %s' %(title1,title2))
	for u in infolist:
		infopopup.addoption(u, u)
	for userid in playerlib.getUseridList('#human'):
		popuplib.send('infomenu', userid)

def unload():
	popuplib.unsendname('infomenu', playerlib.getUseridList('#human'))
	popuplib.delete('infomenu')

def player_activate(event_var):
	if es.getplayersteamid(event_var['userid']) != 'BOT':
		popuplib.send('infomenu', event_var['userid'])

def es_player_chat(event_var):
	if event_var['text'] == '%s'%command:
		popuplib.send('infomenu', event_var['userid'])

def info_menuselect (userid, choice, popupid):
	es.usermsg('create', 'mymsg', 'KeyHintText')
	es.usermsg('write',  'byte',       'mymsg', 1)
	es.usermsg('write',  'string',     'mymsg', "%s"%detailedinfo[choice])
	es.usermsg('send',   'mymsg', userid)
	es.usermsg('delete', 'mymsg')
	popuplib.send('infomenu', userid)
