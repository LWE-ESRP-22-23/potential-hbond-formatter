import math
from atom import *
from residue import *

class Contact:
    def __init__(self, donorR:Residue, acceptorR:Residue, donorA:Atom, acceptorA:Atom, hydrogen:Atom, donorFirstResidueNumber:int, acceptorFirstResidueNumber:int):
        self.donorA = donorA
        self.acceptorA = acceptorA
        self.donorR = donorR
        self.acceptorR = acceptorR
        self.hydrogen = hydrogen
        self.distance = self.calculateDistance(donorA, acceptorA)
        self.angle = self.calculateAngle(donorA, acceptorA, hydrogen)

    def calculateDistance(self, a1:Atom, a2:Atom):
        # 3d distance formula
        return math.sqrt((a1.X - a2.X) ** 2 + (a1.Y - a2.Y) ** 2 + (a1.Z - a2.Z) ** 2)

    def calculateAngle(self, donor:Atom, acceptor:Atom, hydrogen:Atom):
        # Law of Cosines
        # c^2 = a^2 + b^2 - 2*a*b*cos(C)
        # C = acos((c^2 - a^2 - b^2) / (-2 * a * b))
        a = self.calculateDistance(donor, hydrogen)
        b = self.calculateDistance(acceptor, hydrogen)
        c = self.distance # Don't recalculate a distance we already know.

        return math.acos((c**2 - a**2 - b**2) / (-2 * a * b))

if __name__ == "__main__":
    a = Atom()
    b = Atom()
    c = Atom()
    con = Contact(a,b,c,4,5)