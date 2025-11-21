"""
  >>> dave = GelCube(2, 10)
  >>> print(dave.hp)
  inf
  >>> dave.take_damage(20000000)
  >>> print(dave.hp)
  inf
  >>> bob = victim()
  >>> jerry = victim()
  >>> print(bob.hp)
  1200
  >>> print(jerry.hp)
  1200
  >>> dave.absorb(bob)
  >>> print(len(dave.victims))
  1
  >>> dave.burn()
  >>> print(bob.hp)
  1100
  >>> dave.absorb(jerry)
  >>> print(len(dave.victims))
  2
  >>> dave.burn()
  >>> print(bob.hp)
  1000
  >>> print(jerry.hp)
  1100
  >>> garry = victim()
  >>> dave.absorb(garry)
  cannot absorb more victims
  >>> print(len(dave.victims))
  2

"""
import math

class GelCube:
  def __init__ (self, size = 10, hp = 1):
    self.hp = math.inf * hp
    self.size = size
    self.victims = []

  def __str__(self):
    victim_str = '['+(', '.join(vic for vic in self.victims) if self.victims else '')+']'
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
