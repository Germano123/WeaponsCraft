from item import Item, Sword

#Item(name)
itens_dict = {
  "Metal sheet": Item("Metal sheet"),
  "Wood planks": Item("Wood planks"),
  "Bronze coin": Item("Bronze coin"),
  "Silver coin": Item("Silver coin"),
  "Gold coin": Item("Gold coin"),
}

#Sword(name, damage, exp, cost)
#cost = {string itemName : int quantity}
swords_dict = {
  "wooden sword": Sword("Wooden Sword", 3, 5, {
    "Wood planks": 4,
  }),
  "common sword": Sword("Common Sword", 8, 8, {
    "Wood planks": 2,
    "Metal sheet": 5,
  }),
  "heavy sword": Sword("Heavy Sword", 18, 12, {
    "Wood planks": 5,
    "Metal sheet": 12,
  }),
}