from room import Room
from item import Item
from character import Enemy, Character, Friend

#Create rooms with descriptions
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies. A strange pool of smell liquid stains the floor in front of the fridge.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on every wall and an extra long table in the middle.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floors. Huge candlesticks guard the entrance.")

hallway = Room("Hallway")
hallway.set_description ("A long hallway lined with paintings of shadowy figures.")

cellar = Room("Cellar")
cellar.set_description ("A dark smelly room littered with rotting food that emits a powerful odour.")

wine_cellar = Room("Wine Cellar")
wine_cellar.set_description ("A nearly pitch black room with empty wineracks along the walls and broken glass on the floor.")

swimming_pool = Room("Swimming Pool")
swimming_pool.set_description ("A deep pool filled with distilled water with a tiny bit of chlorine and urine.")

gym = Room("Gym")
gym.set_description ("A huge room with a glass ceiling and one yoga ball in the center of the room.")

greenhouse = Room("Greenhouse")
greenhouse.set_description ("A hot and humid room filled with scrawling vines.")

office = Room("Office")
office.set_description ("A dimly lit room where many hours were lost seeking illumination.")

grand_hall = Room("Grand Hall")
grand_hall.set_description ("A large brightly lit room with a high ceiling and ornate paintings on the wall.")

mud_room = Room("Mud Room")
mud_room.set_description ("A room filled with mud and dirty outdoor shoes.")

bedroom = Room("Bedroom")
bedroom.set_description ("A moderately sized room with a large window looking out over a garden."

#Set room locations and directions
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
hallway.link_room(ballroom, "south")
ballroom.link_room(hallway, "north")
hallway.link_room(office, "east")
office.link_room(hallway, "west")
hallway.link_room(grand_hall, "north")
grand_hall.link_room(hallway, "south")
cellar.link_room(kitchen, "up")
kitchen.link_room(cellar, "down")
cellar.link_room(wine_cellar, "east")
wine_cellar.link_room(cellar, "west")
swimming_pool.link_room(ballroom, "east")
ballroom.link_room(swimming_pool, "west")
gym.link_room(swimming_pool, "up")
swimming_pool.link_room(gym, "down")
kitchen.link_room(greenhouse, "west")
greenhouse.link_room(kitchen, "east")
hallway.link_room(mud_room, "west")
mud_room.link_room(hallway, "east")

#Create characters
dave = Enemy("Dave", "a smelly, hungry zombie that appears to be decomposing before your eyes.")
dave.set_conversation("Brrlgrh... rgrhl... braaains...")
dave.set_weakness("brains")
dining_hall.set_character(dave)

catrina = Friend("Catrina", "a tall friendly skeleton with shiny white bones.")
catrina.set_conversation("Why hello there, friend!")
ballroom.set_character(catrina)

chester = Enemy("Chester", "a small, shy mouse that can't keep still.")
chester.set_conversation("Squeak!")
chester.set_weakness("cheese")
kitchen.set_character(chester)

brodie = Friend("Brodie", "a friendly brown labrador retriever.")
brodie.set_conversation("Woof!")
greenhouse.set_character(brodie)

chuck = Enemy("Chuck", "an angry, hungry, hairy monkey.")
chuck.set_conversation("Oo oo, ah ah!")
chuck.set_weakness("banana")
hallway.set_character(chuck)

jordan = Friend("Jordan", "a well rounded, confident friend.")
jordan.set_conversation("I'm working out my brain right now.")
gym.set_character(jordan)

shoe_monster = Enemy("Shoe Monster", "an oversized, smelly, muddy shoe.")
shoe_monster.set_conversation("Squelch!")
shoe_monster.set_weakness("shoe laces")
mud_room.set_character(shoe_monster)

floating_hat = Enemy("Floatin Hat", "a mysterious hat floating 6 feet off the floor.")
floating_hat.set_conversation("Hey! Where's my head?!")
floating_hat.set_weakness("laundry detergent")
greenhouse.set_character(floating_hat)

#Create items with descriptions
key = Item("key")
key.set_description ("a small shiny key")

cheese = Item("cheese")
cheese.set_description ("a cumbling block of smelly, rotting cheese with numerous holes")

broken_glass = Item("broken glass")
broken_glass.set_description ("several broken bottles' worth of broken glass")

weight = Item("weight")
weight.set_description ("a ten pound iron weight")

flower_pot = Item("flower pot")
flower_pot.set_description ("a small yellow flower pot containing a single daisy")

shoe_laces = Item("shoe laces")
shoe_laces.set_description ("a surprisingly clean pair of long white shoe laces")

bread = Item("bread")
bread.set_description ("a freshly baked loaf of bread")

broken_chair = Item("broken chair")
broken_chair.set_description ("a useless broken chair")

floppy_disk = Item("floppy disk")
floppy_disk.set_description ("a small flat object, probably once used as a coaster")

banana = Item("banana")
banana.set_description ("a more brown than yellow, overripe banana")

laundry_detergent = Item("laundry detergent")
laundry_detergent.set_description ("a box of powdery laundry detergent that smells like sunshine")

#Set item locations
cellar.set_item(shoe_laces)
hallway.set_item(floppy_disk)
greenhouse.set_item(flower_pot)
mud_room.set_item(banana)
swimming_pool.set_item(key)
kitchen.set_item(cheese)
wine_cellar.set_item(broken_glass)
gym.set_item(weight)
kitchen.set_item(bread)
dining_hall.set_item(broken_chair)

#Initialize
current_room = kitchen
backpack = []
dead = False

while dead == False:

  print ("\n")
  current_room.get_details()
  inhabitant = current_room.get_character()

  if inhabitant is not None:

    inhabitant.describe()

  inventory = current_room.get_item()

  if inventory is not None:

    inventory.describe()

  command = input("> ")

  #Check whether a direction was typed
  if command in ["north", "south", "east", "west", "up", "down", "above", "below"]:

    current_room = current_room.move(command)

  elif command == "talk":

    if inhabitant is not None:

      inhabitant.talk()

  elif command == "fight":

    # You can check whether an object is an instance of a particular
    # class with isinstance() - useful! This code means
    # "If the character is a Friend"
    if inhabitant == None or isinstance(inhabitant, Friend):

      print("There is no one here to fight with.")

    else:

      print("What will you fight with?")
      fight_with = input()

      if fight_with in backpack:

        if inhabitant.fight(fight_with) == True:

          print("Horray, you won the fight! Or at least you distracted your opponent long enough to escape.")
          print("Now to find a way out of here...")
          current_room.character = None

        else:

          print("Ouch, you lost the fight.")
          print("Your life flashes before your eyes. It slowly gets harder to see.")
          print("Your vision blurs and the world around you fades away.")
          print("You die.")
          dead = True

      else:

          print("You realize you left your personal " + fight_with + " at home and turn to find one here.")

  elif command == "hug":

    if isinstance(inhabitant, Enemy):

      print("I wouldn't do that if I were you...")

    else:

      inhabitant.hug()

  elif command == "take":

    if inventory is not None:

      print ("You put the " + inventory.get_name() + " in your backpack.")
      backpack.append(inventory.get_name())
      current_room.set_item(None)

    else:

      print ("There is nothing here you can take.")

  elif command == "help":

    print ("Pick a direction or try talk, fight, hug or take.")

  else:

    print("I don't know how to " + command + ".")

