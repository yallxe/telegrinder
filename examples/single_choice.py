from telegrinder import Telegrinder, API, Token, Message, SingleChoice
from telegrinder.rules import Text
import logging

api = API(token=Token.from_env())
bot = Telegrinder(api)
logging.basicConfig(level=logging.DEBUG)


@bot.on.message(Text("/choice"))
async def action(m: Message):
    chosen, m_id = await (
        SingleChoice(m.chat.id, "Choose something", max_in_row=2)
        .add_option("apple", "Apple 🔴", "Apple 🟢")
        .add_option("banana", "Banana 🔴", "Banana 🟢", is_picked=True)
        .add_option("pear", "Pear 🔴", "Pear 🟢")
        .wait(m.ctx_api, bot.dispatch)
    )
    await m.ctx_api.edit_message_text(
        m.chat.id,
        m_id,
        text=f"You chose {chosen}",
    )


bot.run_forever()
