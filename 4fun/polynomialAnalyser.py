class Polynomial:
  """
    >>> p = Polynomail('x+1')
    >>> print(p)
    [1, 1]
    >>> p2 = Polynomail('2x + 3')
    >>> print(p)
    [2, 3]
    >>> p3 = Polynomial('2x^2 + 3x + 4')
    >>> print(p2)
    [2, 3, 4]
    >>> p4 = Polynomial('-x^3 + 2x - 5')
    >>> print(p4)
    [-1, 0, 2, -5]
  """
  def __init__(self, polyStr = '0'):
    pass
  
  def __str__(self):
    return ''
  
if __name__ == '__main__':
  import doctest
  doctest.testmod()