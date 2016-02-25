class Kitten():
    def __init__(self):
        pass
    def __repr__(self): return "Kitten()"
    def __str__(self): return "Kitten()"
    def __eq__(self, other): return isinstance(other, Kitten)
    
class Dog():
    def __init__(self, breed):
        self.breed = breed
    def __repr__(self):
        return 'Dog("%s")' % (self.breed)
    def __str__(self): return repr(self)
    def __eq__(self, other): return isinstance(other, Dog) and self.breed == other.breed

