class CourseInfo():
  def __init__(self, args):
    self.values = []
    self.itemCount = 0
    for arg in args:
      self.values.append(arg)
      self.itemCount += 1
      
  def __iter__(self):
    self.i = 0
    #print(f'iter called: {self.i}')
    return self
  
  def __next__(self):
    if self.i <= self.itemCount:
      val = self.values[self.i]
      self.i += 1
      #print(f'next called: {self.i}, {val}')
      return val
    else:
      raise StopIteration
  
  def get_course_name(self):
    return self.values[1]
  
  def get_layout_name(self):
    return self.values[2]
  
  def get_date(self):
    return self.values[3]
  
  def get_par(self):
    return self.values[4]

  def __str__(self) -> str:
    return f'Course {self.values[1]}({self.values[2]}) par: {self.values[4]}\n'
  
  def __repr__(self) -> str:
      return self.__str__()