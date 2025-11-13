class Polynomial:
  """
    >>> p1 = Polynomial()
    >>> print(p1)
    '0'
    >>> p2 = Polynomial([3, 1, 5])
    >>> print(p2)
    '3x^2 + x + 5'
    >>> p3 = Polynomial([2, 3, 1, 5])
    >>> print(p3)
    '2x^3 + 3x^2 + x + 5'
    >>> p4 = Polynomial([2, 0, 3, 7, 2])
    >>> print(p4)
    '2x^4 + 3x^2 + 7x + 2'
  """
  def __init__ (self, coefs = [0]):
    while len(coefs) > 1 and coefs[0] == 0:
      coefs.pop(0)
    
    self.coefs = coefs
    
  def __str__ (self):
    if self.coefs == [0]:
      return "'0'"
    
    parts = []
    degree = len(self.coefs) - 1

    for coef in self.coefs:
      if coef == 0:
        degree -= 1
        continue 

      sign = '-' if coef < 0 else '+'
      absCoef = abs(coef)

      if degree == 0:
        termBody = f"{absCoef}"
      elif degree == 1:
        termBody = "x" if absCoef == 1 else f"{absCoef}x"
      else:
        termBody = f"x^{degree}" if absCoef == 1 else f"{absCoef}x^{degree}"
      
      if not parts:
        if sign == '-':
          parts.append(f"-{termBody}")
        else:
          parts.append(f"{termBody}")
      else:
        parts.append(f" {sign} {termBody}")

      degree -= 1

    return "'"+"".join(parts)+"'"

if __name__ == '__main__':
    import doctest
    doctest.testmod()

