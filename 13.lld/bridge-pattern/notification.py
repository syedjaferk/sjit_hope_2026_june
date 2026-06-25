from abc import ABC, abstractmethod

# IMPLEMENTATION SIDE
# HOW messages are sent


class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailSender(MessageSender):
    def send(self, message):
        print(f"Sending EMAIL: {message}")


class SMSSender(MessageSender):
    def send(self, message):
        print(f"Sending SMS: {message}")


class PushSender(MessageSender):
    def send(self, message):
        print(f"Sending PUSH notification: {message}")


# ABSTRACTION SIDE
# WHAT notifications are


class Notification(ABC):
    def __init__(self, sender):
        self.sender = sender

    @abstractmethod
    def notify(self):
        pass


class OrderNotification(Notification):
    def notify(self):
        self.sender.send("Your order has been placed.")


class PaymentNotification(Notification):
    def notify(self):
        self.sender.send("Your payment was successful.")


class SecurityAlert(Notification):
    def notify(self):
        self.sender.send("Suspicious login detected!")


# Usage

email_sender = EmailSender()
sms_sender = SMSSender()

order_notification = OrderNotification(email_sender)
payment_notification = PaymentNotification(sms_sender)

order_notification.notify()
payment_notification.notify()
