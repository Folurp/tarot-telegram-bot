
import asyncio
import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton
)

# =====================================
# НАСТРОЙКИ БОТА
# =====================================

TOKEN = "9064136765:AAEn8crtydjucS4eEZxpvTacslHqH6mb40Y"

bot = Bot(token=TOKEN)
dp = Dispatcher()


# =====================================
# КОЛОДА ТАРО
# =====================================

cards = [
    {
        "name": "Шут",
        "meaning": "Новые начинания, свобода и приключения. "
                   "Не бойся сделать первый шаг."
    },
    {
        "name": "Маг",
        "meaning": "У тебя есть все возможности для достижения цели. "
                   "Действуй уверенно."
    },
    {
        "name": "Верховная Жрица",
        "meaning": "Прислушайся к интуиции. Не вся информация "
                   "пока открыта тебе."
    },
    {
        "name": "Императрица",
        "meaning": "Изобилие, любовь, творчество и развитие."
    },
    {
        "name": "Император",
        "meaning": "Порядок, стабильность и ответственность. "
                   "Пора взять ситуацию под контроль."
    },
    {
        "name": "Иерофант",
        "meaning": "Мудрость, обучение и духовное развитие."
    },
    {
        "name": "Влюбленные",
        "meaning": "Любовь, выбор и важные отношения. "
                   "Следуй зову сердца."
    },
    {
        "name": "Колесница",
        "meaning": "Победа и движение вперед. Не отступай от целей."
    },
    {
        "name": "Сила",
        "meaning": "Внутренняя сила, терпение и уверенность."
    },
    {
        "name": "Отшельник",
        "meaning": "Время побыть наедине с собой и найти ответы внутри."
    },
    {
        "name": "Колесо Фортуны",
        "meaning": "Перемены и неожиданные возможности."
    },
    {
        "name": "Справедливость",
        "meaning": "Честность, баланс и последствия поступков."
    },
    {
        "name": "Повешенный",
        "meaning": "Посмотри на ситуацию под другим углом."
    },
    {
        "name": "Смерть",
        "meaning": "Завершение старого этапа и начало нового."
    },
    {
        "name": "Умеренность",
        "meaning": "Гармония, спокойствие и поиск баланса."
    },
    {
        "name": "Дьявол",
        "meaning": "Обрати внимание на зависимости, страхи "
                   "и то, что тебя ограничивает."
    },
    {
        "name": "Башня",
        "meaning": "Неожиданные перемены. Старое освобождает "
                   "место новому."
    },
    {
        "name": "Звезда",
        "meaning": "Надежда, вдохновение и исполнение желаний."
    },
    {
        "name": "Луна",
        "meaning": "Неопределенность и скрытые эмоции. "
                   "Не спеши с выводами."
    },
    {
        "name": "Солнце",
        "meaning": "Радость, успех, счастье и позитивные события."
    },
    {
        "name": "Суд",
        "meaning": "Переосмысление прошлого и важное решение."
    },
    {
        "name": "Мир",
        "meaning": "Завершение цикла, успех и достижение цели."
    }
]


# =====================================
# КЛАВИАТУРА
# =====================================

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔮 Карта дня"),
            KeyboardButton(text="🌙 Три карты")
        ],
        [
            KeyboardButton(text="❤️ Любовь"),
            KeyboardButton(text="💰 Финансы")
        ],
        [
            KeyboardButton(text="🎲 Случайный расклад")
        ]
    ],
    resize_keyboard=True
)


# =====================================
# ФУНКЦИИ
# =====================================

def get_card():
    return random.choice(cards)


def format_card(card):
    return (
        f"🃏 Карта: {card['name']}\n\n"
        f"✨ Значение:\n{card['meaning']}"
    )


# =====================================
# КОМАНДА START
# =====================================

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🔮 Добро пожаловать в мистический мир Таро!\n\n"
        "Я помогу тебе получить случайный расклад "
        "и узнать символическое значение карт.\n\n"
        "Выбери интересующий тебя расклад 👇",
        reply_markup=keyboard
    )


# =====================================
# КАРТА ДНЯ
# =====================================

@dp.message(F.text == "🔮 Карта дня")
async def daily_card(message: Message):
    card = get_card()

    await message.answer(
        "🌞 ТВОЯ КАРТА ДНЯ\n\n"
        + format_card(card)
        + "\n\n✨ Пусть день будет прекрасным!"
    )


# =====================================
# ТРИ КАРТЫ
# =====================================

@dp.message(F.text == "🌙 Три карты")
async def three_cards(message: Message):

    selected = random.sample(cards, 3)

    positions = [
        "⏳ ПРОШЛОЕ",
        "🌿 НАСТОЯЩЕЕ",
        "🔮 БУДУЩЕЕ"
    ]

    result = "🌙 ТВОЙ РАСКЛАД НА ТРИ КАРТЫ\n\n"

    for position, card in zip(positions, selected):
        result += (
            f"{position}\n"
            f"{format_card(card)}\n\n"
        )

    await message.answer(result)


# =====================================
# ЛЮБОВЬ
# =====================================

@dp.message(F.text == "❤️ Любовь")
async def love(message: Message):

    card = get_card()

    await message.answer(
        "❤️ РАСКЛАД НА ЛЮБОВЬ\n\n"
        + format_card(card)
        + "\n\n💌 Подумай о своих чувствах "
          "и о том, чего ты действительно хочешь."
    )


# =====================================
# ФИНАНСЫ
# =====================================

@dp.message(F.text == "💰 Финансы")
async def finance(message: Message):

    card = get_card()

    await message.answer(
        "💰 РАСКЛАД НА ФИНАНСЫ\n\n"
        + format_card(card)
        + "\n\n✨ Используй толкование как повод "
          "обдумать свои финансовые решения."
    )


# =====================================
# СЛУЧАЙНЫЙ РАСКЛАД
# =====================================

@dp.message(F.text == "🎲 Случайный расклад")
async def random_reading(message: Message):

    card = get_card()

    await message.answer(
        "🎲 СУДЬБА ВЫБРАЛА ДЛЯ ТЕБЯ КАРТУ!\n\n"
        + format_card(card)
    )


# =====================================
# НЕИЗВЕСТНЫЕ СООБЩЕНИЯ
# =====================================

@dp.message()
async def unknown_message(message: Message):

    await message.answer(
        "🔮 Я пока не знаю такой команды.\n\n"
        "Пожалуйста, воспользуйся кнопками меню."
    )


# =====================================
# ЗАПУСК БОТА
# =====================================

async def main():

    print("================================")
    print("Подключаемся к Telegram...")
    print("================================")

    try:
        # Проверяем подключение и токен
        bot_info = await bot.get_me()

        print("✅ БОТ УСПЕШНО ПОДКЛЮЧЕН!")
        print(f"🤖 Имя: {bot_info.first_name}")
        print(f"🔗 Username: @{bot_info.username}")
        print("================================")
        print("🔮 БОТ ОЖИДАЕТ СООБЩЕНИЯ!")
        print("================================")

        # Запускаем получение сообщений
        await dp.start_polling(bot)

    except Exception as error:
        print("❌ ПРОИЗОШЛА ОШИБКА!")
        print(f"Причина: {error}")

    finally:
        await bot.session.close()
        print("Соединение с Telegram закрыто.")


if __name__ == "__main__":
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print("Бот остановлен пользователем.")
