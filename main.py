from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

bot = Bot(token="1807080422:AAG-Gf9brQuehFW28UbMrTDQY04KjoHbOvU")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
scheduler = AsyncIOScheduler()


async def create_poll(dp: Dispatcher):
    await dp.bot.send_poll(chat_id=-1001575536302, question='Today:', options=['6', '7'], type='regular',
                           is_anonymous=False)


def schedule_jobs():
    scheduler.add_job(create_poll, "cron", day_of_week='mon-fri', hour=14, minute=30, args=(dp,))

async def on_startup(dp):
    schedule_jobs()

if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)

