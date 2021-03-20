from random import randint as Random

class Item:
  def __init__(self, name):
    self.__name = name
    self.__quantity = 0

  def Get_Name(self):
    return self.__name

  def Get_Quantity(self):
    return self.__quantity
  
  def SetQuantity(self, amount):
    self.__quantity = amount
  
  def AddQuantity(self, amount):
    self.__quantity += amount

  def RemoveQuantity(self, amount):
    self.__quantity -= amount

class Sword(Item):
  def __init__(self, name, damage, expGained, cost):
    super().__init__(name)
    self.__damage = damage
    self.__expGained = expGained
    self.__cost = cost
    self.__level = 0

  def Get_Damage(self):
    return self.__damage

  def Get_Level(self):
    return self.__level

  def Get_Exp(self):
    return self.__expGained

  def Set_Level(self, level):
    self.__level = level

  def UpgradeDamage(self, maxDamage):
    self.__damage += Random(0, maxDamage)