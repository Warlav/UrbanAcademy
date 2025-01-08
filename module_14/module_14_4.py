from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *

api = 'token'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button_1 = KeyboardButton(text='Информация')
button_2 = KeyboardButton(text='Купить')
kb.add(button, button_1)
kb.add(button_2)

in_kb = InlineKeyboardMarkup(resize_keybord=True)
in_button_1 = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
in_button_2 = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
in_kb.add(in_button_1)
in_kb.add(in_button_2)

product_kb = InlineKeyboardMarkup(resize_keyboard=True)
product_button_1 = InlineKeyboardButton('Цифра 1', callback_data='product_buying')
product_button_2 = InlineKeyboardButton('Цифра 2', callback_data='product_buying')
product_button_3 = InlineKeyboardButton('Цифра 3', callback_data='product_buying')
product_button_4 = InlineKeyboardButton('Цифра 4', callback_data='product_buying')
product_kb.add(product_button_1, product_button_2)
product_kb.add(product_button_3, product_button_4)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=in_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула Миффлина-Сан Жеора:\n'
                              'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n'
                              'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_weight(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    m_calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    w_calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161
    await message.answer(f'Дневная норма калорий: {m_calories}, если вы - мужчина, и {w_calories}, если вы - женщина.')
    await state.finish()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    for i in products:
        await message.answer(f'Название: {i[1]} | Описание: {i[2]} | Цена: {i[3]}')
        try:
            with open(f'{i[0]}.png', 'rb') as img:
                await message.answer_photo(img)
        except FileNotFoundError:
            pass
        except IndexError:
            pass
    await message.answer(text='Выберите продукт для покупки:', reply_markup=product_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
