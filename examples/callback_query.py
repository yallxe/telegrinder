from telegrinder import (
    Telegrinder,
    API,
    Token,
    Message,
    CallbackQuery,
    InlineKeyboard,
    InlineButton,
)
from telegrinder.rules import Text, CallbackDataEq, CallbackDataMarkup
import logging

api = API(token=Token.from_env())
bot = Telegrinder(api)
logging.basicConfig(level=logging.INFO)

kb = (
    InlineKeyboard()
    .add(InlineButton("Confirm", callback_data="confirm/action"))
    .row()
    .add(InlineButton("One", callback_data="number/1"))
    .add(InlineButton("Two", callback_data="number/2"))
    .row()
    .add(InlineButton("Won't respond", callback_data="number/foobar"))
).get_markup()


@bot.on.message(Text("/action"))
async def action(m: Message):
    await m.answer("Please confirm doing action.", reply_markup=kb)


@bot.on.callback_query(CallbackDataEq("confirm/action"))
async def callback_confirm_handler(cb: CallbackQuery):
    await cb.answer("Okay! Confirmed.")
    await cb.ctx_api.edit_message_text(
        cb.message.chat.id, cb.message.message_id, text="Action happens."
    )
    # *some action happens*


@bot.on.callback_query(CallbackDataMarkup("number/<n:int>"))
async def callback_number_handler(cb: CallbackQuery, n: int):
    await cb.answer("{0} + (7 * 6) - {0} = 42🤯🤯🤯".format(n))


bot.run_forever()
