import importlib
import asyncio
import os
from pyrogram import idle
from AniPlay import app
from AniPlay.plugins import ALL_MODULES

async def init():
    for module in ALL_MODULES:
        importlib.import_module("AniPlay.plugins." + module)
    print("[INFO]: Imported Modules Successfully")

    await app.start()
    print("[INFO]: Bot Started")
    await idle()
    print("[INFO]: BOT STOPPED")
    await app.stop()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
    loop.run_forever()
