from itens import itens_dict, swords_dict
from item import Item
from player import Player
from copy import copy as Copy

# just for tests
player = Player("Germano", 5)

# Helper functions
def AddItem(_player, _itemName, _itemQuantity):
  itens_dict[_itemName].SetQuantity(_itemQuantity)
  _player.AddItem(itens_dict[_itemName])

def RemoveItem(_player, _itemName, _itemQuantity):
  itens_dict[_itemName].SetQuantity(_itemQuantity)
  _player.RemoveItem(itens_dict[_itemName])

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
    # if command needs a target
    _targets = ["status", "inventory", "forge"]
    if(_command in _targets):
      _str += " [target]"
    # show command
    print(_str)
  print("\n")

def ShowInventory(_player):
  _itens = _player.Get_AllItens()
  for _item in _itens:
    print(str(_itens[_item])+" "+str(_item))

def ForgeWeapon(_player, _type):
  if(_type == "sword"):
    _count = 1
    for _sword in swords_dict:
      print(str(_count)+". "+swords_dict[_sword].Get_Name())
      _count += 1
  
  _option = input(str("\nSelect Weapon by name \n>>>"))
  return Copy(swords_dict[_option.lower()])
  #return weapon

def ShowWeapons(_player):
  return

# Game action controllers
actions = {
  "exit": Quit,
  "status": Status,
  "inventory": ShowInventory,
  "weapons": ShowWeapons,
  "forge": ForgeWeapon,
  "help": Help,
}

targets_dict = {
  "player": player,
}

# Game message - Info
print("""The game works with inputs.

Try something as:
[command] [target]

type 'help' command if you need it :D
""")
Help()

# Game message - History
print("""You are the son of a renowned blacksmith. A few years ago, his father left behind legendary material to create an impeccable sword and finish his life's work.

He gave you a mission "If you want to learn all my techniques, you must be able to create a strong sword with anything you have around you. When I arrive back I will test my sword against your best weapon. If your weapon does not break, I will teach you my knowledge."
""")

# game loop
game = True
while(game):
  _input = input(">>> ")

  # the command is the first word 
  _command = _input.split()[0]

  if(_command in actions.keys()):

    # check command in commands list
    if(len(_input.split()) == 1):
      actions[_command]()
    
    # check subcommand in commands list
    elif(len(_input.split()) > 1):
      # the target recieve the second word
      _target = _input.split()[1]
      if(_command == "forge"):
        actions[_command](targets_dict["player"], _target)
      else:
        actions[_command](targets_dict[_target])
  else:
    print("Command not found. Try 'help'")