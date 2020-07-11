import math

class Rectangle:
  def __init__(self, width, height):
      self.width = width
      self.height = height

  def set_width (self, width):
    self.width = width

  def set_height (self, height):
    self.height = height

  def get_area (self):
    return self.width * self.height

  def get_perimeter (self): 
    return (2 * self.width) + (2 * self.height)

  def get_diagonal (self): 
    return math.sqrt(self.width ** 2 + self.height ** 2 )

  def get_picture (self): 
    #< 50 
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      pictureString = ''
      i = 0
      while i < self.height:
        j = 0
        while j < self.width:
          pictureString += "*"
          j += 1
        pictureString += "\n"
        i += 1
      return pictureString  

  def get_amount_inside (self, passed): 
    #times passed can fit into original (ignores times original can fit into passed...originally had it that way but wouldn't validate)
    passedWidths = self.width // passed.width 
    passedHeights = self.height // passed.height 
    passedInOriginal = passedWidths * passedHeights
    return passedInOriginal

  def __repr__(self):
    result = 'Rectangle(width={}, height={})'
    return result.format(self.width, self.height)


class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
    self.side = side

  #called anytime side, width or height changed
  def change_sides (self, side):
    self.side = side
    super().set_width(side)
    super().set_height(side)

  def set_side (self, side):
    self.change_sides(side)

  def set_width (self, side): 
    self.change_sides(side)

  def set_height (self, side):
    self.change_sides(side)
 
  def __repr__(self):
    result = 'Square(side={})'
    return result.format(self.width)