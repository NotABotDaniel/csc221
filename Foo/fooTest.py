class Foo:
    """
        >>> jeff = Foo(65, "pizza")
        >>> jeff.message()
        'I am 65 years old and I love pizza.'
    """
    def __init__(self, age, favorite_food):
        self.age = age
        self.favorite_food = favorite_food

    def message(self):
        return f"I am {self.age} years old and I love {self.favorite_food}."

if __name__ == '__main__':
    import doctest
    doctest.testmod()
