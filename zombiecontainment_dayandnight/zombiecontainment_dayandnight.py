import es, playerlib, gamethread, cmdlib


midnight2 = 84		## Percentage of black to use for after midnight before dawn
midnight1 = 78		## Percentage of black to use for midnight
nightdarkness3 = 72	## Percentage of black to use as night-time darkness later even still
nightdarkness2 = 66	## Percentage of black to use as night-time darkness later 
nightdarkness1 = 60	## Percentage of black to use as night-time darkness early   
    
darkness = 0
darknessnext = 0
changeincrement = .1	
sunsetrate = 1		## Rate of time that sunset takes; must be > 0, low numbers make the transition quick, higher numbers makes the transition slow
sunriserate = 1		## Rate of time that sunrise takes; must be > 0, low numbers make the transition quick, higher numbers makes the transition slow


def load():
	startup() 

def startup():
	for userid in playerlib.getUseridList('#human'):
		es.server.queuecmd('es_give %s env_fog_controller' %userid) 
		fogcontroller()

def unload():
	daylight()

def es_map_start():
	global darkness
	## sv_skyname sky_borealis01
	darkness = 0
	fogcontroller()

def player_activate(event_var):
	userid = event_var['userid']
	es.server.queuecmd('es_give %s env_fog_controller' %userid)
	fogcontroller()

def lighter():
	global darkness
	gamethread.cancelDelayed('lighterloop')
	gamethread.delayedname(sunsetrate, 'lighterloop', lighter)
	if darkness > darknessnext:
		darkness -= changeincrement
	else:
		gamethread.cancelDelayed('lighterloop')	
	fogcontroller()

def darker():
	global darkness
	gamethread.cancelDelayed('darkerloop')
	gamethread.delayedname(sunsetrate, 'darkerloop', darker)
	if darkness < darknessnext:
		darkness += changeincrement
	else:
		gamethread.cancelDelayed('darkerloop')	
	fogcontroller()

def dusk1():
	global darkness, darknessnext
	darkness = nightdarkness1
	darknessnext = nightdarkness2
	gamethread.cancelDelayed('darkerloop')
	gamethread.cancelDelayed('lighterloop')	
	darker()

def dusk2():
	global darkness, darknessnext
	darkness = nightdarkness2
	darknessnext = nightdarkness3
	gamethread.cancelDelayed('darkerloop')
	gamethread.cancelDelayed('lighterloop')	
	darker()

def dusk3():
	global darkness, darknessnext
	darkness = nightdarkness3
	darknessnext = midnight1
	gamethread.cancelDelayed('darkerloop')
	gamethread.cancelDelayed('lighterloop')	
	darker()

def midnight():
	global darkness, darknessnext
	darkness = midnight1
	darknessnext = midnight2
	gamethread.cancelDelayed('darkerloop')
	gamethread.cancelDelayed('lighterloop')	
	darker()

def dawn1():
	global darkness, darknessnext
	darkness = midnight1
	darknessnext = nightdarkness3
	gamethread.cancelDelayed('darkerloop')
	gamethread.cancelDelayed('lighterloop')	
	lighter()

def dawn2():
	global darkness, darknessnext
	darkness = nightdarkness3
	darknessnext = nightdarkness1
	gamethread.cancelDelayed('darkerloop')
	gamethread.cancelDelayed('lighterloop')	
	lighter()

def daylight():
	global daytime, darkness
	gamethread.cancelDelayed('darkerloop')
	gamethread.cancelDelayed('lighterloop')	
	daytime = 1
	darkness = 0
	fogcontroller()	

def fogcontroller():
	for userid in playerlib.getUseridList('#human'):
		es.server.queuecmd('es_xfire %s env_fog_controller TurnOff'%userid)
		es.server.queuecmd('es_xfire %s env_fog_controller addoutput "fogcolor 0 0 0,-1,0"'%userid)
		temp1 = darkness * -100
		temp2 = temp1 + 10000		
		es.server.queuecmd('es_xfire %s env_fog_controller addoutput "fogstart %s,-1,0"'%(userid,temp1))
		es.server.queuecmd('es_xfire %s env_fog_controller addoutput "fogend %s,-1,0"'%(userid,temp2))
		es.server.queuecmd('es_xfire %s env_fog_controller TurnOn'%userid)