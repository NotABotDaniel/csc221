class Fighter:
    """
      >>> fighter = Fighter(20, 'home', 'sword', 100)
      >>> fighter.strength
      20
      >>> dummy = DummyTarget()
      >>> fighter.pilliage(dummy)
      >>> fighter.gold
      3
    """

    def __init__(self, strength, lore, weapon, hp, gold = 0):
        self.strength = strength
        self.lore = lore
        self.weapon = weapon 
        self.hp = hp
        self.gold = gold
    
    def hit(self, dummy):
        dummy.take_damage(self.strength)

    def pilliage(self, dummy):
        if dummy.gold >= 3:
            self.gold += 3
            dummy.gold -= 3

    def block(self, damage):
        if dummy.hit(fighter) and damage < 20:
            damage = damage * 0.5

    def take_damage(self, damage):
        # this is the blocking mechanic
        if damage < 20:
            damage = damage // 2

            self.hp -= damage
        if self.hp <= 0:
            self.hp = 0


class DummyTarget:
    """
      >>> dummy = DummyTarget()
      >>> fighter = Fighter(20, 'home', 'sword', 100)
    """
    def __init__(self, hp=100, gold = 10, strength = 10):
        self.hp = hp
        self.is_alive = True
        self.name = "Training Dummy"
        self.gold = gold
        self.strength = strength
    
    def take_damage(self, damage):
        """Take damage without any special effects."""
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
    def hit(self, fighter):
        fighter.take_damage(self.strength)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
