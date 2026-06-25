class EmailNotification:
    def send(self, message):
        print(f"Sending Email: {message}")


class SMSNotification:
    def send(self, message):
        print(f"Sending SMS: {message}")


class PushNotification:
    def send(self, message):
        print(f"Sending PUSH: {message}")


# Mocking
notification_type = "email"

if notification_type == "email":
    notifier = EmailNotification()
elif notification_type == "sms":
    notifier = SMSNotification()
elif notification_type == "push":
    notifier = PushNotification()


notifier.send("Order placed")
