import random
from data.config import admins as admin_id
from aiogram import types
from utils.db_api.models import *
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message
from states.state import *
from loader import dp
from utils.db_api.db_commands import get_dare, get_truth
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsGroup(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type in (types.ChatType.GROUP, types.ChatType.SUPERGROUP)


@dp.message_handler(Command("start"))
async def starting(message: types.Message):
    await message.answer("Xush kelibsiz!")

@dp.message_handler(Command("haqiqat"))
async def starting(message: types.Message):
    a =await get_truth()
    random_index = random.randint(0,len(a)-1)
    i = a[random_index]
    print(a[random_index])
    await message.answer(i.text)

@dp.message_handler(Command("jasorat"))
async def starting(message: types.Message):
    a =await get_dare()
    random_index = random.randint(0,len(a)-1)
    i = a[random_index]
    print(a[random_index])
    await message.answer(i.text)


@dp.message_handler(IsGroup(),Command("haqiqat"))
async def starting(message: types.Message):
    a =await get_truth()
    print(a, "*"*100)

    random_index = random.randint(0,len(a)-1)
    i = a[random_index]
    print(a[random_index])
    await message.reply(i.text)

@dp.message_handler(IsGroup(),Command("jasorat"))
async def starting(message: types.Message):
    a =await get_dare()
    print(a)
    random_index = random.randint(0,len(a)-1)
    i = a[random_index]
    print(a[random_index])
    await message.reply(i.text)

@dp.message_handler(user_id = admin_id, commands=["add_truth"])
async def add_truth(message: Message):
    await message.answer("Rostgo'ylik savolini kiriting:")
    await TruthAdd.text.set()


@dp.message_handler(state=TruthAdd.text)
async def creating_truth(message:Message, state: FSMContext):
    await TruthOrDare.create(text = message.text, category = "truth")
    await message.answer("ok")
    await state.finish()

@dp.message_handler(user_id = admin_id, commands=["add_dare"])
async def add_truth(message: Message):
    await message.answer("Harakat shartini kiriting:")
    await DareAdd.text.set()


@dp.message_handler(state=DareAdd.text)
async def creating_truth(message:Message, state: FSMContext):
    await TruthOrDare.create(text = message.text, category = "dare")
    await message.answer("ok")
    await state.finish()

@dp.message_handler(user_id = admin_id, commands=["all_truth"])
async def add_truth(message: Message):
    txt = "Barcha truth shartlar:\n"
    a = await get_truth()
    for k, i in enumerate(a):
        txt += f"{k+1}). {i.text}\n"

    await message.answer(txt)

@dp.message_handler(user_id = admin_id, commands=["all_dare"])
async def add_truth(message: Message):
    txt = "Barcha dare shartlar:\n"
    a = await get_dare()
    for i in a:
        txt += f"{i.id}). {i.text}\n"

    await message.answer(txt)