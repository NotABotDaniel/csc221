class Fraction:
  """
    >>> f1 = Fraction()
    >>> print(f1)
    0
    >>> f2 = Fraction(5)
    >>> print(f2)
    5
    >>> f3 = Fraction(4, 5)
    >>> print(f3)
    4/5
    >>> f4 = Fraction(0, 5)
    >>> print(f4)
    0
    >>> f5 = Fraction(7, 5)
    >>> print(f5)
    7/5
    >>> f6 = Fraction(12, 16)
    >>> print(f6)
    3/4
    >>> f7 = Fraction(60, 84)
    >>> print(f7)
    5/7
  """
  # gcd = gratest common divisor
  def __init__(self, numerator = 0, denominator = 1):
    gcd = self._gcd(numerator, denominator)
    self.n = numerator // gcd
    self.d = denominator // gcd

  def _gcd(self, a, b):
    # not sure how to do this yet
    pass


  def __str__(self):
    if self.d == 1:
      return str(self.n)
    elif self.n == 0:
      return "0"
    return f"{self.n}/{self.d}"
    
if __name__ == '__main__':
  import doctest
  doctest.testmod()