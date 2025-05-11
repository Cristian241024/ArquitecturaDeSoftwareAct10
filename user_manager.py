class UserManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.users = {}
        return cls._instance
    
    def add_user(self, user_id, user_data):
        self.users[user_id] = user_data