class Notifier:
    def send(self, message: str):
        raise NotImplementedError



class EmailNotifier (Notifier):
    def send(self, message: str):
        print(f"email notifier {message}")

class SmsNotifier (Notifier):
    def send(self, message: str):
        print(f"sms notifier {message}")


class PushNotifier (Notifier):
    def send(self, message: str):
        print(f"push notifier {message}")