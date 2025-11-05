class Unit:
    pass


class FlyingUnit(Unit):
    def fly(self):
        print("Flying...")


class GroundUnit(Unit):
    def drive(self):
        print("Driving on ground...")


class Drone(FlyingUnit):
    pass


class Tank(GroundUnit):
    pass