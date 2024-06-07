from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove


def en_ru():
    builder = ReplyKeyboardBuilder()

    builder.button(text='Английский -> Русский')

    builder.adjust(1)

    return builder.as_markup(resize=True, input_filed_placeholder='Сделать перевод с английского на русский')


def ru_en():
    builder = ReplyKeyboardBuilder()

    builder.button(text='Русский -> Английский')

    builder.adjust(1)

    return builder.as_markup(resize=True, input_filed_placeholder='Сделать перевод с русского на английский')


rmk = ReplyKeyboardRemove()