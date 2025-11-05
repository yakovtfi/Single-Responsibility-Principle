from abc import ABC, abstractmethod

class IShooter(ABC):
    @abstractmethod
    def shoot(self):
        pass

class INavigator(ABC):
    @abstractmethod
    def navigate(self):
        pass

class IAirSupportCaller(ABC):
    @abstractmethod
    def call_air_support(self):
        pass


class Infantry(IShooter, INavigator):
    def shoot(self):
        print("Infantry shooting")
    def navigate(self):
        print("Infantry navigating")


class ForwardObserver(IShooter, IAirSupportCaller):
    def shoot(self):
        print("Observer shooting")
    def call_air_support(self):
        print("Calling air support")


class Pilot(IAirSupportCaller):
    def call_air_support(self):
        print("Pilot calling air support")