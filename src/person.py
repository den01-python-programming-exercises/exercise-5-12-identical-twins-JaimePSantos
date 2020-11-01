# from simple_date import SimpleDate
class Person:

    def __init__(self,name,birthday,height,weight):
        self.name = name
        self.birthday = birthday
        self.weight = weight
        self.height = height

    # implement an __eq__ method here
    def __eq__(self,other):
      if not isinstance(other,Person):
        return False
      
      if(self.name==other.name and self.birthday==other.birthday and self.weight==other.weight and self.height == other.height):
        return True
      
      return False

if __name__ == 'main':
  from simple_date import SimpleDate
else:
  from src.simple_date import SimpleDate
