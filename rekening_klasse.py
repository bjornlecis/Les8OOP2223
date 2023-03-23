class Rekening:

    def __init__(self,id,spaarrekening,zichtrekening):
        self.id = id
        self.spaarrekening = spaarrekening
        self.zichtrekening = zichtrekening

    def __add__(self, other):
        return f"Spaarrekening {self.spaarrekening + other.spaarrekening} \t" \
               f"Zichtrekening {self.zichtrekening+other.zichtrekening}"
    def __sub__(self, other):
        return self.spaarrekening - other.spaarrekening


r1 = Rekening("r1",10000,2000)
r2 = Rekening("r2",5000,500)
r3 = r1-r2
print(r3)
