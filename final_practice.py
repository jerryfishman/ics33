

class Thing:
    pass

class Yo(Thing):
    pass

x = Yo()
print(type(x))
print(isinstance(x, Yo))
print(isinstance(x, Thing))
