class InventoryArray:
  def __init__(self):
    self.__inventorySlots = 15
    self.__slots = []
    
  #Getters and setters
  def Get_Item(self, name):
    for _item in self.__slots:
      if (_item.Get_Name() == name):
        return self.__slots[_item]
    else:
      return False
   
  def Get_AllItems(self):
    return self.__slots
        
  #Other methods
  def AddItem(self, item):
    if(len(self.__slots) < self.__inventorySlots):
      self.__slots.append(item)
      return True
    else:
      return False
    
  def RemoveItem(self, item):
    _count = 0
    for _item in self.__slots:
      if(_item == item):
        self.__slots.pop(_count)
        return True
      _count += 1
    return False
