from aiogram import Dispatcher ,Bot
import asyncio
from database import Database
from aiogram import filters, types, F

bot = Bot(token="7940028955:AAEHsLfUH2SltrDYDtFRPDYObbysrI9XORU")
dp = Dispatcher(bot=bot)
db = Database()

@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    await message.answer("Salom :)")

@dp.message(F.text=="Qalesan")
async def qalesan_question(message: types.Message):
    await message.answer("Bundan zo'r bo'lmaydi :)")

@dp.message(F.text=="menga hazil ayt")
async def hazil_question(message: types.Message):
    await message.answer("Ikkita do‘st gaplashyapti: — Bilasanmi, men piyoda sayr qilishni yaxshi ko‘raman! — Ha, shunaqami? Qayerlarga sayr qilasan? — To‘xtab qolgan mashinam ustaxonaga qadar...🤣🤣🤣")

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())