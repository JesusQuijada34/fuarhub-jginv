# 🤖 Fuar.hub Telegram Bot
<p align="center">
  <img src="https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=telegram" alt="Telegram Bot">
  <img src="https://img.shields.io/badge/Python-3.7+-green?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Hosted-Replit-orange?style=for-the-badge&logo=replit" alt="Hosted on Replit">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License MIT">
</p>
Plantilla de Bot de Telegram oficial para Joining Links. Da la bienvenida a los nuevos miembros y proporciona acceso directo a canales y grupos.

## ✨ Características

- 🚀 Mensaje de bienvenida personalizado al usar /start
- 👥 Botones inline para unirse al grupo y canal
- 📱 Respuesta automática a cualquier mensaje
- 🔗 Links directos a la comunidad

## 📋 Requisitos

- Python 3.7+
- Token de Bot de Telegram
- Cuenta en Replit (para hosting)

## 🛠️ Configuración

### 1. Obtener Token de Bot
1. Habla con [@BotFather](https://t.me/botfather) en Telegram
2. Envía `/newbot` y sigue las instrucciones
3. Guarda el token que te proporciona

### 2. Variables de Entorno
En Replit, ve a "Secrets" (icono de candado) y agrega:

| Variable | Valor | Descripción |
|----------|-------|-------------|
| `BOT_TOKEN` | `TOKEN DEL BOT` | Token de tu bot de Telegram |
| `CHANNEL_LINK` | `LINK DEL CANAL` | Link del canal |
| `GROUP_LINK` | `LINK DEL GRUPO` | Link del grupo |

### 3. Instalación en Replit

```bash
# Los pasos son automáticos en Replit, pero si clonas localmente:
pip install -r requirements.txt
python fuarhub-jginv.py
```

## 📁 Estructura del Proyecto

```
fuarhub-bot/
│
├── fuarhub-jginv.py     # Código principal del bot
├── requirements.txt      # Dependencias del proyecto
└── README.md            # Este archivo
```

## 🎮 Comandos del Bot

| Comando | Descripción |
|---------|-------------|
| `/start` | Muestra mensaje de bienvenida con botones de acceso |

## 🔧 Dependencias Principales

- `pyTelegramBotAPI` - Interacción con API de Telegram
- `flask` - Servidor web para mantener el bot activo

## 🚀 Despliegue en Replit

1. Fork este repositorio en Replit
2. Configura las variables de entorno (Secrets)
3. Haz clic en "Run"
4. ¡Tu bot está vivo! 🎉

## 📱 Uso del Bot

1. Busca tu bot en Telegram por su username
2. Envía `/start`
3. Haz clic en los botones para probar tus links
4. ¡Listo! 🎊

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea tu rama (`git checkout -b feature/mejora`)
3. Commit cambios (`git commit -am 'Agrega mejora'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abre un Pull Request

## ⭐ Agradecimientos

A todos los miembros de la comunidad GitHub, Telegram y DEV Community por hacer este impulso posible

## PROPOSE

Es un bot dedicado a un canal y un grupo privaod en telegram, por seguridad, hemos convertido esto en una plantilla para el uso