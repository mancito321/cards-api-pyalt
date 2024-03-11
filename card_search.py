import requests
import json

def search_by_name_exact(name):
  print('callling')
  x = requests.get("https://api.scryfall.com/cards/named?exact={}".format(name))
  json_object = json.loads(x.text)
  return create_card_dictionary(json_object)

def create_card_dictionary(fullDict): 
  return {
    "name": fullDict.get("name"),
    "mana_cost": fullDict.get("mana_cost"),
    "cmc": fullDict.get("cmc"),
    "colors": fullDict.get("colors"),
    "color_identity": fullDict.get("color_identity"),
    "type": fullDict.get("type_line"),
    "rarity": fullDict.get("rarity" ),
    "set": fullDict.get("set")
  }