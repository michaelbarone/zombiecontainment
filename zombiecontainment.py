####               No Config in This File              ####
###########################################################
###							###
###                               ...../~               ###
###   ____________________________~ C  ~~*              ###
###                               /<   /\~              ###        
###                ___ __________/_#__/                 ###
###               /(- /(\_\________   \                 ###
###               \ ) \ )       \     \                 ###
###                              |    |                 ###
###                             /_____|                 ###
###                            /______\                 ###
###                           /       |                 ###
###                          / /      |                 ###
###                         /_/\______|                 ###
###                         /  _(    <                  ###
###                        /    /\    \                 ###
###                       /    /  \    |                ###
###                      /____/    \____\               ###
###                    ___/__/     __\__\               ###
###                   /`    o\    /`    o\              ###
###                   |______|    |______|              ###
###							###
###########################################################
###                     el_cabong's                     ###
###                 Zombie Containment                  ###
###                    Version: 4.5                     ###
###########################################################
###########################################################
##########       No config in this file         ###########
###########################################################
###########################################################
###########################################################
###########################################################
import es, playerlib, votelib, gamethread, random, usermsg, os.path, time, popuplib, weaponlib, cmdlib, spe

### Addon Info ###

info = es.AddonInfo() 
info['name']        = "Zombie Containment" 
info['version']     = "4.5" 
info['author']      = "el_cabong" 
info['url']         = "http://forums.eventscripts.com/viewtopic.php?t=33537&sid=ca93e4ee006775a21f75d0b53c28569d" 
info['description'] = "a zombie modification with multiple game modes" 





timeofday = {
	-1: 'Survival Mode',
	0: 'Day 1 | 7:00pm',
	1: 'Day 1 | 9:25pm',
	2: 'Day 1 | 10:40pm',
	3: 'Day 2 | 12:15am',
	4: 'Day 2 | 3:30am',
	5: 'Day 2 | 7:20am',
	6: 'Day 2 | 10:35am',
	7: 'Day 2 | 12:52pm',
	8: 'Day 2 | 2:05pm',
	9: 'Day 2 | 4:20pm',
	10: 'Day 2 | 7:00pm',
	11: 'Day 2 | 9:25pm',
	12: 'Day 2 | 10:40pm',
	13: 'Day 3 | 12:15am',
	14: 'Day 3 | 3:30am',
	15: 'Day 3 | 7:20am',
	16: 'Day 3 | 10:35am',
	17: 'Day 3 | 12:52pm',
	18: 'Day 3 | 2:05pm',
	19: 'Day 3 | 4:20pm',
	20: 'Day 3 | 7:00pm',
	21: 'Day 3 | 9:25pm',
	22: 'Day 3 | 10:40pm',
	23: 'Day 4 | 12:15am',
	24: 'Day 4 | 3:30am',
	25: 'Day 4 | 7:20am',
	26: 'Day 4 | 10:35am',
	27: 'Day 4 | 12:52pm',
	28: 'Day 4 | 2:05pm',
	29: 'Day 4 | 4:20pm',
	30: 'Day 4 | 7:00pm',
	31: 'Day 4 | 9:25pm',
	32: 'Day 4 | 10:40pm',
	33: 'Day 5 | 12:15am',
	34: 'Day 5 | 3:30am',
	35: 'Day 5 | 7:20am',
	36: 'Day 5 | 10:35am',
	37: 'Day 5 | 12:52pm',
	38: 'Day 5 | 2:05pm',
	39: 'Day 5 | 4:20pm',
	40: 'Day 5 | 7:00pm',
	41: 'Day 5 | 9:25pm',
	42: 'Day 5 | 10:40pm',
	43: 'Day 6 | 12:15am',
	44: 'Day 6 | 3:30am',
	45: 'Day 6 | 7:20am',
	46: 'Day 6 | 10:35am',
	47: 'Day 6 | 12:52pm',
	48: 'Day 6 | 2:05pm',
	49: 'Day 6 | 4:20pm',
	50: 'Day 6 | 7:00pm',
	51: 'Day 6 | 9:25pm',
	52: 'Day 6 | 10:40pm',
	53: 'Day 7 | 12:15am',
	54: 'Day 7 | 3:30am',
	55: 'Day 7 | 7:20am',
	56: 'Day 7 | 10:35am',
	57: 'Day 7 | 12:52pm',
	58: 'Day 7 | 2:05pm',
	59: 'Day 7 | 4:20pm',
	60: 'Day 7 | 7:00pm',
	61: 'Day 7 | 9:25pm',
	62: 'Day 7 | 10:40pm',
	63: 'Day 8 | 12:15am',
	64: 'Day 8 | 3:30am',
	65: 'Day 8 | 7:20am',
	66: 'Day 8 | 10:35am',
	67: 'Day 8 | 12:52pm',
	68: 'Day 8 | 2:05pm',
	69: 'Day 8 | 4:20pm',
	70: 'Day 8 | 7:00pm',
	71: 'Day 8 | 9:25pm',
	72: 'Day 8 | 10:40pm',
	73: 'Day 9 | 12:15am',
	74: 'Day 9 | 3:30am',
	75: 'Day 9 | 7:20am',
	76: 'Day 9 | 10:35am',
	77: 'Day 9 | 12:52pm',
	78: 'Day 9 | 2:05pm',
	79: 'Day 9 | 4:20pm',
	80: 'Day 9 | 7:00pm',
	81: 'Day 9 | 9:25pm',
	82: 'Day 9 | 10:40pm',
	83: 'Day 10 | 12:15am',
	84: 'Day 10 | 3:30am',
	85: 'Day 10 | 7:20am',
	86: 'Day 10 | 10:35am',
	87: 'Day 10 | 12:52pm',
	88: 'Day 10 | 2:05pm',
	89: 'Day 10 | 4:20pm',
	90: 'Day 10 | 7:00pm'
}

difficultylevel = {
	0: 'Easy',
	1: 'Normal',
	2: 'Hard',
	3: 'Impossible',
	4: 'Damned',
	5: 'Hell on Earth',
	6: 'Worse than Hell on Earth',
	7: 'Hells Atrium',
	8: 'The Devils Lube',
	9: 'Fuct',
	10: 'Death is Close',
	50: 'The End is Now!'
}

infectionorrespawn = {
	0: 'Respawn Mode',
	1: 'Infection Mode'
}

ammo = {
	'ammo_338mag_max': 666, ## awp
	'ammo_357sig_max': 666, ## p228
	'ammo_45acp_max': 666,  ## ump45,mac10,usp
	'ammo_50AE_max': 666,   ## deagle
	'ammo_556mm_box_max': 666,  ## m249
	'ammo_556mm_max': 666,  ## galil,sg552,gamas,m4a1,sg550
	'ammo_57mm_max': 666,   ## p90, fiveseven
	'ammo_762mm_max': 666,  ## scout,ak47,g3sg1,aug
	'ammo_9mm_max': 666,    ## mp5navy, tmp, glock, elite
	'ammo_buckshot_max': 666 ## m3,xm1014
}

### Server Vars ### 

sv = es.ServerVar

sv_options = {
	'zc_survivalstart': 1,
	'zc_infectionstart': 1,
	'zc_infectiondeathcount': 2,
	'zc_survival_mutated_chance': 20,
	'zc_survival_boss_chance': 8,
	'zc_startingdifficulty': 1,
	'zc_difficultyincrease': 25,
	'zc_zombie_health_min': 65,
	'zc_zombie_health_max': 75,
	'zc_zombie_health_level_bonus_multiplier': .5,
	'zc_zombie_player_health_multiplier': 20,
	'zc_zombie_speed_min': 0.8,
	'zc_zombie_speed_max': 0.86,
	'zc_zombie_player_speed_multiplier': 0.02,
	'zc_zombie_armor_min': 1,
	'zc_zombie_armor_max': 5,
	'zc_zombie_armor_level_bonus_multiplier': 2,
	'zc_zombie_player_armor_multiplier': 20,
	'zc_zombie_models': 'player/elis/uz1/uz1,player/slow/classic_zombie/classic_zombie,player/slow/classic_zombie/classic_zombie_2,player/slow/classic_zombie/classic_zombie_4,player/slow/classic_zombie/classic_zombie_3',
	'zc_mutated_chance': 2,
	'zc_mutated_health_min': 88,
	'zc_mutated_health_max': 94,
	'zc_mutated_health_level_bonus_multiplier': .5,
	'zc_mutated_player_health_multiplier': 15,
	'zc_mutated_speed_min': 0.81,
	'zc_mutated_speed_max': 0.87,
	'zc_mutated_player_speed_multiplier': .02,
	'zc_mutated_armor_min': 5,
	'zc_mutated_armor_max': 15,
	'zc_mutated_armor_level_bonus_multiplier': 2,
	'zc_mutated_player_armor_multiplier': 20, 
	'zc_mutated_models': 'player/lextalionis/fatty/t_phoenix,player/slow/bloodsucker/slow_bloodsucker,player/elis/ud/undead',
	'zc_boss_chance': 75,
	'zc_boss_models': 'player/slow/el_g_fix2/slow_gigante,player/slow/el_g_fix2/slow_gigante',
	'zc_boss_health': 800,
	'zc_boss_player_health_multiplier': 100,
	'zc_boss_armor': 500,
	'zc_boss_speed_min': 0.86,
	'zc_boss_speed_max': 0.89,
	'zc_roundtime': 60,
	'zc_difficulty_health_multiplier': 20,
	'zc_difficulty_speed_multiplier': 0.04,
	'zc_difficulty_humanhealthsubtract_multiplier': 10,
	'zc_restricted_weapons': 'flashbang',
	'zc_bots': 13,
	'zc_humanbothelp': 0,
	'zc_minimumhumanplayers': 3,
	'zc_headshot_only': 0,
	'zc_few_humans_hp_bonus': 15,
	'zc_start_hp_value': 450,
	'zc_per_human_hp_loss': 10,
	'zc_human_speed': .85,
	'zc_classiczombiemode': 0,
	'zc_ending': 1,
	'zc_wdrounds': 9,
	'zc_supplydropload': 0
}

### Globals ###

respawn_rate = 25
humanrespawntime = 2
t_wave_remaining = None
ct_wave_remaining = None
difvote = None
irvote = None
survote = None
infection = 0
difficulty = 1
survival = 1
messages = {}
temp_zombies = 0
wins = -1
checked = 0
gameload = 0
changedmap = 1
humanbots = 0
humanbothelp = 0
tempz = 0
tempd = 0
knockback = 0
wdtemp = 0
bossess = []
boss_levels = ('12,24,48')
mapchange_finale = 36
rounds_to_win = 48
minimumhumans = 1
humandeathcount = {}
roundtime = 0
ideathcount = 0
dikills = 0
lastdifset = 0
losscounter = 0
wincounter = 0

### Loads ###
def load():
	add_downloads()
	for type in ammo:
		es.server.queuecmd('%s %s'%(type, ammo[type]))
	knife_bot()
	for a in sv_options:
		es.ServerVar(a).set(sv_options[a])
	set_pythonvars()
	if os.path.isfile(es.getAddonPath('zombiecontainment') + '/zombiecontainment.cfg'):
		es.server.queuecmd('es_xmexec ../addons/eventscripts/zombiecontainment/zombiecontainment.cfg')
	else:
		es.dbgmsg(0, 'Zombie Containment: Config not found')
	es.server.queuecmd('mp_restartgame 4')
	es.set('mp_limitteams', 0)
	es.set('mp_freezetime', 2)
	es.set('mp_timelimit', 999)
	es.set('mp_winlimit', 0)
	es.set('mp_maxrounds', 0)
	es.set('mp_autoteambalance', 0)
	es.set('sv_alltalk', 1)
	gamethread.delayed(4, resetAll)
	es.load('popup')
	es.load('zombiecontainment/zombiecontainment_dayandnight')
	es.load('zombiecontainment/healthregen')
	es.load('zombiecontainment/maplevels')
	es.load('zombiecontainment/infopopup')

	global difvote
	if not es.exists('saycommand', '!difficulty'): 
		es.regsaycmd('!difficulty', 'zombiecontainment/votedifficulty') 
	difvote = votelib.create('difvote', finishdif, submitdif)
	difvote.setquestion('Difficulty')
	difvote.addoption('Easy')
	difvote.addoption('Normal')
	difvote.addoption('Hard')
	difvote.addoption('Impossible')
	difvote.addoption('Damned')
	
	global irvote
	if not es.exists('saycommand', '!infection'): 
		es.regsaycmd('!infection', 'zombiecontainment/voteir') 
	if not es.exists('saycommand', '!respawn'): 
		es.regsaycmd('!respawn', 'zombiecontainment/voteir')
	irvote = votelib.create('irvote', finishir, submitir)
	irvote.setquestion('Infection or Respawn Mode')
	irvote.addoption('Respawn')
	irvote.addoption('Infection')
	
	global survote
	if not es.exists('saycommand', '!gametype'): 
		es.regsaycmd('!gametype', 'zombiecontainment/votesur')
	if not es.exists('saycommand', '!infection'): 
		es.regsaycmd('!infection', 'zombiecontainment/votesur')
	if not es.exists('saycommand', '!story'): 
		es.regsaycmd('!story', 'zombiecontainment/votesur')
	survote = votelib.create('survote', finishsur, submitsur)
	survote.setquestion('Story or Survival Mode')
	survote.addoption('Story')
	survote.addoption('Survival')			

	global botvote
	if not es.exists('saycommand', '!bothelp'): 
		es.regsaycmd('!bothelp', 'zombiecontainment/votebot') 
	botvote = votelib.create('botvote', finishbot, submitbot)
	botvote.setquestion('Add some bot teammates?')
	botvote.addoption('Yes')
	botvote.addoption('No')

	global botnvote
	if not es.exists('saycommand', '!botnumber'): 
		es.regsaycmd('!botnumber', 'zombiecontainment/votebotn') 
	botnvote = votelib.create('botnvote', finishbotn, submitbotn)
	botnvote.setquestion('Minimum number of Human team mates')
	botnvote.addoption('2')
	botnvote.addoption('3')
	botnvote.addoption('4')
	botnvote.addoption('5')
	botnvote.addoption('6')

	global storylvote
	storylvote = votelib.create('storylvote', finishstoryl, submitstoryl)
	storylvote.setquestion('Game Length')
	storylvote.addoption('Short')
	storylvote.addoption('Medium')		
	storylvote.addoption('Long')
	storylvote.addoption('Epic')
	
def unload():
	gamethread.delayedname(1.7, 'delayedbotquota', es.server.queuecmd, 'bot_quota 0')
	gamethread.delayedname(1.8, 'delayedbotkick', es.server.queuecmd, 'bot_kick all')
	es.server.queuecmd('mp_restartgame 2')
	es.server.queuecmd('ammo_338mag_max 1000')
	es.server.queuecmd('ammo_357sig_max 1000')
	es.server.queuecmd('ammo_45acp_max 1000')
	es.server.queuecmd('ammo_50AE_max 1000')
	es.server.queuecmd('ammo_556mm_box_max 1000')
	es.server.queuecmd('ammo_556mm_max 1000')
	es.server.queuecmd('ammo_57mm_max 1000')
	es.server.queuecmd('ammo_762mm_max 1000')
	es.server.queuecmd('ammo_9mm_max 1000')
	es.server.queuecmd('ammo_buckshot_max 1000')
	gamethread.delayedname(2.9, 'delayedservercfg', es.server.queuecmd, 'exec server.cfg')
	for loop in ['update_hud', 'check_quota', 'waveRepeat_delay', 'round_timer', 'noplayergamerestart', 'zombiekick', 'addhumanbot', 'addzombiebot', 'humankick']:
		gamethread.cancelDelayed(loop)
	for votecommand in ['!difficulty', '!gametype', '!infection', '!respawn', '!infection', '!story', '!bothelp', '!botnumber']:
		es.unregsaycmd(votecommand)
	survote.delete()	 
	difvote.delete()
	irvote.delete()
	botvote.delete()
	botnvote.delete()
	storylvote.delete()
	global gameload, wins, survival
	gameload = 0
	wins = -1
	survival = 1
	es.unload('popup')
	es.unload('zombiecontainment/zombiecontainment_dayandnight')
	es.unload('zombiecontainment/supplydrop')
	es.unload('zombiecontainment/healthregen')
	es.unload('zombiecontainment/maplevels')
	es.unload('zombiecontainment/infopopup')
	es.lightstyle(0, 'g')

### Events ###

def player_activate(ev):
	gamethread.cancelDelayed('update_hud')
	update_hud()
	gamethread.cancelDelayed('noplayergamerestart')
	userid = int(ev['userid'])
	humandeathcount[userid] = 0

def player_disconnect(ev):
	if survival == 0:
		if (len(playerlib.getUseridList('#human'))) == 0:
			gamethread.delayedname(400, 'noplayergamerestart', gamerestart)
	userid = int(ev['userid'])
	if humandeathcount.has_key(userid):
 		del humandeathcount[userid]	

def player_spawn(ev):
	userid = ev['userid']
	Player(userid).set_attributes(1)
	Player(userid).health_bonus()
	Player(userid).check_team()

def player_death(ev):
	userid = ev['userid']
	Player(userid).check_respawn()
	Player(userid).dissolve()
	Player(userid).play_sound()
	Player(userid).check_boss(userid)
	## if int(sv('zc_ending')) == 1:
	##	if wins > rounds_to_win:
	##		x, y, z = es.getplayerlocation(userid)
	##		es.server.queuecmd('est_blackhole %s %s %s 7'%(x, y, z))
	userid1 = int(ev['userid'])
	if ev['es_attackerteam'] != ev['es_userteam']:
		if humandeathcount.has_key(userid1):
			humandeathcount[userid1] += 1
			tempdeath = ideathcount - humandeathcount[userid1] 
			if tempdeath > 0:
				es.tell(userid, '#multi', '#lightgreen[Zombie Containment]: #green%s#default more respawn(s) as a human' %tempdeath)
			if tempdeath == 0:
				es.tell(userid, '#multi', '#lightgreen[Zombie Containment]: #defaultYour #greenNext#default death will turn you into a zombie')
			if tempdeath == -1:
				humandeathcount[userid1] = 0
				Player(userid).zombify()

def player_team(ev):
	Player(ev['userid']).check_team()
	if (len(playerlib.getUseridList('#human,#ct'))) > 0:
		gamethread.cancelDelayed('noplayergamerestart')

def es_map_start(ev):
	global checked, changedmap
	checked = 0
	changedmap = 1
	es.server.queuecmd('es_xmexec ../addons/eventscripts/zombiecontainment/zombiecontainment.cfg')
	add_downloads()
	knife_bot()
	gamethread.cancelDelayed('round_timer')
	gamethread.cancelDelayed('check_quota')
	gamethread.delayedname(3, 'check_quota', bot_check_loop)
	set_pythonvars()

def item_pickup(ev):
	Player(ev['userid']).check_restrict(ev['item'])
	if ev['item'] == 'c4': es.server.queuecmd('es_xfire %s weapon_c4 kill'%ev['userid'])

def player_hurt(ev):
	if not random.randint(0, 7):
		Player(ev['userid']).play_sound()
	if int(sv('zc_headshot_only')):
		if not int(ev['hitgroup']) == 1 and not ev['weapon'] in ['weapon_knife', 'weapon_hegrenade']:
			es.setplayerprop(ev['userid'], es.getplayerprop(ev['userid'], 'CBasePlayer.m_iHealth') + int(ev['dmg_health']))
	Player(ev['userid']).knockback(ev['attacker'], int(ev['dmg_health']))

def round_start(ev):
	set_pythonvars()
	global temp_zombies, infection, checked, wins, survival, difficulty, gameload, humanbothelp, bosses, tempz, tempd, wdtemp, minimumhumans
	bossess = []
	if gameload == 0:
		gameload = 1
		if int(sv('zc_survivalstart')) == 1:
			survival = 1
			es.doblock('zombiecontainment/maplevels/gtfoswitchoff')
		else:
			survival = 0
		if int(sv('zc_infectionstart')) == 1:
			infection = 1
		else:
			infection = 0
		if int(sv('zc_humanbothelp')) == 1:
			humanbothelp = 1
		else:
			humanbothelp = 0
		minimumhumans = int(sv('zc_minimumhumanplayers'))
		if int(sv('zc_supplydropload')) == 1:
			es.load('zombiecontainment/supplydrop')
	gamethread.cancelDelayed('round_timer')
	gamethread.cancelDelayed('update_hud')
	update_hud()
	if survival == 1:
		temp_zombies = 0
		difficulty = int(sv('zc_startingdifficulty'))
		wins = -1
		tempz = 0
		tempd = difficulty
		## es.msg('#multi', '#lightgreen[Zombie Containment]: #defaultSay !maps to change maps in survival mode.')
		for userid in playerlib.getUseridList('#human'):
			humandeathcount[int(userid)] = 0
	else:
		gamethread.delayedname(roundtime, 'round_timer', round_timer)
		wdtemp = 0
		if wins == 0:
			global losscounter, wincounter
			losscounter = 0 
			wincounter = 0
			difficulty = lastdifset
			temp_zombies = 0
			es.doblock('zombiecontainment/supplydrop/reset')
			for userid in playerlib.getUseridList('#all'):
				humandeathcount[int(userid)] = 0
	lightstyle()
	resetAll()
	gamethread.delayedname(10, 'check_quota', bot_check_loop)
	if humanbothelp == 1:
		global humanbots
		humancount = 0
		for a in playerlib.getUseridList('#human,#ct'):
			humancount += 1
		if humancount > 0:
			if humancount < minimumhumans:
				humanbots = minimumhumans - humancount
			else:
	 			humanbots = 0
		else:
	 		humanbots = 0
		if (len(playerlib.getUseridList('#bot,#ct'))) != humanbots:
			gamethread.cancelDelayed('addhumanbot')
			gamethread.delayedname(0, 'addhumanbot', humanbotcontrol)
	for userid in playerlib.getUseridList('#ct'):
		## es.setplayerprop(self.userid, 'CBasePlayer.localdata.m_flLaggedMovementValue', float(sv('zc_human_speed')))
		if int(sv('zc_supplydropload')) == 1:
			if survival == 1:
				gamethread.delayed(.3, es.setplayerprop, (userid, 'CCSPlayer.m_iAccount', 10000)) 	
			else:
				if wins == 0:
					gamethread.delayed(.3, es.setplayerprop, (userid, 'CCSPlayer.m_iAccount', 1000))
		else:
			if survival == 1:
				gamethread.delayed(.3, es.setplayerprop, (userid, 'CCSPlayer.m_iAccount', 10000)) 	
			else:
				if wins == 0:
					gamethread.delayed(.3, es.setplayerprop, (userid, 'CCSPlayer.m_iAccount', 10000))

def round_freeze_end(ev):
	if es.getUseridList():
		es.server.queuecmd('es_xfire %s hostage_entity kill'%es.getUseridList()[0])
		es.server.queuecmd('es_xfire %s func_bomb_target kill'%es.getUseridList()[0])
		es.server.queuecmd('es_xfire %s func_hostage_rescue kill'%es.getUseridList()[0])

def round_end(ev):
	round_restart_loader()
	set_pythonvars()
	gamethread.cancelDelayed('round_timer')
	global wins, temp_zombies, tempz, tempd, infection
	if wins > rounds_to_win:
		es.doblock('zombiecontainment/supplydrop/resetupgrades')
		es.doblock('zombiecontainment/maplevels/reset')
		es.doblock('zombiecontainment/supplydrop/resetclips')
		es.server.queuecmd('mp_restartgame 6')
		if int(sv('zc_ending')) == 1:
			wins = 0
			temp_zombies = 0
			es.msg('#multi', '#lightgreen[Zombie Containment]: #defaultYou have been sucked into Hell, there is no hope for the human race.  Game re-starting in 5 seconds.')
		if int(sv('zc_ending')) == 2:
			wins = 0
			temp_zombies = 0
			infection = 0
			## es.server.cmd("est_Freeze #all 4")
			for userid in playerlib.getUseridList('#all'): ## for userid in getusers(users):
				movetype = es.getplayerprop(userid, "CBaseEntity.movetype")
				es.setplayerprop(userid, "CBaseEntity.movetype", movetype - 2)
				gamethread.delayed(4, es.setplayerprop, 'userid, "CBaseEntity.movetype", movetype + 2')
			es.msg('#multi', '#lightgreen[Zombie Containment]: #defaultThere are no humans left on Earth, you are doomed to wander looking for brains until you starve to death.  Game re-starting in 5 seconds.')
	if survival == 0:
		global losscounter, difficulty, wincounter
		if ev['winner'] == 2:
			wincounter = 0
			losscounter += 1
			if losscounter == 2:
				if difficulty > 0:
					difficulty -= 1
				losscounter = 0
		elif ev['winner'] == 2:
			if losscounter > 0:
				losscounter -= 1
	else:
		es.doblock('zombiecontainment/supplydrop/resetwide')
		es.doblock('zombiecontainment/zombiecontainment_dayandnight/daylight')
		es.doblock('zombiecontainment/supplydrop/resetupgrades')	
	if es.getplayercount(3) == 0:
		es.msg('Not enough players to start')
	gamethread.cancelDelayed('update_hud')
	gamethread.cancelDelayed('waveRepeat_delay')
	gamethread.cancelDelayed('check_quota')
	if (len(playerlib.getUseridList('#bot,#t'))) < int(sv('zc_bots')):
		add_bots()
	if (len(playerlib.getUseridList('#bot,#t'))) > int(sv('zc_bots')):
		gamethread.delayedname(0, 'zombiekick', zombiebotkick)
	for player in playerlib.getPlayerList('#bot,#alive'):
		player.slay()
	remove_boss()

### Classes ###

class Player:
	def __init__(self, userid):
		self.userid = userid
		self.steamid = es.getplayersteamid(userid)

	def dissolve(self):
		gamethread.cancelDelayed('remove_ragdolls')
		gamethread.delayedname(1.9, 'remove_ragdolls', es.server.queuecmd, 'es_xfire %s cs_ragdoll kill'%self.userid)
		if survival == 1:
			global difficulty, tempz, tempd, dikills
			if temp_zombies > tempz:
				tempz += dikills
			if temp_zombies == tempz:
				tempz += dikills
				if tempd < 10:
					tempd += 1
				difficulty = tempd
				if tempd == 2: 		
					es.doblock('zombiecontainment/zombiecontainment_dayandnight/dusk1')
				if tempd == 4: 		
					es.doblock('zombiecontainment/zombiecontainment_dayandnight/dusk2')
					es.doblock('zombiecontainment/supplydrop/supplydrop')
				if tempd == 6: 		
					es.doblock('zombiecontainment/zombiecontainment_dayandnight/dusk3')
				if tempd == 8: 		
					es.doblock('zombiecontainment/zombiecontainment_dayandnight/midnight')
					es.doblock('zombiecontainment/supplydrop/supplydrop')
				gamethread.cancelDelayed('update_hud')
				update_hud()

	def check_restrict(self, weapon):
		if es.getplayerteam(self.userid) == 2:
			if not 'knife' in weapon:
				handle = es.getplayerhandle(self.userid)
				for index in es.createentitylist('weapon_%s'%weapon.replace('weapon_', '')):
					if handle == int(es.getindexprop(index, "CBaseEntity.m_hOwnerEntity")):
						es.server.queuecmd('es_xremove %s'%index)
						es.sexec(self.userid, 'use weapon_knife')
						playerlib.getPlayer(int(self.userid)).setWeaponColor(0, 0, 0, 0)
		elif weapon.replace('weapon_', '') in str(sv('zc_restricted_weapons')):
			handle = es.getplayerhandle(self.userid)
			for index in es.createentitylist('weapon_%s'%weapon.replace('weapon_', '')):
				if handle == int(es.getindexprop(index, "CBaseEntity.m_hOwnerEntity")):
					es.server.queuecmd('es_xremove %s'%index)
					es.tell(self.userid, '#multi', '#lightgreen[Zombie Containment]: #greenSorry, the #lightgreen%s #greenis restricted'%(weapon.replace('weapon_', '')))
					es.sexec(self.userid, 'lastinv')
					break

	def check_respawn(self):
		global temp_zombies
		if es.getplayerteam(self.userid) == 2:
			temp_zombies += 1
			## gamethread.delayed(2, es.server.queuecmd, 'est_spawn %s'%self.userid)
			gamethread.delayed(humanrespawntime, es.ServerCommand, 'es_setplayerprop %s CBasePlayer.m_lifeState 512' %self.userid)
			gamethread.delayed(humanrespawntime, es.ServerCommand, 'es_setplayerprop %s CCSPlayer.m_iPlayerState 0' %self.userid)
			gamethread.delayed(humanrespawntime, es.ServerCommand, 'es_spawnplayer %s' %self.userid)

	def zombify(self):
		if infection == 1:
			if es.exists('userid', self.userid):
				if playerlib.getPlayer(self.userid).get('teamid') == 3:
					if wins > rounds_to_win:				
						## es.server.queuecmd('est_team %s 2'%self.userid)
						spe.switchTeam(self.userid, 2)
						## gamethread.delayed(2, es.server.queuecmd, 'est_spawn %s'%self.userid)
						gamethread.delayed(humanrespawntime, es.ServerCommand, 'es_setplayerprop %s CBasePlayer.m_lifeState 512' %self.userid)
						gamethread.delayed(humanrespawntime, es.ServerCommand, 'es_setplayerprop %s CCSPlayer.m_iPlayerState 0' %self.userid)
						gamethread.delayed(humanrespawntime, es.ServerCommand, 'es_spawnplayer %s' %self.userid)
					else:
						if es.getlivingplayercount(3) >= 1:
							## es.server.queuecmd('est_team %s 2'%self.userid)
							spe.switchTeam(self.userid, 2)
							## gamethread.delayed(2, es.server.queuecmd, 'est_spawn %s'%self.userid)
							gamethread.delayed(humanrespawntime, es.ServerCommand, 'es_setplayerprop %s CBasePlayer.m_lifeState 512' %self.userid)
							gamethread.delayed(humanrespawntime, es.ServerCommand, 'es_setplayerprop %s CCSPlayer.m_iPlayerState 0' %self.userid)
							gamethread.delayed(humanrespawntime, es.ServerCommand, 'es_spawnplayer %s' %self.userid)

	def round_restart(self):
		if es.exists('userid', self.userid):
			if self.steamid != 'BOT':
				if playerlib.getPlayer(self.userid).get('teamid') == 2:
					## es.server.queuecmd('est_team %s 3'%self.userid)
					spe.switchTeam(self.userid, 3)
					playerlib.getPlayer(self.userid).set('health', 35000)

	def set_attributes(self, model):
		if es.getplayerteam(self.userid) == 2:
			es.setplayerprop(self.userid, 'CCSPlayer.m_iAccount', 0)
			if int(sv('zc_classiczombiemode')) == 1:
				self.set_attributes_default()
			else:
				if survival == 1:
					if random.randint(1, 100) < int(sv('zc_survival_boss_chance')):
						self.set_attributes_boss()
					else:
						if random.randint(1, 100) < int(sv('zc_survival_mutated_chance')):
							self.set_attributes_mutated()
						else:
							self.set_attributes_default()
				else:
					global changedmap
					if str(wins) in str(boss_levels).split(',') or wins > rounds_to_win or changedmap == 0 or wins == mapchange_finale:
						if random.randint(1, 100) < float(sv('zc_boss_chance')):
							self.set_attributes_boss()
						else:
							temp = wins * int(sv('zc_mutated_chance')) * (1 + (9 / rounds_to_win))
							if temp > 70:
								temp = 70
							if random.randint(1, 100) <= temp:
								self.set_attributes_mutated()
							else:
								self.set_attributes_default()
					else:
						temp = wins * int(sv('zc_mutated_chance')) * (1 + (9 / rounds_to_win))
						if temp > 70:
							temp = 70
						if random.randint(1, 100) <= temp:
							self.set_attributes_mutated()
						else:
							self.set_attributes_default()

	def set_attributes_default(self):
		playerlib.getPlayer(self.userid).set('model', random.choice(zombie_models))
		es.setplayerprop(self.userid, 'CBasePlayer.m_iHealth', random_value(health_min, health_max) + (float(sv('zc_zombie_player_health_multiplier')) * es.getplayercount()) + (float(sv('zc_difficulty_health_multiplier')) * difficulty))
		es.setplayerprop(self.userid, 'CCSPlayer.m_ArmorValue', random_value(armor_min, armor_max) + (float(sv('zc_zombie_player_armor_multiplier')) * es.getplayercount()))
		## es.setplayerprop(self.userid, 'CBasePlayer.localdata.m_flLaggedMovementValue', random_value(speed_min, speed_max) + (float(sv('zc_zombie_player_speed_multiplier')) * es.getplayercount()) + (float(sv('zc_difficulty_speed_multiplier')) * difficulty))
		playerlib.getPlayer(int(self.userid)).setWeaponColor(0, 0, 0, 0)

	def set_attributes_mutated(self):
		playerlib.getPlayer(self.userid).set('model', random.choice(mutated_models))
		es.tell(self.userid, '#multi', '#lightgreen[Zombie Containment]: #defaultYou have come back as a Mutated Zombie!')
		es.setplayerprop(self.userid, 'CBasePlayer.m_iHealth', random_value(mhealth_min, mhealth_max) + (float(sv('zc_mutated_player_health_multiplier')) * es.getplayercount()) + (float(sv('zc_difficulty_health_multiplier')) * difficulty))
		es.setplayerprop(self.userid, 'CCSPlayer.m_ArmorValue', random_value(marmor_min, marmor_max) + (marmor_multiplier * es.getplayercount()))
		## es.setplayerprop(self.userid, 'CBasePlayer.localdata.m_flLaggedMovementValue', random_value(speed_minm, speed_maxm) + (float(sv('zc_zombie_player_speed_multiplier')) * es.getplayercount()) + (float(sv('zc_difficulty_speed_multiplier')) * difficulty))
		playerlib.getPlayer(int(self.userid)).setWeaponColor(0, 0, 0, 0)

	def set_attributes_boss(self):	
		bossess.append(int(self.userid))
		es.tell(self.userid, '#multi', '#lightgreen[Zombie Containment]: #defaultYou have come back as a Boss Zombie!')	
		playerlib.getPlayer(self.userid).set('model', random.choice(boss_models))
		es.setplayerprop(self.userid, 'CBasePlayer.m_iHealth', float(sv('zc_boss_health')) + (wins * float(sv('zc_zombie_health_level_bonus_multiplier'))) + (float(sv('zc_zombie_player_health_multiplier')) * es.getplayercount()) + (float(sv('zc_difficulty_health_multiplier')) * difficulty))
		es.setplayerprop(self.userid, 'CCSPlayer.m_ArmorValue', float(sv('zc_boss_armor')) + (wins * float(sv('zc_zombie_armor_level_bonus_multiplier'))) + (float(sv('zc_zombie_player_armor_multiplier')) * es.getplayercount()))
		## es.setplayerprop(self.userid, 'CBasePlayer.localdata.m_flLaggedMovementValue', random_value(speed_minb, speed_maxb) + (float(sv('zc_zombie_player_speed_multiplier')) * es.getplayercount()) + (float(sv('zc_difficulty_speed_multiplier')) * difficulty))
		playerlib.getPlayer(int(self.userid)).setWeaponColor(0, 0, 0, 0)

	def check_boss(self, boss):
		if int(boss) in bossess:
			bossess.remove(int(boss))

	def knockback(self, attacker, damage):
		if int(attacker) in bossess:
			## knockback = random_value(20, 40)
			## knockback *= int(damage)
			knockback = 800
			x, y, z = playerlib.getPlayer(attacker).get('viewvector')
			es.setplayerprop(self.userid, 'CBasePlayer.localdata.m_vecBaseVelocity', '%s,%s,%s'%(x * knockback, y * knockback, z * knockback))
			usermsg.shake(self.userid, 8, 2)
			## for everyone in playerlib.nearCoord(es.getplayerlocation(attacker), 300, '#alive'): ## and not attacker and not self.userid:
			##	if everyone != attacker or self:
			##		x2, y2, z2 = playerlib.getPlayer(everyone).get('viewvector')
			##		knockback2 = -300
			##		es.setplayerprop(everyone, 'CBasePlayer.localdata.m_vecBaseVelocity', '%s,%s,%s'%(x2 * knockback2, y2 * knockback2, z2 * knockback2))	

	def play_sound(self):
		if es.getplayerteam(self.userid) == 2:
			sounds = []
			for a in range(1, 10):
				if a < 5:
					sounds.append('npc/zombie/moan_loop' + str(a))
				if a < 4:
					sounds.append('npc/zombie/zombie_die' + str(a))
					sounds.append('npc/zombie/zombie_alert' + str(a))
				if sounds < 7:
					sounds.append('npc/zombie/zombie_pain' + str(a))
				sounds.append('npc/zombie/zombie_voice_idle' + str(a))
			sound = random.choice(sounds)
			es.emitsound('player', self.userid, sound + '.wav', 0.75, 0.4)
			gamethread.delayed(3, es.stopsound, (self.userid, sound + '.wav'))

	def health_bonus(self):
		if int(sv('zc_few_humans_hp_bonus')):
			if es.getplayerteam(self.userid) == 3:
				if es.getplayercount(3) <= int(sv('zc_few_humans_hp_bonus')):	
					gamethread.delayed(0, es.setplayerprop, (self.userid, 'CBasePlayer.m_iHealth', max(100, int(sv('zc_start_hp_value')) - (int(sv('zc_per_human_hp_loss')) * es.getplayercount(3))) - (int(sv('zc_difficulty_humanhealthsubtract_multiplier')) * difficulty)))
					gamethread.delayed(2.5, es.setplayerprop, (self.userid, 'CBasePlayer.m_iHealth', max(100, int(sv('zc_start_hp_value')) - (int(sv('zc_per_human_hp_loss')) * es.getplayercount(3))) - (int(sv('zc_difficulty_humanhealthsubtract_multiplier')) * difficulty)))
					## es.setplayerprop(self.userid, 'CBasePlayer.localdata.m_flLaggedMovementValue', sv('zc_human_speed'))

	def hud(self):
		global temp_zombies, wins, difficulty, infection, respawn, survival
		humans = 0
		zombies = 0
		for userid in playerlib.getUseridList('#ct,#alive'):
			humans += 1
		zombies = temp_zombies
		usermsg.hudhint(self.userid, '%s\nHumans: %s \nZombies Killed: %s\nDifficulty: %s\n %s'%(timeofday[wins], humans, zombies, difficultylevel[difficulty], infectionorrespawn[infection]))

	def check_team(self):
		if es.exists('userid', self.userid):
			if infection == 0:
				if self.steamid != 'BOT':
					if playerlib.getPlayer(self.userid).get('teamid') == 2:
						## es.server.queuecmd('est_team %s 3'%self.userid)
						spe.switchTeam(self.userid, 3)
						## es.server.queuecmd('est_spawn %s'%self.userid)
						gamethread.delayed(humanrespawntime, es.ServerCommand, 'es_setplayerprop %s CBasePlayer.m_lifeState 512' %self.userid)
						gamethread.delayed(humanrespawntime, es.ServerCommand, 'es_setplayerprop %s CCSPlayer.m_iPlayerState 0' %self.userid)
						gamethread.delayed(humanrespawntime, es.ServerCommand, 'es_spawnplayer %s' %self.userid)
						if wins != 0:
							es.tell(self.userid, '#multi', '#lightgreen[Zombie Containment]: #defaultOnly bots can be zombies during Respawn Mode. Say #green!infection #defaultfor Infection Mode')
				else:
					if humanbots == 0:
						if not playerlib.getPlayer(self.userid).get('teamid') == 2:
							## es.server.queuecmd('est_team %s 2'%self.userid)
							spe.switchTeam(self.userid, 2)
			if infection == 1:
				if int(sv('zc_ending')) == 2:
					if wins > rounds_to_win:
						if playerlib.getPlayer(self.userid).get('teamid') == 3:
							## es.server.queuecmd('est_team %s 2'%self.userid)
							spe.switchTeam(self.userid, 2)
							## es.server.queuecmd('est_spawn %s'%self.userid)
							gamethread.delayed(humanrespawntime, es.ServerCommand, 'es_setplayerprop %s CBasePlayer.m_lifeState 512' %self.userid)
							gamethread.delayed(humanrespawntime, es.ServerCommand, 'es_setplayerprop %s CCSPlayer.m_iPlayerState 0' %self.userid)
							gamethread.delayed(humanrespawntime, es.ServerCommand, 'es_spawnplayer %s' %self.userid)
							self.set_attributes(1)

### Functions ###

def set_pythonvars():
	global health_min, health_max, speed_min, speed_max, zombie_models, mutated_models, boss_models, health_multiplier, speed_multiplier, armor_min, armor_max, armor_multiplier, speed_minm, speed_maxm, speed_minb, speed_maxb
	global ideathcount, remove_ragdolls, mhealth_min, mhealth_max, mhealth_multiplier, mspeed_min, mspeed_max, mspeed_multiplier, marmor_min, marmor_max, marmor_multiplier, dikills, roundtime
	zombie_models = str(sv('zc_zombie_models')).split(',')
	mutated_models = str(sv('zc_mutated_models')).split(',')
	boss_models = str(sv('zc_boss_models')).split(',')
	health_min, health_max, health_multiplier = tuple(int(sv('zc_zombie_health_' + x)) for x in ['min', 'max', 'level_bonus_multiplier'])
	speed_min, speed_max = tuple(int(sv('zc_zombie_speed_' + x)) for x in ['min', 'max'])
	speed_minm, speed_maxm = tuple(int(sv('zc_mutated_speed_' + x)) for x in ['min', 'max'])
	speed_minb, speed_maxb = tuple(int(sv('zc_boss_speed_' + x)) for x in ['min', 'max'])
	armor_min, armor_max, armor_multiplier = tuple(int(sv('zc_zombie_armor_' + x)) for x in ['min', 'max', 'level_bonus_multiplier'])
	mhealth_min, mhealth_max, mhealth_multiplier = tuple(int(sv('zc_mutated_health_' + x)) for x in ['min', 'max', 'level_bonus_multiplier'])
	mspeed_min, mspeed_max = tuple(int(sv('zc_mutated_speed_' + x)) for x in ['min', 'max'])
	marmor_min, marmor_max, marmor_multiplier = tuple(int(sv('zc_mutated_armor_' + x)) for x in ['min', 'max', 'level_bonus_multiplier'])
	remove_ragdolls = int(sv('zc_remove_ragdolls'))
	ideathcount = int(sv('zc_infectiondeathcount'))
	roundtime = int(sv('zc_roundtime'))
	dikills = int(sv('zc_difficultyincrease'))

def remove_boss():
	for userid in playerlib.getUseridList('#all'):
		Player(userid).check_boss(userid)
	
def add_downloads():
	if os.path.isfile(es.getAddonPath('zombiecontainment') + '/downloads.cfg'):
		for a in return_downloads():
			es.stringtable('downloadables', a)

def knife_bot():
	es.server.queuecmd('bot_join_after_player 0')
	es.server.queuecmd('bot_difficulty 2')
	es.server.queuecmd('bot_allow_rogues 0')
	es.server.queuecmd('bot_auto_follow 1')
	es.server.queuecmd('bot_defer_to_human 0')
	es.server.queuecmd('bot_auto_vacate 0')
	es.server.queuecmd('bot_quota_mode normal')
	es.server.queuecmd('bot_allow_grenades 0')
	es.set('mp_limitteams', 0)
	es.set('mp_autoteambalance', 0)

def add_bots():
	if (len(playerlib.getUseridList('#bot,#t'))) < int(sv('zc_bots')):
		es.ServerCommand('bot_add_t')
		gamethread.delayedname(.1, 'addzombiebot', add_bots)
	else:
		gamethread.cancelDelayed('addzombiebot')

def humanbotcontrol():
	global humanbots
	if (len(playerlib.getUseridList('#bot,#ct'))) <= humanbots:
		if (len(playerlib.getUseridList('#bot,#ct'))) < humanbots:
			es.ServerCommand('bot_add_ct')
			new_bot_quota = es.ServerVar('bot_quota') + 1
			es.server.queuecmd('bot_quota %s'%new_bot_quota)
			gamethread.delayedname(.2, 'addhumanbot', humanbotcontrol)
		else:
			gamethread.cancelDelayed('addhumanbot')
	else:
		gamethread.delayedname(.1, 'humankick', humanbotkick)
		gamethread.cancelDelayed('addhumanbot')

def humanbotkick():
	global humanbots
	if (len(playerlib.getUseridList('#bot,#ct'))) > humanbots:
		botlist = playerlib.getUseridList('#bot,#ct')
		botid = random.choice(botlist)
		es.ServerCommand('kickid '+str(botid))
		new_bot_quota = es.ServerVar('bot_quota') - 1
		es.server.queuecmd('bot_quota %s'%new_bot_quota)
		gamethread.delayedname(.1, 'humankick', humanbotkick)
		if new_bot_quota == int(sv('zc_bots')):
			minimumhumans = int(sv('zc_minimumhumanplayers')) 
	else:
		gamethread.cancelDelayed('humankick')

def zombiebotkick():
	if (len(playerlib.getUseridList('#bot,#t'))) > int(sv('zc_bots')):
		botlist = playerlib.getUseridList('#bot,#t')
		botid = random.choice(botlist)
		es.ServerCommand('kickid '+str(botid))
		gamethread.delayedname(.1, 'zombiekick', zombiebotkick)
	else:
		gamethread.cancelDelayed('zombiekick')

def kick_bots():
	es.server.queuecmd('bot_kick')

def lightstyle():
	if str(wins) in str('0, 10, 20, 30, 40, 50, 60, 70, 80').split(','):
		es.doblock('zombiecontainment/zombiecontainment_dayandnight/dusk1')
	if str(wins) in str('1, 11, 21, 31, 41, 51, 61, 71, 81').split(','):
		es.doblock('zombiecontainment/zombiecontainment_dayandnight/dusk2')
	if str(wins) in str('2, 12, 22, 32, 42, 52, 62, 72, 82').split(','):
		es.doblock('zombiecontainment/zombiecontainment_dayandnight/dusk3')
	if str(wins) in str('3, 13, 23, 33, 43, 53, 63, 73, 83').split(','):
		es.doblock('zombiecontainment/zombiecontainment_dayandnight/midnight')
	if str(wins) in str('4, 14, 24, 34, 44, 54, 64, 74, 84').split(','):
		es.doblock('zombiecontainment/zombiecontainment_dayandnight/dawn1')
	if str(wins) in str('5, 15, 25, 35, 45, 55, 65, 75, 85').split(','):
		es.doblock('zombiecontainment/zombiecontainment_dayandnight/dawn2')
	if str(wins) in str('6, 16, 26, 36, 46, 56, 66, 76, 86').split(','):
		es.doblock('zombiecontainment/zombiecontainment_dayandnight/daylight')

def change_teams():
	for userid in es.getUseridList():
		Player(userid).check_team()

def finishdif(votename, win, winname, winvotes, winpercent, total, tie, cancelled): 
	if cancelled: 
		es.msg("The vote "+votename+" was cancelled.") 
	else: 
		es.msg("The option "+winname+" ["+str(win)+"] has won the vote with "+str(winvotes)+" ("+str(winpercent)+"%) votes.") 
	global difficulty, lastdifset
	if winname == 'Easy':
		difficulty = 0
	if winname == 'Normal':
		difficulty = 1
	if winname == 'Hard': 
		difficulty = 2
	if winname == 'Impossible': 
		difficulty = 3
	if winname == 'Damned': 
		difficulty = 4
	lastdifset = difficulty

def finishbot(votename, win, winname, winvotes, winpercent, total, tie, cancelled): 
	if cancelled: 
		es.msg("The vote "+votename+" was cancelled.") 
	else: 
		es.msg("The option "+winname+" ["+str(win)+"] has won the vote with "+str(winvotes)+" ("+str(winpercent)+"%) votes.") 
	global humanbothelp
	if winname == 'Yes':
		humanbothelp = 1
		botnvote.start(30)
	if winname == 'No':
		humanbothelp = 0

def finishbotn(votename, win, winname, winvotes, winpercent, total, tie, cancelled): 
	if cancelled: 
		es.msg("The vote "+votename+" was cancelled.") 
	else: 
		es.msg("The option "+winname+" ["+str(win)+"] has won the vote with "+str(winvotes)+" ("+str(winpercent)+"%) votes.") 
	global minimumhumans
	minimumhold = minimumhumans
	if winname == '2':
		minimumhumans = 2
	if winname == '3':
		minimumhumans = 3
	if winname == '4': 
		minimumhumans = 4
	if winname == '5': 
		minimumhumans = 5
	if winname == '6': 
		minimumhumans = 6
	if survival == 1:
		es.server.queuecmd('mp_restartgame 1')

def finishir(votename, win, winname, winvotes, winpercent, total, tie, cancelled): 
	if cancelled: 
		es.msg("The vote "+votename+" was cancelled.") 
	else: 
		es.msg("The option "+winname+" ["+str(win)+"] has won the vote with "+str(winvotes)+" ("+str(winpercent)+"%) votes.") 
	global infection
	if winname == 'Respawn':
		infection = 0
		change_teams()
	elif winname == 'Infection':
		infection = 1

def finishsur(votename, win, winname, winvotes, winpercent, total, tie, cancelled): 
	if cancelled: 
		es.msg("The vote "+votename+" was cancelled.") 
	else: 
		es.msg("The option "+winname+" ["+str(win)+"] has won the vote with "+str(winvotes)+" ("+str(winpercent)+"%) votes.") 
	global survival, difficulty, wins, temp_zombies, tempz, tempd, infection
	if winname == 'Story':
		if survival == 1:
			global losscounter, wincounter
			losscounter = 0 
			wincounter = 0
			wins = 0
			survival = 0
			difficulty = 1
			infection = 0
			temp_zombies = 0
			es.server.queuecmd('mp_restartgame 10')
			es.doblock('zombiecontainment/supplydrop/resetupgrades')
			es.doblock('zombiecontainment/supplydrop/reset')
			gamethread.delayed(10, es.doblock, 'zombiecontainment/maplevels/reset')
			es.doblock('zombiecontainment/supplydrop/resetclips')
			storylvote.start(30)
			difvote.start(30)
			botvote.start(30)
	elif winname == 'Survival':
		if survival == 0:
			es.msg('#multi', '#lightgreen[Zombie Containment]: #green[Survival Mode]: #defaultEndabled. See how many zombies you can kill!')
			survival = 1
			difficulty = int(sv('zc_startingdifficulty'))
			infection = 1
			tempz = 0
			tempd = difficulty
			temp_zombies = 0
			es.server.queuecmd('mp_restartgame 10')
			es.doblock('zombiecontainment/supplydrop/resetwide')
			gamethread.delayed(10, es.doblock, 'zombiecontainment/maplevels/levelpickfun')
			es.doblock('zombiecontainment/maplevels/gtfoswitchoff')
			difvote.start(30)
			botvote.start(30)

def finishstoryl(votename, win, winname, winvotes, winpercent, total, tie, cancelled): 
	if cancelled: 
		es.msg("The vote "+votename+" was cancelled.") 
	else: 
		es.msg("The option "+winname+" ["+str(win)+"] has won the vote with "+str(winvotes)+" ("+str(winpercent)+"%) votes.") 
	global boss_levels, mapchange_finale, rounds_to_win
	if winname == 'Short':
		boss_levels = ('8,24')
		mapchange_finale = 16
		rounds_to_win = 24
	if winname == 'Medium':
		boss_levels = ('12,24,48')
		mapchange_finale = 36
		rounds_to_win = 48
	if winname == 'Long':
		boss_levels = ('14,28,42,70')
		mapchange_finale = 56
		rounds_to_win = 70
	if winname == 'Epic':
		boss_levels = ('14,28,42,56,90')
		mapchange_finale = 75
		rounds_to_win = 90

def submitdif(userid, votename, choice, choicename):
	es.msg("#multi", "#lightgreen[Zombie Containment]: #greenVote for #lightgreen" + choicename) 

def submitbot(userid, votename, choice, choicename):
	es.msg("#multi", "#lightgreen[Zombie Containment]: #greenVote for #lightgreen" + choicename)

def submitbotn(userid, votename, choice, choicename):
	es.msg("#multi", "#lightgreen[Zombie Containment]: #greenVote for #lightgreen" + choicename)

def submitir(userid, votename, choice, choicename):
	es.msg("#multi", "#lightgreen[Zombie Containment]: #greenVote for #lightgreen" + choicename) 

def submitsur(userid, votename, choice, choicename):
	es.msg("#multi", "#lightgreen[Zombie Containment]: #greenVote for #lightgreen" + choicename)

def submitstoryl(userid, votename, choice, choicename):
	es.msg("#multi", "#lightgreen[Zombie Containment]: #greenVote for #lightgreen" + choicename)

def votedifficulty():
	difvote.start(30)
 
def voteir():
	irvote.start(30)

def votesur():
	survote.start(30)

def votebot():
	botvote.start(30)

def votebotn():
	botnvote.start(30)

def votestoryl():
	storylvote.start(30)

def round_restart_loader():
	for userid in es.getUseridList():
		Player(userid).round_restart()

def resetAll():
	global t_wave_remaining, ct_wave_remaining
	t_wave_remaining  = respawn_rate
	ct_wave_remaining = respawn_rate
	gamethread.cancelDelayed('waveRepeat_delay')
	gamethread.delayedname(1, 'waveRepeat_delay', waveRepeat)

def gamerestart():
	global survival, infection, difficulty, wins, temp_zombies
	if survival == 0:
		wins = 0
		temp_zombies = 0
		difficulty = 1
		survival = 1
		infection = 1
		temp_zombies = 0
		es.server.queuecmd('mp_restartgame 5')
		es.doblock('zombiecontainment/supplydrop/resetwide')

### Returns ###

def random_value(low, high):
	return random.randint(int(low * 1000), int(high * 1000)) / 1000.0

def return_downloads():
	if os.path.isfile(es.getAddonPath('zombiecontainment') + '/downloads.cfg'):
		a = open(es.getAddonPath('zombiecontainment') + '/downloads.cfg', 'r')
		b = a.readlines()
		a.close()
		return map(lambda x: x.replace('\n', '').replace('\\', '/').replace('downloadable', ''), filter(lambda x: not x.startswith('//') and not x == '\n', b))
	else:
		es.dbgmsg(0, 'ERROR: No downloads.cfg found for Zombie Containment!')

### Loops ###

def round_timer():
	gamethread.cancelDelayed('round_timer')
	gamethread.delayedname(roundtime, 'round_timer', round_timer)
	global wins, rounds_to_win, temp_zombies, wdtemp, wincounter, losscounter
	wdtemp = wdtemp + 1
	if wdtemp > int(sv('zc_wdrounds')) - 1:
		wdtemp = 0
		es.doblock('zombiecontainment/supplydrop/supplydrop')
	if (len(playerlib.getUseridList('#human,#ct'))) > 0:
		wins += 1
		if str(wins) in str(boss_levels).split(',') or wins == mapchange_finale:
			if wins < rounds_to_win:
				global changedmap
				changedmap = 0
				## if wins != int(sv('zc_mapchange_finale')):			
				if wins != mapchange_finale:
					gamethread.delayed(roundtime, es.doblock, ('zombiecontainment/maplevels/levelpick'))
					es.msg('#multi', '#lightgreen[Zombie Containment]: #defaultZombies have evolved here, leave this area to search for weaker zombies.')
				else:
					gamethread.delayed(roundtime, es.doblock, ('zombiecontainment/maplevels/levelpickfinale'))
					es.msg('#multi', '#lightgreen[Zombie Containment]: #defaultZombies have evolved here, leave this area to search for weaker zombies.')
				es.doblock('zombiecontainment/maplevels/gtfoswitchon')
		if wins > rounds_to_win:
			if int(sv('zc_ending')) == 0:
				es.msg('#multi', '#lightgreen[Zombie Containment]: #defaultCongratulations on defeating all the zombies, game re-starting in 5 seconds.')
				wins = 0
				temp_zombies = 0
				es.doblock('zombiecontainment/supplydrop/resetupgrades')
				es.doblock('zombiecontainment/maplevels/reset')
				es.doblock('zombiecontainment/supplydrop/resetclips')
				es.server.queuecmd('mp_restartgame 6')
			if int(sv('zc_ending')) == 2:
				global difficulty, infection
				difficulty = 50
				infection = 1
			gamethread.cancelDelayed('round_timer')
			gamethread.cancelDelayed('waveRepeat_delay')
		if losscounter > 0:
			losscounter -= 1
		wincounter += 1
		if wincounter > rounds_to_win / 6:
			if difficulty < 10:
				difficulty += 1
			wincounter = 0
		lightstyle()
		gamethread.cancelDelayed('update_hud')
		update_hud()

def bot_check_loop():
	gamethread.cancelDelayed('check_quota')
	gamethread.delayedname(10, 'check_quota', bot_check_loop)
	if infection == 0:
		global humanbots
		if humanbothelp == 1:
			humancount = 0
			for a in playerlib.getUseridList('#human,#ct'):
				humancount += 1
			if humancount > 0:
				if humancount < minimumhumans:
					## humanbots = int(sv('zc_minimumhumanplayers')) - humancount
					humanbots = minimumhumans - humancount
				else:
		 			humanbots = 0
			else:
		 		humanbots = 0
			if (len(playerlib.getUseridList('#bot,#ct'))) != humanbots:
				gamethread.cancelDelayed('addhumanbot')
				gamethread.delayedname(1, 'addhumanbot', humanbotcontrol)
		if humanbothelp == 0:
			humanbots = 0
			if (len(playerlib.getUseridList('#bot,#ct'))) != humanbots:
				gamethread.cancelDelayed('addhumanbot')
				gamethread.delayedname(1, 'addhumanbot', humanbotcontrol)
		if (len(playerlib.getUseridList('#bot,#t'))) < int(sv('zc_bots')):
			add_bots()
		if (len(playerlib.getUseridList('#bot,#t'))) > int(sv('zc_bots')):
			gamethread.delayedname(.4, 'zombiekick', zombiebotkick)	

def update_hud():
	gamethread.cancelDelayed('update_hud')
	gamethread.delayedname(1, 'update_hud', update_hud)
	for userid in es.getUseridList():
		Player(userid).hud()

def waveRepeat():
	gamethread.cancelDelayed('waveRepeat_delay')
	gamethread.delayedname(1, 'waveRepeat_delay', waveRepeat)
	global t_wave_remaining, ct_wave_remaining
	for userid in es.getUseridList():
		team = es.getplayerteam(userid)		
		if playerlib.getPlayer(userid).get('isdead'):
			if team == 2:
				es.centertell(userid, 'Time until respawn: %s' % t_wave_remaining)
				if t_wave_remaining < 1:
					## es.centertell(userid, '')
					## es.server.queuecmd('est_spawn %s' % userid)
					gamethread.delayed(0, es.ServerCommand, 'es_setplayerprop %s CBasePlayer.m_lifeState 512' % userid)
					gamethread.delayed(0, es.ServerCommand, 'es_setplayerprop %s CCSPlayer.m_iPlayerState 0' % userid)
					gamethread.delayed(0, es.ServerCommand, 'es_spawnplayer %s' % userid)
			elif team == 3:
				es.centertell(userid, 'Time until respawn: %s' % ct_wave_remaining)
				if ct_wave_remaining < 1:
					## es.centertell(userid, '')
					## es.server.queuecmd('est_spawn %s' % userid)
					gamethread.delayed(0, es.ServerCommand, 'es_setplayerprop %s CBasePlayer.m_lifeState 512' % userid)
					gamethread.delayed(0, es.ServerCommand, 'es_setplayerprop %s CCSPlayer.m_iPlayerState 0' % userid)
					gamethread.delayed(0, es.ServerCommand, 'es_spawnplayer %s' % userid)
		else:
			if team == 2:
				if es.getlivingplayercount(2) == 1:
					if es.getplayercount(2) > 1:
						es.centertell(userid, 'Stay alive, reinforcements in %s' % t_wave_remaining)
			elif team == 3:
				if es.getlivingplayercount(3) == 1:
					if es.getplayercount(3) > 1:
						es.centertell(userid, 'Stay alive, reinforcements in %s' % ct_wave_remaining)
	if t_wave_remaining < 1:
		t_wave_remaining = respawn_rate
	if ct_wave_remaining < 1:
		ct_wave_remaining = respawn_rate
	t_wave_remaining -= 1
	ct_wave_remaining -= 1

### Call Functions ###

gamethread.delayed(0, round_timer)
gamethread.delayed(0, update_hud)
gamethread.delayed(0, bot_check_loop)
gamethread.delayed(0, waveRepeat)