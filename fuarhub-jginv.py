#!/usr/bin/env python
# -*- coding: utf-8 -*-
# kejq34/myapps/system/influent.shell.vIO-34-2.18-knosthalij.iflapp
# kejq34/home/influent.fuarhub-jginv.v1.0-26.02-18.02-AlphaCube/.gites
# App: Fuar.hub Telegram Bot for Invitation to JoinGroup
# publisher: influent
# name: fuarhub-jginv
# version: IO-1.0-26.02-18.02-AlphaCube
# script: Python3
# nocombination
#
#  Copyright 2025 JesusQuijada34 <@JesusQuijada34>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import time
import threading
from flask import Flask
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuración del bot
TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_LINK = os.environ.get('CHANNEL_LINK')
GROUP_LINK = os.environ.get('GROUP_LINK')

# Inicializar el bot
bot = telebot.TeleBot(TOKEN)

# Manejador para el comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        # Crear el mensaje de bienvenida
        welcome_text = (
            f"✨ ¡Bienvenido a la familia de Fuar.hub! ✨\n\n"
            f"Hola {message.from_user.first_name}, nos alegra tenerte aquí.\n"
            f"Somos una comunidad dedicada a compartir conocimiento y ayudarnos mutuamente.\n\n"
            f"👇 Únete a nuestros canales oficiales 👇"
        )
        
        # Crear los botones inline
        markup = InlineKeyboardMarkup(row_width=1)
        
        # Botón para el grupo
        btn_group = InlineKeyboardButton(
            text="👥 Unirse al Grupo",
            url=GROUP_LINK
        )
        
        # Botón para el canal
        btn_channel = InlineKeyboardButton(
            text="📢 Unirse al Canal",
            url=CHANNEL_LINK
        )
        
        # Agregar los botones al markup
        markup.add(btn_group, btn_channel)
        
        # Enviar el mensaje con los botones
        bot.reply_to(message, welcome_text, reply_markup=markup)
        logger.info(f"Usuario {message.from_user.id} inició el bot")
        
    except Exception as e:
        logger.error(f"Error en send_welcome: {e}")
        bot.reply_to(message, "❌ Hubo un error. Por favor intenta más tarde.")

# Manejador para cualquier otro mensaje
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        welcome_text = (
            f"👋 Hola {message.from_user.first_name}!\n\n"
            f"Para comenzar, usa el comando /start\n"
            f"O únete directamente a nuestra comunidad usando los botones de abajo:"
        )
        
        # Crear los botones inline
        markup = InlineKeyboardMarkup(row_width=1)
        btn_group = InlineKeyboardButton(text="👥 Unirse al Grupo", url=GROUP_LINK)
        btn_channel = InlineKeyboardButton(text="📢 Unirse al Canal", url=CHANNEL_LINK)
        markup.add(btn_group, btn_channel)
        
        bot.reply_to(message, welcome_text, reply_markup=markup)
        
    except Exception as e:
        logger.error(f"Error en echo_all: {e}")

# Configuración del servidor web para mantener el bot activo
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot de Fuar.hub está funcionando!"

@app.route('/health')
def health():
    return "OK", 200

def run_flask():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def run_bot():
    while True:
        try:
            logger.info("Bot iniciado correctamente")
            bot.polling(none_stop=True, interval=0, timeout=60)
        except Exception as e:
            logger.error(f"Error en bot.polling: {e}")
            time.sleep(5)

if __name__ == "__main__":
    # Iniciar el bot en un hilo separado
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # Iniciar el servidor web
    run_flask()
