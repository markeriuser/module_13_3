from aiogram import Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

@dp.message_handler(text= ["бро"])
async def sevi_message(message):
    print("sevi message")
    await message.answer("не брат ты мне, гнида черножопая")

@dp.message_handler(commands=['start'])
async def start_message(message):
    print('привет! Я бот помогающий твоему здоровью.')
    await message.answer("здарова здарова, секунду, ща отвечу)")

@dp.message_handler()
async def all_message(message):
    print("Введите команду /start, чтобы начать общение.")
    await message.answer("ты ебень? нажми /start")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
