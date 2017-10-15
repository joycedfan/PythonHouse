class Item():
  
  def __init__(self, item_name):
    self.name = item_name
    self.description = None
    self.item_location = {}
    
  def set_description(self, item_description):
    self.description = item_description
  
  def set_name(self, item_name):
    self.name = item_name
    
  def get_name(self):
    return self.name
    
  def get_description(self):
    return self.description
  
  def describe(self):
    print ("You see " + self.description + " here.")
  
  def print_items(self, current_room, all_items):
    if current_room == self.item_location[self]:
      print ("You see a " + self.name)
