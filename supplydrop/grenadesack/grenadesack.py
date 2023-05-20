###################################################
#          GrenadeSack v1.0 By JoeyT2008          #
###################################################
#               ```````.........                  #
#         `.://:///::::::///++ooo+                #
#        `+ohmo+++ooo+ooossosyyyys-               #
#        `:/oho++++os+oossossyhyyys.              #
#            -o+o+++oooo+ossssyyyyys.             #
#            .o+++oooooo+/+ososo+++os-            #
#            `oo++++oo++osdNddhydhys+/.           #
#            `shys+:o+oyhNNyoohddmhyys//`         #
#           `osyh+:::ssodNsoo++syhhhyyy/+````     #
#          -+shddhhs+ddmMNmhyssooyhhhyys//..-+    #
#        .+ssyyyyyy+sdNNNmmNNNmho:/yhdhy:/  `o    #
#      `/osyyyyyyyyoomNNNddmmNNNmy/:hhho/o//+/    #
#     `+syyyyyssssyy+ymNmhddmmNNNmdo:yy/sy-       #
#    `osyyyyyssssssyyosdmdhdddmmNNNdo/+syys`      #
#   `+syyyyyssooooosyyyosyhddddmmmdsoo/hmyy+      #
#   /syyyyyssoo+++ossyyyhsssoosssshhdh++mdyy-     #
#  .oyyyyyysso++++ossoyyyyshhydhmmNMNmh-ohhys     #
#  /syyyyyysso++++osssyyhhhhdhddmmmNNNdo.yhhy:    #
# `osyyyyyysoo+++oossyhhhhdddddddmmNNNmy.+yhys    #
# .osyyyyysssoo+ooosyyhhhhdddddddmmmNNmh/.yhyy.   #
# -osyyyyyysssooosssyyhhhhddddddhhdmNmmho`ohhy/   #
# oossyyyyyssssssssyosyssshdsydyhhydmmddd/:yhyo   #
# +syyyyyyyyyssssyyy/sysoohsyyyhyhddNNNmy..yhyy`  #
# `+osyyyyyyyyyyyyhhyhhhhddddddddddddmdy: `shyy.  #
#  :osssyyyyyyyyyyyyhhhhhhdddddddddmmmhs`  oyyy-  #
#  `+ossyyyyyyyyyyyyhhhhhhhhhhddddddmdy:   +yyy-  #
#   .+ssssyyyyyyysyyyhhyyhhhhhhhhhdddh+    /yys-  #
#    .+sssyyyssyysyyhhyyhhyhhhhhhdddho`    /yys-  #
#     .osyyyyyyyyyhhhhhhyhhhhddddddyo`     /yys-  #
#      `+syyyyyhhhhhhhhhhhhddddddhy+`      /yys.  #
#       `:syyyhhhhhhhhhhhhdddddhhs:        +yys`  #
#         `/yyhhhhhhhhhddddddhhy/`         syys`  #
#           .+yhhhhhdddddddddds`           .sy+   #
#           `/syhhhhhdddddmmddy/           `ss.   #
#           .osyyysssyyhhhddddy:           /s:    #
#              .--:://++++/:-`             .`     #
###################################################
#      PLEASE REPORT ANY BUGS TO "JoeyT2006"      #
###################################################

###################################################
#            GrenadeSack Configuration            #
###################################################

# Maximum HE Grenades a player can hold. 0 = Unlimited.
# Ingame Var: gs_max_hegrenade
max_he = 8

# Maximum Flashbangs a player can hold. 0 = Unlimited.
# Ingame Var: gs_max_flashbang
max_fb = 1

# Maximum Smoke Grenades a player can hold. 0 = Unlimited.
# Ingame Var: gs_max_smokegrenade
max_sg = 2

# Maximum grenades allowed in the map, if the ammount exceeds this, GrenadeSack is disabled to stop lag. 0 = Unlimited.
# Ingame Var: gs_max_grenades
max_grenades = 10

# The max distance between a player and grenade before it is picked up.
# Ingame Var: gs_max_distance
max_distance = 70

###################################################
#        !!!DO NOT EDIT BELOW THIS LINE!!!        #
###################################################

# Imports
import es, playerlib, gamethread, vecmath

# Dicts and Lists
players = {}
max = {0: int(max_he), 1: int(max_fb), 2: int(max_sg)}
defmax = {0: 1, 1: 2, 2: 1}
grenades = {"hegrenade": 0, "flashbang": 1, "smokegrenade": 2}
short_grenades = {"hegrenade": "he", "flashbang": "fb", "smokegrenade": "sg"}

# ServerVar's
max_he = es.ServerVar("gs_max_hegrenade", max_he)
max_fb = es.ServerVar("gs_max_flashbang", max_fb)
max_sg = es.ServerVar("gs_max_smokegrenade", max_sg)
max_grenades = es.ServerVar("gs_max_grenades", max_grenades)
max_distance = es.ServerVar("gs_max_distance", max_distance)

# Public Variable
es.ServerVar("grenadesack_ver", 1.0, "The version of GrenadeSack you are running.").makepublic()

# EventScripts Blocks
def load():
    es.addons.registerClientCommandFilter(BuyFilter)
    for userid in playerlib.getUseridList("#all"):
        Setup(userid)
    EntSearch()
    es.doblock('corelib/noisy_on')

def unload():
    gamethread.cancelDelayed("EntSearch")
    es.addons.unregisterClientCommandFilter(BuyFilter)
    es.doblock('corelib/noisy_off')

# Events
def player_activate(event_var):
    Setup(event_var["userid"])

def player_spawn(event_var):
    Setup(event_var["userid"], 1)
'''
def round_start(event_var):
    es.msg("#multi", "#green[GrenadeSack] #defaultYou can carry up to:")
    frags = str(max[0])
    if frags == "0":
        frags = "Unlimited"
    flashes = str(max[1])
    if flashes == "0":
        flashes = "Unlimited"
    smokes = str(max[2])
    if smokes == "0":
        smokes = "Unlimited"
    es.msg("#multi", "#green[GrenadeSack] #lightgreen%s#default Frags, #lightgreen%s#default Flashes and #lightgreen%s#default Smokes!" % (frags, flashes, smokes))
'''
def weapon_fire(event_var):
    global players
    if event_var["weapon"] in grenades:
        nadetype = int(grenades[event_var["weapon"]])
        short = short_grenades[event_var["weapon"]]
        nades = int(players[event_var["userid"]][nadetype]) - 1
        if nades < 0:
            nades = 0
        players[event_var["userid"]][nadetype] = nades

def item_pickup(event_var):
    if event_var["item"] in grenades:
        grenade = event_var["item"]
        if int(players[event_var["userid"]][grenades[grenade]]) == 0:
            players[event_var["userid"]][grenades[grenade]] = 1

# Custom Blocks
def BuyFilter(userid, args):
    if args[0].lower() == "buy" and len(args) > 1:
        grenade = args[1]
        if grenade in grenades:
            cash = int(playerlib.getPlayer(userid).get("cash")) - 300
            if cash >= 0:
                if playerlib.getPlayer(userid).get(short_grenades[grenade]) >= defmax[grenades[grenade]]:
                    if max[grenades[grenade]] == 0 or playerlib.getPlayer(userid).get(short_grenades[grenade]) < max[grenades[grenade]]:
                        GiveGrenade(userid, None, grenade)
                        playerlib.getPlayer(userid).set("cash", cash)
                        return False
    return True

def Setup(userid, blank=None):
    global players
    userid = str(userid)
    players[userid] = {}
    if not blank == 1:
        players[userid][0] = 0
        players[userid][1] = 0
        players[userid][2] = 0
    else:
        players[userid][0] = playerlib.getPlayer(userid).get("he")
        players[userid][1] = playerlib.getPlayer(userid).get("fb")
        players[userid][2] = playerlib.getPlayer(userid).get("sg")

def EntSearch():
    global max
    max = {0: int(max_he), 1: int(max_fb), 2: int(max_sg)}
    maxlen = 0
    for grenade in grenades:
        maxlen += len(es.createentitylist("weapon_%s" % grenade))
    if maxlen <= int(max_grenades) or int(max_grenades) == 0:
        players = {}
        for grenade in grenades:
            for index in es.createentitylist("weapon_%s" % grenade):
                userid = getClosest(playerlib.getUseridList("#alive"), index)
                if not userid == None:
                    GiveGrenade(userid, index, grenade)
    gamethread.delayedname(0.1, "EntSearch", EntSearch)


def getClosest(playerlist, index):
    max = 500000
    indexloc = es.getindexprop(index, "CBaseEntity.m_vecOrigin")
    for userid in playerlist:
        playerloc = es.getplayerprop(userid, "CBaseEntity.m_vecOrigin")
        dist = vecmath.distance(playerloc, indexloc)
        if dist < max:
            max = dist
            closest = userid
    if max <= int(max_distance):
        return closest
    else:
        return None

def GiveGrenade(userid, index, grenade):
    userid = str(userid)
    nades = int(players[userid][grenades[grenade]])
    if max[grenades[grenade]] == 0 and not nades == 0 or nades < max[grenades[grenade]] and not nades == 0:
        if not index == None:
            es.server.cmd("es_xremove %s" % str(index))
        nades += 1
        players[userid][grenades[grenade]] = nades
        playerlib.getPlayer(userid).set(short_grenades[grenade], "%d" % nades)
        es.emitsound("player", userid, "items/itempickup.wav", 1.0, 0.6)
        es.emitsound("player", userid, "items/itempickup.wav", 1.0, 0.6)