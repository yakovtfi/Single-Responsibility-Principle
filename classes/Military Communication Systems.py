class IRadioComm:
    def send_radio(self):
        pass

class ISatelliteComm:
    def send_satellite(self):
        pass

class IMorseComm:
    def send_morse(self):
        pass


class FieldRadio(IRadioComm):
    def send_radio(self):
        print("Sending via radio")


class SatelliteComm(ISatelliteComm):
    def send_satellite(self):
        print("Sending via satellite")


class LegacyMorseUnit(IMorseComm):
    def send_morse(self):
        print("Sending via Morse code")