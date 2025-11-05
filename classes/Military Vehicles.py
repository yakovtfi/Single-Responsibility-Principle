class IDrive:
    def drive(self):
        pass

class IFly:
    def fly(self):
        pass

class ISail:
    def sail(self):
        pass


class Tank(IDrive):
    def drive(self):
        print("Tank driving")


class FighterJet(IFly, IDrive):
    def fly(self):
        print("Jet flying")
    def drive(self):
        print("Jet taxiing on runway")


class Submarine(ISail):
    def sail(self): print("Submarine sailing underwater")