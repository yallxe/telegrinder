from telegrinder import Telegrinder, API, Token, Keyboard, Button, Message
from telegrinder.rules import Text, EnumTextRule
import enum
import itertools
import asyncio

api = API(token=Token.from_env())
bot = Telegrinder(api)

YesOrNoKeyboard = (Keyboard().add(Button("Yes")).add(Button("No"))).get_markup()


class YesOrNo(enum.Enum):
    YES = "Yes"
    NO = "No"


@bot.on.message(Text("/start"))
async def start(message: Message):
    await message.answer("Do you want some tee?")
    wm, ctx = await bot.on.message.wait_for_message(
        message.chat.id, EnumTextRule(YesOrNo), default="You want, dont you?"
    )
    if ctx["enum"] == YesOrNo.NO:
        await message.answer("Leee thats sad dat tee is so sweet")
        return
    await message.answer("Yay here is you tee with a nice krendeliok")
    message_id = (await message.answer("Preparing..")).unwrap().message_id
    queue = itertools.cycle(["🫖🥨", "🥨🤗", "🤗🫖"])
    for _ in range(10):
        msg = next(queue)
        await api.edit_message_text(message.chat.id, message_id, text=msg)
        await asyncio.sleep(0.5)
    await message.answer("Tee session is over! Goodbye!")


bot.run_forever()
