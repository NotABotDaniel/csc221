"""
  >>> dave = GelCube(2)
  >>> print(dave.hp)
  999999999999999999999999999999
  >>> dave.take_damage(199)
  >>> print(dave.hp)
  999999999999999999999999999800
  >>> bob = victim()
  >>> jerry = victim()
  >>> print(bob.hp)
  1200
  >>> print(jerry.hp)
  1200
  >>> dave.absorb(bob)
  >>> print(dave.victims)
  [dave]
  >>> dave.burn()
  >>> print(bob.hp)
  1100
  >>> dave.absorb(jerry)
  >>> print(dave.victims)
  [dave, jerry]
  >>> dave.burn()
  >>> print(bob.hp)
  1000
  >>> print(jerry.hp)
  1100
  >>> garry = victim()
  >>> dave.absorb(garry)
  'cannot absorb more victims'
  >>> print(dave.victims)
  [dave, jerry]

"""


class GelCube:
  def __init__ (self, size = 1):
    self.hp = 999999999999999999999999999999
    self.size = size
    self.victims = []
  
  def take_damage(self, damage):
    self.hp -= damage
  
  def absorb(self, victim):
    if len (self.victims) < 2:
      self.victims.append(victim)
    else:
      print('cannot absorb more victims')


class victim:
  def __init__ (self):
    self.hp = 1200
  
  def take_damage(self, damage):
    self.hp -= damage


if __name__ == '__main__':
    import doctest
    doctest.testmod()
