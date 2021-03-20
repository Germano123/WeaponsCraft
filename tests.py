from player  import Player
from item import *

# main
player = Player("Germano", 5)

# Actions functions
def Quit():
  print("Quit")
  global game
  game = False

def Status(target):
  print("Show status")

def Help():
  print("\n")
  _count = 0
  for _command in actions:
    _count += 1
    _str = "%d. %s" %(_count, _command)
    _targets = ["status"]
    if(_command in _targets):
      _str += " [target]"
    print(_str)
  print("\n")

# Game action controllers
actions = {
  "exit": Quit,
  "status": Status,
  "help": Help,
}

targets_dict = {
  "player": player,
}

print("""The game works with inputs.
Try something as:
[command] [target]
type 'help' command if you need it :D
""")

game = True
while(game):
  _input = input(">>> ")

  # not checking if command need

  if(_input in actions.keys()):
    _command = _input.split()[0]
    # check command in commands list
    if(len(_input.split()) == 1):
      actions[_command]()
    
    # check subcommand in commands list
    elif(len(_input.split()) > 1):
      _target = _input.split()[1]
      actions[_command](targets_dict[_target])
  else:
    print("Command not found. Try 'help'")