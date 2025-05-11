class AuthAdapter:
    def authenticate(self, credentials):
        pass

class LDAPAuth(AuthAdapter):
    def authenticate(self, credentials):
        return f"LDAP auth: {credentials['username']}"

class DBAuth(AuthAdapter):
    def authenticate(self, credentials):
        return f"DB auth: {credentials['username']}"