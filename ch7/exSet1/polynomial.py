class Polynomial:
    """
      >>> p1 = Polynomial()
      >>> print(p1)
      '0'
    """
    """
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
        self.coefs = coefs[0]
    
    def __str__ (self):
        return "'"+str(self.coefs)+"'"

if __name__ == '__main__':
    import doctest
    doctest.testmod()

