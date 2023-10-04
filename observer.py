from abc import ABC, abstractmethod

# Observer Interface
class NewsSubscriber(ABC):
    @abstractmethod
    def update(self, news):
        pass

# Concrete Observers
class IOSAppSubscriber(NewsSubscriber):
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"{self.name} received news on iOS: {news}")

class AndroidAppSubscriber(NewsSubscriber):
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"{self.name} received news on Android: {news}")

class WebSubscriber(NewsSubscriber):
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"{self.name} received news on the web: {news}")

# Subject
class NewsPublisher:
    def __init__(self):
        self.subscribers = set()

    def subscribe(self, subscriber):
        self.subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self, news):
        for subscriber in self.subscribers:
            subscriber.update(news)

if __name__ == "__main__":
    # Usage
    news_publisher = NewsPublisher()

    ios_subscriber = IOSAppSubscriber("iOS App")
    android_subscriber = AndroidAppSubscriber("Android App")
    web_subscriber = WebSubscriber("Web Client")

    news_publisher.subscribe(ios_subscriber)
    news_publisher.subscribe(android_subscriber)
    news_publisher.subscribe(web_subscriber)

    news_publisher.notify_subscribers("Breaking news: Python is awesome!")
