from aiogram import Router, flags
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command('start'))
async def handle_start(message: Message):
    await message.answer('it is bot template just test')


@router.message(Command('bye'))
@flags.del_from
async def handle_bye(message: Message):
    await message.answer('bye')
