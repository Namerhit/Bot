from unittest import result
from aiogram import Bot, types
import os
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor 
from config import TOKEN 
bot = Bot(token=TOKEN)
dp =Dispatcher(bot) 
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["Ага", "Нєа"]
keyboard.add(*buttons)
keyboardYesNo = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttonsYesNo = ["Жадаю", "Нє"]
keyboardYesNo.add(*buttonsYesNo)


eng = ["q", "Q", "w", "W", "e", "E", "r", "R", "t", "T", "y", "Y", "u", "U", "i", "I", "o", "O", "p", "P", "[", "{", "]", "}", "a", "A", "s", "S", "d", "D", "f", "F", "g", "G", "h", "H", "j", "J", "k", "K", "l", "L", ";", ":", "'", '"', "z", "Z", "x", "X", "c", "C", "v", "V", "b", "B", "n", "N", "m", "M", ",", "<", ".", ">", "/", "?", " ", "!", "@", "#", "$",  "%",  "^", "&",  "*", "=", "+"]
ukr = ["й", "Й", "ц", "Ц", "у", "У", "к", "К", "е", "Е", "н", "Н", "г", "Г", "ш", "Ш", "щ", "Щ", "з", "З", "х", "Х", "ї", "Ї", "ф", "Ф", "і", "І", "в", "В", "а", "А", "п", "П", "р", "Р", "о", "О", "л", "Л", "д", "Д", "ж", "Ж", "є", 'Є', "я", "Я", "ч", "Ч", "с", "С", "м", "М", "и", "И", "т", "Т", "ь", "Ь", "б", "Б", "ю", "Ю", ".", ",", " ", "!",  '"',  "№", ";",  "%", ":", "?", "*", "=", "+"]
@dp.message_handler(Text(equals="Ага"))
async def with_puree(message: types.Message):
    chat_id = message.chat.id
    await bot.send_photo(chat_id, photo=open('love.png', 'rb'), reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(Text(equals="Нє"))
async def with_puree(message: types.Message):
    await message.reply("Ладна")



	

@dp.message_handler(Text(equals="Нєа"))
async def with_puree(message: types.Message):
    chat_id = message.chat.id
    await bot.send_photo(chat_id, photo=open('fuck.png', 'rb'), reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
	await message.reply("Поки вас не попросять, кнопки не натискати")
@dp.message_handler(commands=['greeting'])
async def process_start_command(message: types.Message):
	await message.reply("https://youtu.be/dQw4w9WgXcQ")
@dp.message_handler()
async def echo_message(msg: types.Message):
	
	chat_id = msg.chat.id
	temp = list(msg.text)
	for n in range(0, len(eng)):
		if(temp[0]==eng[n]):
		    
			result = str()
			for i in range(0, len(temp)):
						for k in range(0, len(eng)):
							if(temp[i]==eng[k]):
								result = result + ukr[k]
	await msg.reply("Переклад?", reply_markup=keyboardYesNo)
	

@dp.message_handler(Text(equals="Жадаю"))
async def with_puree(msgg: types.Message):
	await msgg.reply("Відбувається переклад з древньої мови сітхів на рідну соловїну, зачекайте, будь ласка")
	await msgg.reply(result)
	chat_id = msgg.chat.id
	chat_id = msgg.chat.id
	
	chat_id = msgg.chat.id
	await bot.send_photo(chat_id, photo=open('Duck.png', 'rb'))
	await msgg.reply("Чи задовольняє вас переклад?", reply_markup=keyboard)
		
	


if __name__ == '__main__':
	executor.start_polling(dp)