import asyncio
from pytgcalls import idle
from modules.clientbot import call_py, bot, user


async def start_bot():
    await bot.start()
    print("[INFO]: BOT & UBOT CLIENT STARTED !!")
    await call_py.start()
    print("[INFO]: PY-TGCALLS CLIENT STARTED !!")
    await user.join_chat("telugucoders")
    await user.join_chat("tgshadow_fighters")
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()
