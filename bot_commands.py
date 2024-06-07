import asyncio

from aiogram.types import Message
from aiogram.filters import Command

from aiogram import Router, Bot, F

from reply import en_ru, ru_en, rmk

from translator import Transl

router = Router()

trans = Transl('ru', 'en')


@router.message(Command('start'))
async def start(message: Message):
    await message.reply(f'Привет! Я бот переводчик с русского на английский или наоборот. Сейчас стоит перевод с русского на английский', reply_markup=en_ru())
    trans.first = 'ru'
    trans.second = 'en'



@router.message(F.text == 'Английский -> Русский')
async def eng_rus(message: Message):
    await message.reply(f'Успешно изменено! Теперь стоит перевод с англ на рус', reply_markup=ru_en())
    trans.first = 'en'
    trans.second = 'ru'


@router.message(F.text == 'Русский -> Английский')
async def rus_eng(message: Message):
    await message.reply(f'Успешно изменено! Теперь стоит перевод с рус на англ', reply_markup=en_ru())
    trans.first = 'ru'
    trans.second = 'en'


@router.message()
async def translate(message: Message):
    await message.reply(trans.translate(message.text))




