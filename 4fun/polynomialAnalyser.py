class Polynomial:
  """
    >>> p = Polynomial('x+1')
    >>> print(p)
    [(1, 1), (1, 0)]
    >>> p2 = Polynomial('2x + 3')
    >>> print(p2)
    [(2, 1), (3, 0)]
    >>> p3 = Polynomial('2x^2 + 3x + 4')
    >>> print(p3)
    [(2, 2), (3, 1), (4, 0)]
    >>> p4 = Polynomial('-x^3 + 2x - 5')
    >>> print(p4)
    [(-1, 3), (2, 1), (-5, 0)]
  """
  def __init__ (self, polyStr = '0'):
    self.coefs = []
    polyStr = polyStr.strip()
    polyStr = '+' + polyStr if polyStr[0] != '-' else polyStr
    polyStr = polyStr.replace('-', ' -').replace('+', ' +')
    chars = polyStr.split()
    for i, c in enumerate(chars):
      if c == '+':
        chars[i + 1] = '+' + chars[i + 1]
        chars.remove(c)
      elif c == '-':
        chars[i + 1] = '-' + chars[i + 1]
        chars.remove(c)   
    for term in chars:      
      t = term.split('x')
      sign = 1 if t[0][0] == '+' else -1
      if len(t[0]) == 1:
        num = sign
      else:
        num = sign * int(t[0][1:])
      degree = 0 if len(t) == 1 else (1 if t[1] == '' else int(t[1][1:]))
      self.coefs.append((num, degree))
	     
  def __str__(self):
    return str(self.coefs)
  
if __name__ == '__main__':
  import doctest
  doctest.testmod()