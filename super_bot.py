from flask import Flask
from threading import Thread
from javascript import require, On
import random

# --- НАЛАШТУВАННЯ САЙТУ ---
app = Flask('')

@app.route('/')
def home():
    return "<h1>✅ Python_Hero онлайн!</h1><p>Бот працює, поки працює цей сайт.</p>"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- ЛОГІКА БОТА MINECRAFT ---
mineflayer = require('mineflayer')

bot = mineflayer.createBot({
    'host': 'sprat.aternos.host',
    'port': 24575,
    'username': 'Python_Hero2'
})

# Списки для генератора
classes = ["Воїн", "Маг", "Лучник", "Крафтер Minecraft"]
powers = ["Вогонь", "Блискавка", "Невидимість", "Супер-швидкість"]

@On(bot, 'chat')
def handle_chat(this, username, message, *args):
    if username == bot.username: return
    
    msg = message.lower()
    
    if msg == 'хто ти?':
        h_class = random.choice(classes)
        h_power = random.choice(powers)
        bot.chat(f"Я {h_class} із магією {h_power}! Я охороняю цей сервер 24/7.")

# Запуск сайту та бота
keep_alive()
print("🚀 Сайт запущено. Бот підключається до Minecraft...")
