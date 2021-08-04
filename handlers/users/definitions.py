from aiogram import types

from loader import dp

from oxfordLookup import getDifinitions
from translite import tarjimon

# Oxford diffinition
@dp.message_handler(state=None)
async def bot_definition(message: types.Message):
    if len(message.text.split())>2 :
        await message.reply(tarjimon(message.text)['result'])
    else:
        if tarjimon(message.text)["lang"]=="en":
            word_id=message.text
        else:
            word_id=tarjimon(message.text)['result']
        lookup=getDifinitions(word_id)
        if lookup :
            await message.reply(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}")
            if lookup.get('audio'):
               await message.reply_voice(lookup['audio'])
        else:
            await message.reply("Bunday so'z topilmadi")



