class User:
  def __init__(self, username, password, birds_found = [], points = 0):
    self.username = username
    self.password = password
    self.birds_found = birds_found
    self.points = points
  def __str__(self):
    return str(self.__dict__)