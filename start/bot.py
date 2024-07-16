from .config import bot
from handlers.register import register_dispatcher



async def start():
    dp = await register_dispatcher()
    await dp.start_polling(bot)
