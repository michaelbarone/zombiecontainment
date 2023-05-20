import es, random, gamethread, playerlib, popuplib, usermsg, vecmath, weaponlib, cmdlib, spe


menupullup = "y"
prop = 'props/cs_office/file_cabinet1.mdl'


low = 1
high = 30
grendet = 0
fardist = 350


def reset():
	global low, high, location, grendet
	low = 1
	high = 12
	location = 0,0,0
	grendet = 0
	createupgradepopup()
	unsendnameallpopups()
	resetupgrades()

def resetwide():
	global low, high, location, grendet
	low = 4
	high = 20
	location = 0,0,0
	grendet = 0
	createupgradepopup()
	unsendnameallpopups()
	resetupgrades()

location = 0,0,0
ctplayers = []
weaponoptions = []
upgradeoptions = []

supplypopups = ('mainmenu','weaponcrate','upgrademenu')

pistols = ('weapon_usp,weapon_glock,weapon_deagle,weapon_p228,weapon_elite,weapon_fiveseven')

weapons = {
	1: 'weapon_deagle',
	2: 'weapon_elite',
	3: 'weapon_elite',
	4: 'weapon_elite',
	5: 'weapon_elite',
	6: 'weapon_m3',
	7: 'weapon_m3',
	8: 'weapon_m3',
	9: 'weapon_m3',
	10: 'weapon_m3',
	11: 'weapon_m3',
	12: 'weapon_m3',
	13: 'weapon_xm1014',
	14: 'weapon_mp5navy',
	15: 'weapon_mp5navy',
	16: 'weapon_p90',
	17: 'weapon_tmp',
	18: 'weapon_mac10',
	19: 'weapon_m4a1',
	20: 'weapon_ak47',
	21: 'weapon_ak47',
	22: 'weapon_sg552',
	23: 'weapon_m4a1',
	24: 'weapon_m4a1',
	25: 'weapon_aug',
	26: 'weapon_scout',
	27: 'weapon_awp',
	28: 'weapon_g3sg1',
	29: 'weapon_sg550',
	30: 'weapon_m249'
}

def load():
	global mainpopup
	mainpopup = popuplib.easymenu('mainmenu', '_popup_choicem', main_menuselect)
	mainpopup.settitle('Supply Drop')
	moptions = ('Weapons', 'Larger Ammo Clips', 'Upgrades')
	for o in moptions:
		mainpopup.addoption(o, o)

	es.load('zombiecontainment/supplydrop/grenadesack')
	createupgradepopup()

def unload():
	for userid in playerlib.getUseridList('#human'):
		gamethread.delayed(.2, es.server.queuecmd, 'es_xfire %s func_buyzone start' %userid)
	unsendnameallpopups()
	gamethread.cancelDelayed('checkdrop')
	es.unload('zombiecontainment/supplydrop/grenadesack')
	for yyy in supplypopups:
		popuplib.delete(yyy)

def createupgradepopup():
	global upgradepopup, upgradeoptions
	upgradepopup = popuplib.easymenu('upgrademenu', '_popup_choice', upgrade_menuselect)
	upgradepopup.settitle('Supply Drop - Upgrades')
	upgradeoptions = []
	uoptions = ('Hand Guns - 12000', 'Shotguns - 8000', 'SMGs - 11000', 'Rifles - 13000', 'Sniper Rifles - 8000', 'Grenades - 10000', 'Automatic Hand Guns - 12000', 'Main Menu')
	for p in uoptions:
		upgradeoptions.append(p)
	for u in upgradeoptions:
		upgradepopup.addoption(u, u)

def unsendnameallpopups():
	for xxx in supplypopups:
		## if popuplib.isqueued(xxx, playerlib.getUseridList('#human')):
		popuplib.unsendname(xxx, playerlib.getUseridList('#human'))

def refreshpopup():
	for userid in playerlib.getUseridList('#human,#alive'):
		for xxx in supplypopups:
			if popuplib.isqueued(xxx, userid):
				popuplib.updatePopup(xxx, userid)

def round_freeze_end(ev):
	global ctplayers
	ctplayers = playerlib.getUseridList('#ct,#alive')
	supplydrop()
	removeweapons()

def round_end(ev):
	global location
	location = 0,0,0
	gamethread.cancelDelayed('checkdrop')
	unsendnameallpopups()

def supplydrop():
	global low, high, options, weaponoptions, grendet, cratepopup
	weaponoptions = []
	for x in ctplayers:
		weaponoptions.append(weapons[random.randint(low, high)])
		weaponoptions.append(weapons[random.randint(low, high)])
		weaponoptions.append('weapon_hegrenade')
	weaponoptions.append('Main Menu')
	cratepopup = popuplib.easymenu('weaponcrate', '_popup_choice', weapon_menuselect)
	cratepopup.settitle('Supply Drop - Weapons')
	for o in weaponoptions:
		cratepopup.addoption(o, o)
	if low < 5:
		low += 1
	if high < 26:
		high += 4
		if high > 30:
			high = 30
	gamethread.cancelDelayed('checkdrop')
	for userid in playerlib.getUseridList('#ct,#alive,#human'):
		es.tell(userid, '#multi', '#lightgreen[Zombie Containment]: #defaultThe Army is flying over, throw a smoke grenade for a supply drop.')
		for index in weaponlib.getIndexList('smokegrenade'):
			if es.getindexprop(index, 'CBaseEntity.m_hOwnerEntity') == userid:
				es.server.queuecmd('es_xremove %s' % index)
		es.server.queuecmd('es_give %s weapon_smokegrenade' %userid)
	grendet = 0
	gamethread.delayedname(20, 'checkdrop', checkdroploop)

def player_death(event_var):
	userid = event_var['userid']
	for xxx in supplypopups:
		if popuplib.isqueued(xxx, userid):
			popuplib.unsendname(xxx, userid)

def es_player_chat(event_var):
	if event_var['text'] == '%s'%menupullup:
		if es.getplayerteam(event_var['userid']) == 3:
			global location
			playerloc = es.getplayerprop(event_var['userid'], "CBaseEntity.m_vecOrigin")
			dist = vecmath.distance(playerloc, location)
			if dist < fardist:
				popuplib.send('mainmenu', event_var['userid'])			

def player_spawn(event_var):
	userid = event_var['userid']
	Player(userid).pspawn()

def smokegrenade_detonate(event_var):
	gamethread.cancelDelayed('checkdrop')
	global grendet
	if grendet == 0:
		grendet = 1
		global location, coords
		coords = []
		location = ','.join(event_var[x] for x in 'xyz')
		## userid = es.getuserid()
		userid = str(random.choice(playerlib.getUseridList('#bot')))
		oldpos = es.getplayerlocation(userid)
		oldang = playerlib.getPlayer(userid).getViewAngle()
		coords = location.split(",")
		gamethread.delayed(2, es.server.queuecmd, 'es_setpos %s %s %s %s' %(userid,coords[0],coords[1],coords[2]))
		gamethread.delayed(2, es.server.queuecmd, 'es_setang %s 270 0 0' %userid)	
		gamethread.delayed(2, es.server.queuecmd, 'es_xprop_physics_create %s %s' %(userid,prop))
		gamethread.delayed(2, es.server.queuecmd, 'es_setpos %s %s %s %s' %(userid,oldpos[0],oldpos[1],oldpos[2]))
		gamethread.delayed(2, es.server.queuecmd, 'es_setang %s %s %s %s' %(userid,oldang[0],oldang[1],oldang[2]))
		es.msg('#multi', '#lightgreen[Zombie Containment]:#default Say #green%s #default near the smoke grenade or dropped box to access more weapons.'%menupullup)
		for userid1 in playerlib.getUseridList('#alive'):
			for index in weaponlib.getIndexList('smokegrenade'):
				if es.getindexprop(index, 'CBaseEntity.m_hOwnerEntity') == userid1:
					es.server.queuecmd('es_xremove %s' % index)

def weapon_menuselect (userid, choice, popupid):
	if not playerlib.getPlayer(userid).get('isdead'):
		global location
		playerloc = es.getplayerprop(userid, "CBaseEntity.m_vecOrigin")
		dist = vecmath.distance(playerloc, location)
		if dist < fardist:
			global weaponoptions
			if choice == "Main Menu":
				popuplib.send('mainmenu', userid)
				return
			if choice in weaponoptions:
				if choice in str(pistols).split(','):
					if playerlib.getPlayer(userid).getSecondary():
						gun = playerlib.getPlayer(userid).getSecondary()
						## es.server.queuecmd('est_removeweapon %s 2'%userid)
						spe.dropWeapon(userid, gun)
				else:
					if choice == "weapon_hegrenade":
						es.server.queuecmd('es_give %s weapon_hegrenade' %userid)
						es.server.queuecmd('es_give %s weapon_hegrenade' %userid)
						es.server.queuecmd('es_give %s weapon_hegrenade' %userid)
					else:
						if playerlib.getPlayer(userid).getPrimary():
							gun = playerlib.getPlayer(userid).getPrimary()
							## es.server.queuecmd('est_removeweapon %s 1'%userid)
							spe.dropWeapon(userid, gun)
				es.server.queuecmd('es_give %s %s' %(userid,choice))
				weaponoptions.remove('%s'%choice)
				if weaponoptions == []:
					supplydrop()
				else:
					cratepopup = popuplib.easymenu('weaponcrate', '_popup_choice', weapon_menuselect)
					cratepopup.settitle('Weapon Drop')
					for o in weaponoptions:
						cratepopup.addoption(o, o)
					refreshpopup()
			else:
				es.tell(userid,'Choice not available anymore.')
		else:
			es.tell(userid,'You are not close enough to a supply drop.')
	else:
		es.tell(userid,'You Must be alive to use a supply drop.')
	
def main_menuselect (userid, choice, popupid):
	if not playerlib.getPlayer(userid).get('isdead'):
		global location
		playerloc = es.getplayerprop(userid, "CBaseEntity.m_vecOrigin")
		dist = vecmath.distance(playerloc, location)
		if dist < fardist:
			if choice == "Weapons":
				popuplib.send('weaponcrate', userid)
			elif choice == "Larger Ammo Clips":
				es.tell(userid,'Larger Weapon Clips are disabled.')
				popuplib.send('mainmenu', userid)
			elif choice == "Upgrades":
				popuplib.send('upgrademenu', userid)	
		else:
			es.tell(userid,'You are not close enough to a supply drop.')
	else:
		es.tell(userid,'You Must be alive to use a supply drop.')		
		
def upgrade_menuselect (userid, choice, popupid):
	if not playerlib.getPlayer(userid).get('isdead'):
		global location
		playerloc = es.getplayerprop(userid, "CBaseEntity.m_vecOrigin")
		dist = vecmath.distance(playerloc, location)
		if dist < fardist:
			name = es.getplayername(userid)
			if choice == "Main Menu":
				popuplib.send('mainmenu', userid)
				return
			global upgradeoptions
			if choice in upgradeoptions:
				if choice == "Hand Guns - 12000":
					if playerlib.getPlayer(userid).get('cash') >= 12000:
						playerlib.getPlayer(userid).set('cash', playerlib.getPlayer(userid).get('cash') - 12000)
						es.load('zombiecontainment/supplydrop/critshotpistol')
						es.msg('#multi', '#lightgreen%s #default upgraded #lightgreenPistol Damage' %name)
						upgradeoptions.remove('%s'%choice)
						refreshupgradelist()
				if choice == "Shotguns - 8000":
					if playerlib.getPlayer(userid).get('cash') >= 8000:
						playerlib.getPlayer(userid).set('cash', playerlib.getPlayer(userid).get('cash') - 8000)
						es.load('zombiecontainment/supplydrop/critshotshotgun')
						es.msg('#multi', '#lightgreen%s #default upgraded #lightgreenShotgun Damage' %name)
						upgradeoptions.remove('%s'%choice)
						refreshupgradelist()
				if choice == "SMGs - 11000":
					if playerlib.getPlayer(userid).get('cash') >= 11000:
						playerlib.getPlayer(userid).set('cash', playerlib.getPlayer(userid).get('cash') - 11000)
						es.load('zombiecontainment/supplydrop/critshotsmg')
						es.msg('#multi', '#lightgreen%s #default upgraded #lightgreenSMG Damage' %name)
						upgradeoptions.remove('%s'%choice)
						refreshupgradelist()
				if choice == "Rifles - 13000":
					if playerlib.getPlayer(userid).get('cash') >= 13000:
						playerlib.getPlayer(userid).set('cash', playerlib.getPlayer(userid).get('cash') - 13000)
						es.load('zombiecontainment/supplydrop/critshotrifle')
						es.msg('#multi', '#lightgreen%s #default upgraded #lightgreenRifle Damage' %name)
						upgradeoptions.remove('%s'%choice)
						refreshupgradelist()
				if choice == "Sniper Rifles - 8000":
					if playerlib.getPlayer(userid).get('cash') >= 8000:
						playerlib.getPlayer(userid).set('cash', playerlib.getPlayer(userid).get('cash') - 8000)
						es.load('zombiecontainment/supplydrop/critshotsniper')
						es.msg('#multi', '#lightgreen%s #default upgraded #lightgreenSniper Damage' %name)
						upgradeoptions.remove('%s'%choice)
						refreshupgradelist()
				if choice == "Grenades - 10000":
					"""
					es.tell(userid,'Grenade Damage Upgrade is disabled.')
					popuplib.send('mainmenu', userid)
					"""
					if playerlib.getPlayer(userid).get('cash') >= 10000:
						playerlib.getPlayer(userid).set('cash', playerlib.getPlayer(userid).get('cash') - 10000)
						es.load('zombiecontainment/supplydrop/nadeslay')
						es.msg('#multi', '#lightgreen%s #default upgraded #lightgreenGrenade Damage' %name)
						upgradeoptions.remove('%s'%choice)
						refreshupgradelist()
				if choice == "Automatic Hand Guns - 12000":
					es.tell(userid,'Automatic Hand Guns Upgrade is disabled.')
					popuplib.send('mainmenu', userid)
					"""
					if playerlib.getPlayer(userid).get('cash') >= 12000:
						playerlib.getPlayer(userid).set('cash', playerlib.getPlayer(userid).get('cash') - 12000)
						es.load('zombiecontainment/supplydrop/weaponmod')
						es.msg('#multi', '#lightgreen%s #default upgraded #lightgreenPistol Fire Rate' %name)
						upgradeoptions.remove('%s'%choice)
						refreshupgradelist()
					"""
			else:
				es.tell(userid,'Choice not available anymore.')
		else:
			es.tell(userid,'You are not close enough to a supply drop.')
	else:
		es.tell(userid,'You Must be alive to use a supply drop.')		
			
def refreshupgradelist():
	global upgradeoptions, upgradepopup
	upgradepopup = popuplib.easymenu('upgrademenu', '_popup_choice', upgrade_menuselect)
	upgradepopup.settitle('Supply Drop - Upgrades')
	for d in upgradeoptions:
		upgradepopup.addoption(d, d)
	refreshpopup()

def resetupgrades():
	es.unload('zombiecontainment/supplydrop/critshotpistol')
	es.unload('zombiecontainment/supplydrop/weaponmod')
	es.unload('zombiecontainment/supplydrop/nadeslay')
	es.unload('zombiecontainment/supplydrop/critshotsniper')
	es.unload('zombiecontainment/supplydrop/critshotrifle')
	es.unload('zombiecontainment/supplydrop/critshotsmg')
	es.unload('zombiecontainment/supplydrop/critshotshotgun')

def checkdroploop():
	gamethread.cancelDelayed('checkdrop')
	gamethread.delayedname(20, 'checkdrop', checkdroploop)
	if grendet == 0:
		for userid in playerlib.getUseridList('#ct,#alive'):	
			es.tell(userid, '#multi', '#lightgreen[Zombie Containment]: #default The Army is flying over, throw a smoke grenade for a supply drop.')
	else:
		gamethread.cancelDelayed('checkdrop') 

def removeweapons():
	for index in weaponlib.getIndexList('#primary'):
		if es.getindexprop(index, 'CBaseEntity.m_hOwnerEntity') == -1:
			es.server.cmd('es_xremove %s' % index)

class Player:
	def __init__(self, userid):
		self.userid = userid
		self.steamid = es.getplayersteamid(userid)

	def pspawn(self):
		if es.getplayerteam(self.userid) == 3:
			if self.steamid != 'BOT':
				if grendet == 0:
					global weaponoptions
					if weaponoptions != []:
						for index in weaponlib.getIndexList('smokegrenade'):
							if es.getindexprop(index, 'CBaseEntity.m_hOwnerEntity') == self.userid:
								es.server.queuecmd('es_xremove %s' % index)
						es.server.queuecmd('es_give %s weapon_smokegrenade' %self.userid)
						## es.tell(self.userid, '#multi', '#lightgreen[Zombie Containment]:#default The Army is flying over, throw a smoke grenade for a supply drop.')
				gamethread.delayed(.2, es.server.queuecmd, 'es_xfire %s func_buyzone kill' %self.userid)
			else:
				weapon = weapons[random.randint(9, high)]
				es.server.queuecmd('es_give %s %s' %(self.userid, weapon))
				gamethread.delayed(2, removeweapons())
