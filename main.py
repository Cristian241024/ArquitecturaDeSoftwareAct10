from user_manager import UserManager
from auth import LDAPAuth, DBAuth
from notifier import EmailNotifier, UserSubject

# Singleton
manager = UserManager()
manager.add_user("001", {"name": "Alice"})

# Adapter
ldap_auth = LDAPAuth()
print(ldap_auth.authenticate({"username": "alice"}))

# Observer
subject = UserSubject()
subject.attach(EmailNotifier())
subject.notify("Usuario registrado")