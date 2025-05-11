class UserNotifier:
    """Sistema de notificaciones"""
    def __init__(self):
        self.subscribers = []
    
    def subscribe(self, subscriber):
        """Añade un nuevo suscriptor"""
        self.subscribers.append(subscriber)
    
    def notify(self, event_type, user):
        """Notifica a todos los suscriptores"""
        message = f"{event_type} - Usuario: {user.name} ({user.role})"
        for subscriber in self.subscribers:
            subscriber.update(message, user.email)

class EmailNotifier:
    """Notificador por correo electrónico"""
    def update(self, message, email):
        print(f"📧 Enviando a {email}: {message}")

class LogNotifier:
    """Notificador para registro en logs"""
    def update(self, message, _):
        print(f"📝 Registrando en log: {message}")