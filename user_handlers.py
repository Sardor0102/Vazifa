from loader import dp
from aiogram import types
from database import add_user, get_letters_id
from aiogram.dispatcher.storage import FSMContext
from random import choice
from states import AddLetter


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await add_user(
        user_id=message.from_user.id,
        username=message.from_user.username
    )
    await message.answer('Salom, botimizga hush kelibsiz!')


@dp.message_handler(commands=['sher'])
async def search_letters(message: types.Message):
    letters = await get_letters_id()
    random_letter = choice(letters[-1])
    await message.answer(random_letter)
