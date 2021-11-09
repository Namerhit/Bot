from aiogram import Bot, types
import os

from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor 
from config import TOKEN 
bot = Bot(token=TOKEN)
dp =Dispatcher(bot) 




eng = ["q", "Q", "w", "W", "e", "E", "r", "R", "t", "T", "y", "Y", "u", "U", "i", "I", "o", "O", "p", "P", "[", "{", "]", "}", "a", "A", "s", "S", "d", "D", "f", "F", "g", "G", "h", "H", "j", "J", "k", "K", "l", "L", ";", ":", "'", '"', "z", "Z", "x", "X", "c", "C", "v", "V", "b", "B", "n", "N", "m", "M", ",", "<", ".", ">", "/", "?", " ", "1", "!", "2", "@", "3", "#", "4", "$", "5", "%", "6", "^", "7", "&", "8", "*", "9", "(", "0", ")", "-", "_", "=", "+"]
ukr = ["й", "Й", "ц", "Ц", "у", "У", "к", "К", "е", "Е", "н", "Н", "г", "Г", "ш", "Ш", "щ", "Щ", "з", "З", "х", "Х", "ї", "Ї", "ф", "Ф", "і", "І", "в", "В", "а", "А", "п", "П", "р", "Р", "о", "О", "л", "Л", "д", "Д", "ж", "Ж", "є", 'Є', "я", "Я", "ч", "Ч", "с", "С", "м", "М", "и", "И", "т", "Т", "ь", "Ь", "б", "Б", "ю", "Ю", ".", ",", " ", "1", "!", "2", '"', "3", "№", "4", ";", "5", "%", "6", ":", "7", "?", "8", "*", "9", "(", "0", ")", "-", "_", "=", "+"]
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
	await message.reply("Переводчик для сектантов")
@dp.message_handler()
async def echo_message(msg: types.Message):
	temp = list(msg.text)
	for n in range(0, len(eng)):
		if(temp[0]==eng[n]):
			result = str()
			for i in range(0, len(temp)):
			     	   	for k in range(0, len(eng)):
			     	   		if(temp[i]==eng[k]):
			     	   			result = result + ukr[k]
	await msg.reply(result)
	chat_id = msg.chat.id
	

	await bot.send_photo(chat_id, photo=open('Duck.png', 'rb'))


if __name__ == '__main__':
	executor.start_polling(dp)