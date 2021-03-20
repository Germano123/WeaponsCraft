class Inventory:
  def __init__(self, quantity):
    self.__slots = {}
    self.__slotQuantity = quantity

  def Get_AllItens(self):
    return self.__slots
  
  def Get_Item(self, itemName):
    return self.__slots[itemName]

  def Get_ItemQuantity(self, itemName):
    return self.__slots[itemName].quantity
  
  def AddItem(self, item):
    try:
      if(item.Get_Name() in self.__slots.keys()):
        self.__slots[item.Get_Name()] += item.Get_Quantity()
      else:
        self.__slots[item.Get_Name()] = item.Get_Quantity()
      return True
    except:
      return False
  
  def RemoveItem(self, item):
    try:
      if(item.Get_Name() in self.__slots.keys()):
        self.__slots[item.Get_Name()] -= item.Get_Quantity()
      else:
        self.__slots[item.Get_Name()] = item.Get_Quantity()
      return True
    except:
      return False