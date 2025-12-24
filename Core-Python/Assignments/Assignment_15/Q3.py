class Shirt:
  
    def __init__(self, sid=0, sname="", stype="", price=0.0, size=""):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size

    def ShowBook(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.stype)
        print("Price:", self.price)
        print("Size:", self.size)

    def __del__(self):
        print("Shirt object destroyed")

s1 = Shirt(10, "Cotton Shirt", "Formal", 1200, "Large")
s1.ShowBook()

s2 = Shirt()
s2.ShowBook()
