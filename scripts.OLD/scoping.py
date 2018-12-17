class Fake:
    def __init__(self):
        self.x = 2
        self.y = 3
        self.z = 4
        global q
        q = 55

f = Fake()
print(q)
