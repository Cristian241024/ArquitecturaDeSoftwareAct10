class UserManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.users = {}
        return cls._instance
    
    def add_user(self, user):
        """Registra un usuario en el sistema"""
        if user.user_id in self.users:
            raise ValueError(f"Usuario {user.user_id} ya existe")
        self.users[user.user_id] = user
        return f"Usuario {user.user_id} registrado exitosamente"
    
    def get_user(self, user_id):
        """Obtiene un usuario por ID"""
        return self.users.get(user_id)