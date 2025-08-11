from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass

class SMSNotification(Notification):
    def send(self, message):
        print(f"Send SMS: {message}")

class EmailNotification(Notification):
    def send(self, message):
        print(f"Send Email: {message}")

class NotificationFactory(ABC):

    @abstractmethod
    def create_notification(self) -> Notification:
        pass

    def notify(self, message):
        notification = self.create_notification()
        notification.send(message)

class SMSFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return SMSNotification()

class EmailFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return EmailNotification()

def client_message(factory: NotificationFactory, message:str):
    print("Client send notification, Using factory.")
    factory.notify(message)

sms_factory = SMSFactory()
client_message(sms_factory, "My first message")

email_factory = EmailFactory()
client_message(email_factory, "Message from email")