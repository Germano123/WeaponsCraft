from inventory import Inventory

class Player:
  def __init__(self, name, skill):
    self.__name = name
    self.__skill = skill
    self.__exp = 0
    self.__level = 1
    self.__inventory = Inventory(10)
    self.__weapons = []
  
  # Getters and Setters
  def Get_Name(self):
    return self.__name

  def Get_Skill(self):
    return self.__skill

  # Game methods
  def GainXp(self, amount):
    self.__exp += amount
    if(self.__exp > pow(self.__level+3, 2)):
      self.__LevelUp()

  def __LevelUp(self):
    self.__level += 1

  def Get_AllItens(self):
    return self.__inventory.Get_AllItens()

  def AddItem(self, item):
    return self.__inventory.AddItem(item)
  
  def RemoveItem(self, item):
    return self.__inventory.RemoveItem(item)
