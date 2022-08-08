from aiogram import Bot, Dispatcher, executor, types
import parse
from data_store import dataSaver
from core import S_apic, apic, calc_time_for_boss

bot = Bot(token="TOKEEEENNN")
dp = Dispatcher(bot)
bos_tupe = ['Simple boss!', 'Drake apic boss', 'Apic boss']


@dp.message_handler(commands="start")
async def start(message):

    inline_btn_s_boss = types.InlineKeyboardButton(
        'Simple boss!',
        callback_data='Simple boss!')
    inline_btn_a_boss = types.InlineKeyboardButton(
        'Apic boss',
        callback_data='Apic boss')
    inline_btn_Drake_apik = types.InlineKeyboardButton(
        'Drake apic boss',
        callback_data='Drake apic boss')
    keyboard = types.InlineKeyboardMarkup().add(inline_btn_s_boss)
    keyboard.add(inline_btn_a_boss)
    keyboard.add(inline_btn_Drake_apik)
    await message.answer("Chose your boos", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data in bos_tupe)
async def type_boss(callback_query: types.CallbackQuery):
    parse.start_parse()
    unic_boss = dataSaver._unic_bos
    keyboard = types.InlineKeyboardMarkup()
    for boss in unic_boss:
        if callback_query.data == 'Drake apic boss':
            if boss in S_apic:
                inline_btn_Drake_apik = types.InlineKeyboardButton(
                    boss,
                    callback_data=boss)
                keyboard.add(inline_btn_Drake_apik)
                print('drake_apick_boss')
        elif callback_query.data == 'Apic boss':
            if boss in apic:
                inline_btn_apik = types.InlineKeyboardButton(
                    boss,
                    callback_data=boss)
                keyboard.add(inline_btn_apik)
        else:
            if boss not in S_apic and boss not in apic:
                inline_btn_simple_boss = types.InlineKeyboardButton(
                    boss,
                    callback_data=boss)
                keyboard.add(inline_btn_simple_boss)
    await callback_query.message.answer("Chose your boss",
                                        reply_markup=keyboard)
    await callback_query.answer((callback_query.data))


@dp.callback_query_handler(lambda c: c.data in dataSaver._unic_bos)
async def resp_time(callback_query: types.CallbackQuery):
    parse.start_parse()
    boss = callback_query.data
    time = dataSaver._data[boss]
    message_info = calc_time_for_boss(boss, time)
    # await callback_query.message.answer(callback_query.data)
    await callback_query.message.answer(message_info)
    await callback_query.answer((callback_query.data))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
