from user_manager import UserManager
from user_factory import UserFactory
from notifier import UserNotifier, EmailNotifier, LogNotifier

def main():
    # Configuración inicial
    manager = UserManager()
    notifier = UserNotifier()
    
    # Registrar notificadores
    notifier.subscribe(EmailNotifier())
    notifier.subscribe(LogNotifier())
    
    # Crear usuario admin
    try:
        admin = UserFactory.create_user(
            "admin",
            "user001",
            "Ana López",
            "ana@example.com"
        )
        
        # Registrar usuario
        print(manager.add_user(admin))
        
        # Notificar registro
        notifier.notify("NUEVO_REGISTRO", admin)
        
        # Crear usuario regular
        regular = UserFactory.create_user(
            "regular",
            "user002",
            "Carlos Ruiz",
            "carlos@example.com"
        )
        
        print(manager.add_user(regular))
        notifier.notify("NUEVO_REGISTRO", regular)
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()