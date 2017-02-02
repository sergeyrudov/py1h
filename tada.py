class Room:
    def __init__(self, long=0.0, wightd=0.0, num_windows=0):
      self.long = long
      self.wightd = wightd
      self.num_windows = num_windows

    def get_area(self):
      return self.long*self.wightd

    def windows_quantity(self):
      return self.num_windows

r = Room(5, 5, 1)
r2 = Room(6, 6, 2)

class Apartment:
     def __init__(self):
      self.rooms = []

     def add_room(self,room):
      self.rooms.append(room)

     def get_area_rooms(self):
      v = 0
      for i in self.rooms:
        v += i.get_area()
      return v




p = Apartment()
p2 = Apartment()

