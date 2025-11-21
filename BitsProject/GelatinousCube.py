"""
  >>> dave = GelCube(2, 10)
  >>> print(dave.hp)
  9999999999999999999999999999990
  >>> dave.take_damage(190)
  >>> print(dave.hp)
  9999999999999999999999999999800
  >>> bob = victim()
  >>> jerry = victim()
  >>> print(bob.hp)
  1200
  >>> print(jerry.hp)
  1200
  >>> dave.absorb(bob)
  >>> print(dave.victims)
  [bob]
  >>> dave.burn()
  >>> print(bob.hp)
  1100
  >>> dave.absorb(jerry)
  >>> print(dave.victims)
  [bob, jerry]
  >>> dave.burn()
  >>> print(bob.hp)
  1000
  >>> print(jerry.hp)
  1100
  >>> garry = victim()
  >>> dave.absorb(garry)
  cannot absorb more victims
  >>> print(dave.victims)
  [bob, jerry]

"""


class GelCube:
  def __init__ (self, size = 1, hp = 1):
    self.hp = hp * 999999999999999999999999999999
    self.size = size
    self.victims = []

  def __str__(self):
    victim_str = '['+(', '.join(str(vic) for vic in self.victims) if self.victims else '')+']'
    return f"GelCube(size={self.size}, hp={self.hp}, victims={victim_str})"
  
  def take_damage(self, damage):
    self.hp -= damage
  
  def absorb(self, victim):
    if len (self.victims) < 2:
      self.victims.append(victim)
    else:
      print('cannot absorb more victims')
  
  def burn(self):
    for v in self.victims:
      v.take_damage(100)

class victim:
  def __init__ (self):
    self.hp = 1200
  
  def __str__(self):
    return f"victim(hp={self.hp})"
  
  def take_damage(self, damage):
    self.hp -= damage


if __name__ == '__main__':
    import doctest
    doctest.testmod()
