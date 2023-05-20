with this script you can :

change the rate of fire of any gun and knife slash (stab doesn't fire the weapon_fire event so it can't be changed).

change the recoil of any gun (glock has no recoil by default).

you can add a 2nd fire mode to pistols so they fire fully automatic.

-----

regarding automatic pistols :

you switch between normal mode and automatic mode with the secondary attack command similar to the glock's burst mode.

you can't use the glock's burst mode or the usp's silencer if you enable the automatic mode for them.

-----

regarding rate of fire :

rate of fire also changes the glock and famas burst fire rate.

-----

rof (rate of fire) multipliers - 0 has no delay between shots, 1 is default, over 1 makes the weapon fire slower, smaller than 1 makes the weapon fire faster.

recoil1 + recoil2 multipliers - 0 has no recoil, 1 is default, smaller than 1 reduces recoil, anything over 1 increases recoil.

automatic mode - 0 off, 1 on, pistols only.

-----

there are a few non game breaking glitches :

clients can't see all the decals fired from their weapon if the rate of fire is high, this has no effect in third person i.e others see all the decals

clients can't hear all the weapon sounds from their weapon if the rate of fire is high, this has no effect in third person i.e others hear all the weapon sounds.

clients will get animation glitches when changing fire modes on the glock or usp, they will normally see the last animation played, they don't have to wait for the animation to stop before firing though.

clients will see some recoil if the recoil is set to 0 but the bullets will impact with no recoil i.e they will impact lower than the crosshair.

clients will see choppy recoil if you increase the recoil, the higher the recoil the more choppy it becomes.

-----

WARNING !!!!! setting recoil to extremely high values WILL crash the server and the client firing the weapon.

-----

you shouldn't need to change any code in the main script only the multipliers in the weapon database.

