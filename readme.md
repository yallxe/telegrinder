# telegrinder

Framework for effective and reliable telegram bot building.

Still in development.

* Type hinted
* Customizable and extensible
* Ready to use scenarios and rules
* Fast models built on msgspec
* Both low-level and high-level API

# Getting started

Install using PyPI:

```
pip install telegrinder
```

Basic example:

```python
from telegrinder import Telegrinder, API, Token, Message
from telegrinder.rules import Text
import logging

api = API(token=Token("123:token"))
bot = Telegrinder(api)
logging.basicConfig(level=logging.INFO)

@bot.on.message(Text("/start"))
async def start(message: Message):
    me = (await api.get_me()).unwrap()
    await message.answer(f"Hello, {me.first_name}")

bot.run_forever()
```

# Community

Join our [telegram chat](https://t.me/telegrinder_en).

# [Contributing](https://github.com/timoniq/telegrinder/blob/main/contributing.md)

# License

Telegrinder is [MIT licensed](./LICENSE)  
Copyright © 2022 [timoniq](https://github.com/timoniq)