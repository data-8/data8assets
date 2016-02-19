import hashlib

def cat_box_hash(obj):
    if isinstance(obj, Box) or isinstance(obj, Cat):
        return hash(obj)
    else:
        return int(hashlib.md5(repr(obj).encode('utf-8')).hexdigest(), 16)

class Box():
    def __init__(self, *args):
        self.contents = list(args)
    def __repr__(self):
        return "Box(%s)" % (", ".join([repr(c) for c in self.contents]))
    def __str__(self): return repr(self)
    def __eq__(self, other): return isinstance(other, Box) and self.contents == other.contents
    def __hash__(self): return 17 + sum(17**(i+2) * cat_box_hash(self.contents[i]) for i in range(len(self.contents)))

class Cat():
    def __init__(self):
        pass
    def __repr__(self): return "Cat()"
    def __str__(self): return "Cat()"
    def __eq__(self, other): return isinstance(other, Cat)
    def __hash__(self): return 149

