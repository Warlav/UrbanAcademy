import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import CommandStart
from aiogram.filters.callback_data import CallbackQuery
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = 'token'
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())

button = KeyboardButton(text='Рассчитать')
button_1 = KeyboardButton(text='Информация')
kb = ReplyKeyboardMarkup(keyboard=[[button, button_1]], resize_keybord=True)

in_button_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
in_button_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb = InlineKeyboardMarkup(inline_keyboard=[[in_button_1], [in_button_2]], resize_keybord=True)

start_router = Router()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@start_router.message(F.text == 'Рассчитать')
async def main_menu(message: Message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb)


@start_router.callback_query(F.data == 'formulas')
async def get_formulas(message: Message):
    await message.answer('Формула Миффлина-Сан Жеора:\n'
                         'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n'
                         'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')


@start_router.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@start_router.callback_query(F.data == 'calories')
async def set_age(message: Message, state: FSMContext):
    await message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)


@start_router.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await state.set_state(UserState.growth)


@start_router.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)


@start_router.message(UserState.weight)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    m_calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    w_calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161
    await message.answer(f'Дневная норма калорий: {m_calories}, если вы - мужчина, и {w_calories}, если вы - женщина.')
    await state.clear()


@start_router.message()
async def all_massages(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


async def main():
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
