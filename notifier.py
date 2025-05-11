class UserObserver:
    def update(self, event):
        pass

class EmailNotifier(UserObserver):
    def update(self, event):
        print(f"Email enviado: {event}")

class LogNotifier(UserObserver):
    def update(self, event):
        print(f"Log registrado: {event}")

class UserSubject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, event):
        for obs in self._observers:
            obs.update(event)