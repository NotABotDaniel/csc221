"""
  >>> graph1 = Graph([(2,1),(1,0)])
  >>> print(f'--{graph1.coefs}--')
  --[(2, 1), (1, 0)]--
  >>> print(graph1.points)
  [(-11, 21), (-10, 19), (-9, 17), (-8, 15), (-7, 13), (-6, 11), (-5, 9), (-4, 7), (-3, 5), (-2, 3), (-1, 1), (0, -1), (1, -3), (2, -5), (3, -7), (4, -9), (5, -11), (6, -13), (7, -15), (8, -17), (9, -19), (10, -21)]
  >>> graph2 = Graph([(1,2),(-2,0)])
  >>> print(f'--{graph2.coefs}--')
  --[(1, 2), (-2, 0)]--
  >>> print(graph2.points)
  [(-11, -119), (-10, -98), (-9, -79), (-8, -62), (-7, -47), (-6, -34), (-5, -23), (-4, -14), (-3, -7), (-2, -2), (-1, 1), (0, 2), (1, 1), (2, -2), (3, -7), (4, -14), (5, -23), (6, -34), (7, -47), (8, -62), (9, -79), (10, -98)]
"""

class Graph:
  def __init__(self, coefs = []):
    self.width = 20
    self.height = 20
    self.coefs = coefs
    self.points = self.get_points(coefs)
    self.find_slopes()

  def __str__(self):
    return f"Graph(points={self.points}, width={self.width}, height={self.height})"
  
  def get_points(self, coefs): 
    points = []
    for i, x in enumerate(range(-self.width // 2 - 1, self.width // 2 + 1)):
      y = 0
      for c in coefs:
        y += c[0] * (x ** c[1])
      points.append(Point(self, i, x, -y))
    return points

  def find_slopes(self):
    for i, p in enumerate(self.points):
      if i > 0 and i <= self.width:
        p.m = p.get_slope()

class Point:
  def __init__(self, graph, i, x, y):
    self.x = x
    self.y = y
    self.i = i
    self.m = None
    self.graph = graph

  def __str__(self):
    return f'Point(x={self.x}, y={self.y}, i={self.i}, m={self.m}, graph={self.graph})'

  def __repr__(self):
    return f"({self.x}, {self.y})"

  def get_slope(self):
    return (self.graph.points[self.i + 1].y - self.graph.points[self.i - 1].y) / 2