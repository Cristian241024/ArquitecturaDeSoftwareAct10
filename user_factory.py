class User:
    """Clase base para usuarios"""
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class AdminUser(User):
    """Usuario con privilegios administrativos"""
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.role = "admin"
        self.permissions = ["manage_users", "edit_content"]

class RegularUser(User):
    """Usuario estándar"""
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.role = "regular"
        self.permissions = ["view_content"]

class UserFactory:
    """Factory para crear usuarios"""
    @staticmethod
    def create_user(user_type, user_id, name, email):
        if user_type == "admin":
            return AdminUser(user_id, name, email)
        elif user_type == "regular":
            return RegularUser(user_id, name, email)
        raise ValueError(f"Tipo de usuario inválido: {user_type}")