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
  def __init__(self, coefs = [0]):
    self.coefs = coefs if any(coefs) else [0]

  def __str__(self):
    if self.coefs == [0]:
      return "'0'"

    parts = []
    degree = len(self.coefs) - 1

    for coef in self.coefs:
      if coef == 0:
        degree -= 1
        continue

      absCoef = abs(coef)

      termBody = (
        f"{absCoef}" if degree == 0 else
        ("x" if absCoef == 1 else f"{absCoef}x") if degree == 1 else
        (f"x^{degree}" if absCoef == 1 else f"{absCoef}x^{degree}")
      )

      sign = "-" if coef < 0 else "+" if parts else ""
      parts.append(f"{sign} {termBody}".strip())
      degree -= 1

    return "'" + " ".join(parts) + "'"

if __name__ == '__main__':
  import doctest
  doctest.testmod()

