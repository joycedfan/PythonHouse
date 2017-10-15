# PythonHouse
A collection of rooms, items, and characters in python.

I'm learning Object-Oriented Programming in Python from Futurelearn.com
Please help me add more rooms and link them together.

---

Add rooms by adding the following code to main.py:

newroom = Room("Insert New Room Name")

newroom.set_description("Insert New Room Description.")


Link rooms by adding the following code to main.py:

firstroom.link_room(roomtolinkto, "direction to link")

roomtolinkto.link_room(firstroom, "opposite direction to direction to link")

Please note that links only go one way so you have to repeat the process in the opposite direction.

Example:

kitchen = Room("Kitchen")

kitchen.set_description("A dank and dirty room buzzing with flies.")

kitchen.link_room(dining_hall, "south")

dining_hall.link_room(kitchen, "north")

---

Add Enemies by adding the following code to main.py:

name = Enemy("Name", "description of character.")

name.set_conversation("What you want the character to say!")

dave.set_weakness("item that will be the enemy's weakness")

room_where_enemy_should_be.set_character(name)


Add Friends by adding the following code to main.py:

name = Friend("Name", "description of character.")

name.set_conversation("What you want the character to say!")

room_where_enemy_should_be.set_character(name)

#Note, friends don't fight friends so they don't have any weaknesses.


Example:

dave = Enemy("Dave", "a smelly, hungry zombie.")

dave.set_conversation("Brrlgrh... rgrhl... braaains...")

dave.set_weakness("brains")

dining_hall.set_character(dave)


catrina = Friend("Catrina", "a tall friendly skeleton.")

catrina.set_conversation("Why hello there, friend!")

ballroom.set_character(catrina)

---

Add Items by adding the following code:

new_item = Item("item name")

new_item.set_description ("description of item")

location_of_item.set_item(new_item)

Example:

cheese = Item("cheese")

cheese.set_description ("a cumbling block of smelly, rotting cheese")

kitchen.set_item(cheese)
                         
 ---                        


Move through the house here: https://trinket.io/python/c0bf3c7c32
