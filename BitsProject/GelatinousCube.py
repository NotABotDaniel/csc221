"""
  >>> dave = GelCube(10, 2)
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
  900.0
  >>> dave.absorb(jerry)
  >>> print(len(dave.victims))
  2
  >>> dave.burn()
  >>> print(bob.hp)
  600.0
  >>> print(jerry.hp)
  900.0
  >>> garry = victim()
  >>> dave.absorb(garry)
  cannot absorb more victims
  >>> print(len(dave.victims))
  2

"""
import math

class GelCube:
  def __init__ (self, hp = 1, size = 10):
    self.hitpts = 1000000 * hp
    self.alive = True
    self.size = size
    self.victims = []
    self.godmode = False
    self.enemies = []

  def __str__(self):
    victim_str = '['+(', '.join(v for v in self.victims) if self.victims else '')+']'
    return f"GelCube(size={self.size}, hp={self.hp}, victims={victim_str})"
  
  def take_damage(self, damage):
    if not self.godmode:
      if self.alive:
        if damage >= self.hitpts * 1000:
          print('you hit the cube so hard that it vaporized all its victims')
          self.vaporize()
          self.hitpts = 0
        elif math.random() > 0.8:
          self.hitpts -= damage
          print(f'you dealt {damage} damage to the cube')
        else:
          print('the cube absorbed the damage')
      else:
        self.alive = True
        self.hitpts = damage
        print(f'the cube was dead but it was hit it again and it revived \n the cube healed {damage} hp')
      
      if self.hitpts <= 0:
        self.alive = False
        print('the cube is basically dead now')
    else:
      print('the cube is on a higher plane and cannot be dealt damage \n your attacks, though inefective, have insulted the cube \n it will now unleash its wrath uppon you all')
      
      for e in self.enemies:
        try:
          self.victims.append(e)
        except:
          pass
      self.vaporize()

  def absorb(self, v):
    if len(self.victims) < self.size:
      self.victims.append(v)
      v.dripinonanibinwana = v.hp
    else:
      print('cannot absorb more victims')
  
  def burn(self):
    for v in self.victims:
      v.take_damage(v.dripinonanibinwana / 4)
  
  def vaporize(self):
    for v in self.victims:
      v.take_damage(math.inf)
      v.take_damage(math.inf)
      v.take_damage(math.inf)

  def reform(self):
    if not self.alive:
      self.alive = True
      self.hitpts = 1000000
      print('the cube has reformed itself and is alive again')

  def DE(self, enemies):
    self.enemies = enemies

  def acend(self):
    print('the cube has acended to a higher plane of existence \n its victims are freed')
    self.godmode = True
    self.victims = []
  
  def punish(self, enemy):
    if self.godmode:
      enemy.take_damage(math.inf)
      enemy.take_damage(math.inf)
      enemy.take_damage(math.inf)
    else:
      print('the cube is a mortal being and cannot punish its enemies so easily')
    

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
