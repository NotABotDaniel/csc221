class GelCube:
  """
    >>> dave = GelCube()
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
  """

class victim:
  pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
