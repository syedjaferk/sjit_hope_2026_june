from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")


class PushNotification(Notification):
    def send(self, message):
        print(f"Sending PUSH: {message}")


class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        raise ValueError("Invalid Notification Type")


# Client Code
notifier = NotificationFactory.create_notification("sms")
notifier.send("ORder placed ")
