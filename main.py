from aiogram import Bot, Dispatcher, types, executor
import config
import random

bot = Bot(token = config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands =['start', 'go', 'davai'])
async def start(message: types.Message):
    await message.answer(f"Здраствуйте {message.from_user.full_name}")
    await message.answer('Давай-ка поиграем, в угадайку чисел тут!!')
 
@dp.message_handler(commands = ['rand'])
async def random_num(message: types.Message):
    guess_num = random.randint(1, 10)
    await message.answer('Я загадал число от 1 до 10 угадайте ')
    await message.answer("Введите число ")
    
    num = int(message.text)
    if num == guess_num:
        await message.chat('Вы угадали, поздравляем!')
        #return random_num
    else:
        await message.chat('Неверный ввод. Введите число')      
        #return random_num


@dp.message_handler()
async def not_found(message: types.Message):
    await message.reply("Я вас не понял, введите /help")
 
executor.start_polling(dp)