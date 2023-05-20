# ./addons/eventscripts/_libs/python/cfglib.py

import es
import os.path
import string

import psyco
psyco.full()


class AddonCFG:
   TYPE_TEXT    = 0
   TYPE_CVAR    = 1
   TYPE_COMMAND = 2

   gamedir = str(es.ServerVar('eventscripts_gamedir'))

   """ Begin AddonCFG """

   def __init__(self, cfgpath, indention=3):
      self.cfgpath   = cfgpath
      self.indention = indention

      self.cfglist  = []
      self.commands = set()
      self.cvars    = {}

   """ Public functions """

   def text(self, text, comment=True):
      """Adds the given text to the config"""
      if not text.strip(): comment = False
      self.cfglist.append((self.TYPE_TEXT, ('// ' if comment else '') + text + '\n'))

   def cvar(self, name, default, description=''):
      """Adds the named cvar to the config and returns a ServerVar instance"""
      var = self.cvars[name] = (name, default, description)
      self.cfglist.append((self.TYPE_CVAR, var))

      return es.ServerVar(name, default, description)

   def command(self, name):
      """Designates a place for the named server command in the config"""
      self.commands.add(name)

      self.cfglist.append((self.TYPE_COMMAND, name))

   def write(self):
      """Writes the config to file"""
      current_cfg = self._parse()
      indention   = ' ' * self.indention

      cfgfile = open(self.cfgpath, 'w')

      # Write the config to file

      for ltype, data in self.cfglist:
         # Write text
         if ltype == self.TYPE_TEXT:
            cfgfile.write(data)

         # Write cvar
         elif ltype == self.TYPE_CVAR:
            name, default, description = data

            cfgfile.write('\n')
            if description:
               cfgfile.write('// %s\n' % description)

            if name in current_cfg:
               cfgfile.write(indention + current_cfg[name][0] + '\n')
               del current_cfg[name]

            else:
               cfgfile.write(indention + name + ' ' + ('\"%s\"' if isinstance(default, str) else '%s') % default + '\n')

         # Write server command
         elif ltype == self.TYPE_COMMAND:
            if data in current_cfg:
               cfgfile.write('\n')
               for old_line in current_cfg[data]:
                  cfgfile.write(indention + old_line + '\n')
               del current_cfg[data]

      # Write extraneous commands or variables
      if current_cfg:
         cfgfile.write('\n')
      for name in sorted(filter(lambda x: es.exists('variable', x) or es.exists('command', x), current_cfg)):
         for line in current_cfg[name]:
            cfgfile.write(indention + line + '\n')
         del current_cfg[name]

      # Write unrecognized data
      if current_cfg:
         cfgfile.write('\n')
      for name in sorted(current_cfg): # If we don't sort these names they'll appear in a new order every time the .cfg is created
         for line in current_cfg[name]:
            cfgfile.write('// ' + line + '\n')

      cfgfile.close()

   def execute(self, queuecmd=False):
      """Executes the config"""
      if queuecmd:
         es.server.queuecmd('es_xmexec ..' + self.cfgpath.replace(self.gamedir, '', 1))
      else:
         es.server.cmd('es_xmexec ..' + self.cfgpath.replace(self.gamedir, '', 1))

   def getCvars(self):
      """Returns the cvars dictionary"""
      return self.cvars.copy()

   """ Private functions """

   def _parse(self):
      """Parses the config and returns the current settings"""
      if not os.path.isfile(self.cfgpath): return {}

      cfgfile  = open(self.cfgpath)
      cfglines = map(string.strip, cfgfile.readlines())
      cfgfile.close()

      current_cfg = {}

      for line in cfglines:
         if line.startswith('//') or not line: continue

         name = line.split(' ', 1)[0]
         if name in self.commands or name in self.cvars:
            if not line.count(' '): continue

         if name not in current_cfg:
            current_cfg[name] = []

         if line not in current_cfg[name]:
            current_cfg[name].append(line + ('\"' if line.count('\"') % 2 else ''))

      return current_cfg

"""
# Example usage:

import cfglib
import es

config = cfglib.AddonCFG(es.getAddonPath("mugmod") + "/mugmod.cfg")

config.text("******************************")
config.text("  MUGMOD SETTINGS")
config.text("******************************")

mattie_mugmod     = config.cvar("mattie_mugmod",     1, "Enable/disable Mattie's MugMod")
mugmod_announce   = config.cvar("mugmod_announce",   1, "Announces MugMod each round.")
mugmod_taunt      = config.cvar("mugmod_taunt",      1, "Taunts the mugging victim with a random message.")
mugmod_sounds     = config.cvar("mugmod_sounds",     1, "Enables kill sounds for MugMod")
mugmod_soundfile  = config.cvar("mugmod_soundfile",  "bot/owned.wav", "Sound played for a mugging if mugmod_sounds is 1")
mugmod_percentage = config.cvar("mugmod_percentage", 100, "Percentage of money stolen during a mugging.")

config.write() # Writes the .cfg to file


def load():
   config.execute() # Executes the .cfg to register changes
"""