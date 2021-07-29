class Score():
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
  
  def get_player_name(self):
    return self.values[0]
  
  def get_total(self):
    return self.values[4]
  
  def get_score(self):
    return self.values[5]

  def __str__(self) -> str:
    return f'Score for {self.values[0]}: {self.values[5]}, total: {self.values[4]}\n'
  
  def __repr__(self) -> str:
      return self.__str__()
    
  def __lt__(self, other):
    return True if self.values[4] < other.values[4] else False
  
  def __le__(self, other):
    return True if self.values[4] <= other.values[4] else False
  
  def __ne__(self, other):
    return True if self.values[4] != other.values[4] else False
  
  def __gt__(self, other):
    return True if self.values[4] > other.values[4] else False
  
  def __ge__(self, other):
    return True if self.values[4] >= other.values[4] else False
  
  def __eq__(self, other):
    return True if self.values[4] == other.values[4] else False
  

