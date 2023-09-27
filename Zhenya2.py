from config import TOKEN_BOT as TOKEN
import random
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import logging

# Налаштовуємо рівень логування на INFO, щоб отримувати інформацію про події.
logging.basicConfig(level=logging.INFO)
# Створюємо об'єкт бота, використовуючи токен зі змінної TOKEN.
bot = Bot(token=TOKEN)
# Створюємо диспетчер, який відповідає за обробку повідомлень бота.
dp = Dispatcher(bot)
# Встановлюємо середовище реєстрації логів, щоб відстежувати події.
dp.middleware.setup(LoggingMiddleware())


# Визначаємо обробник для команди /start.
@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    # Створюємо клавіатуру з однією кнопкою "Генерувати Рядок".
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.KeyboardButton(text="Генерувати Рядок")
    keyboard.add(button)

    # Надсилаємо привітальне повідомлення та клавіатуру користувачеві.
    await message.answer("Ласкаво просимо! Натисніть кнопку 'Генерувати Рядок', щоб отримати випадковий рядок.",
                         reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Генерувати Рядок")
async def generate_random_string(message: types.Message):
    tak = "httpswwwyoutubecomwatchvdQw4w9WgXcNifjdsfgDJJSeFGQQRoooOPPDKsfdsalmnbvz"
    save = ""
    d = 14
    for x in range(d):
        save += random.choice(tak)
    await message.answer(f"Згенерована випадкова строка:\n{save}")


# Перевіряємо, чи файл виконується безпосередньо (а не імпортується як модуль).
if __name__ == '__main__':
    # Імпортуємо метод `start_polling` з модуля `executor` для запуску бота з використанням dp (диспетчера).
    from aiogram import executor

    # Запускаємо бота в режимі відстеження нових повідомлень (полінгу), ігноруючи оновлення (skip_updates=True).
    executor.start_polling(dp, skip_updates=True)
    """"""
