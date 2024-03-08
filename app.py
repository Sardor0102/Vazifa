from loader import dp
from aiogram import executor
from database import create_tables


async def on_startup(dispatcher):
    await create_tables()
    import user_handlers


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)