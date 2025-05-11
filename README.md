# Sistema de Gestión de Usuarios con Patrones de Diseño
## 📌 Caso de Uso
Sistema centralizado para gestión de usuarios que implementa:
- **Registro y almacenamiento** de usuarios (Singleton)
- **Creación flexible** de tipos de usuario (Factory Method)
- **Notificaciones** automáticas por email y logs (Observer)

## 🛠️ Patrones Implementados

### 1. Singleton (Creacional)
**Propósito**: Garantizar una única instancia global del gestor de usuarios  
**Problema resuelto**: Evitar inconsistencia en datos por múltiples instancias  
**Archivo**: `user_manager.py`  
**Uso**:
```python
manager = UserManager()
manager.add_user(user_obj)
```

### 2. Adapter (AuthAdapter)

**Propósito:** Centralizar la creación de objetos usuario
**Problema resuelto:** Flexibilidad para añadir nuevos tipos de usuario
**Archivo:**  user_factory.py
**Implementaciones:**
  -AdminUser
  -RegularUser

### 3. Observer - UserNotifier

**Propósito:** Notificar eventos a múltiples sistemas
**Archivo:** notifier.py
**Componentes:**

  UserNotifier (Observable)

  EmailNotifier (Envía emails)

  LogNotifier (Registra en sistema de logs)

### 🚀 Cómo Ejecutar
**Clonar repositorio:**
  https://github.com/Cristian241024/ArquitecturaDeSoftwareAct10.git

**Ejecutar:**
  python main.py