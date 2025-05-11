# Sistema de Gestión de Usuarios con Patrones de Diseño
## 📌 Caso de Uso
Sistema centralizado para gestión de usuarios que implementa:
1. **Registro y almacenamiento** de usuarios (Singleton)
2. **Autenticación flexible** con múltiples proveedores (Adapter)
3. **Notificaciones automáticas** ante eventos (Observer)

## 🛠️ Patrones Implementados

### 1. Singleton (Creacional)
- **Propósito**: Garantizar una única instancia global del gestor de usuarios.
- **Problema resuelto**: Evitar inconsistencia en datos por múltiples instancias.
- **Archivo**: `user_manager.py`
- **Uso**:
  ```python
  manager = UserManager()
  manager.add_user("001", {"name": "Alice"})
### 2. Adapter (AuthAdapter)

Propósito: Unificar interfaces de autenticación diferentes
Archivo: auth.py
Implementaciones:

LDAPAuth

DBAuth
### 3. Observer - UserNotifier

Propósito: Notificar eventos a múltiples sistemas
Archivo: notifier.py
Componentes:

UserSubject (Observable)

EmailNotifier (Observer)

LogNotifier (Observer)

### 🚀 Cómo Ejecutar
Clonar repositorio:
https://github.com/Cristian241024/ArquitecturaDeSoftwareAct10.git
Ejecutar:
python main.py