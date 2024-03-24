import asyncio
import os
import shutil
import socket
from datetime import datetime

import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from pyrogram import filters

import config
from AnonXMusic import app
from AnonXMusic.misc import HAPP, SUDOERS, XCB
from AnonXMusic.utils.database import (
    get_active_chats,
    remove_active_chat,
    remove_active_video_chat,
)
from AnonXMusic.utils.decorators.language import language
from AnonXMusic.utils.pastebin import AnonyBin


@app.on_message(filters.command(["reboot"]) & SUDOERS)
async def restart_(_, message):
    response = await message.reply_text("➻ 𝖸𝖾𝗇𝗂𝖽𝖾𝗇 𝖻𝖺𝗌̧𝗅𝖺𝗍ı𝗅ı𝗒𝗈𝗋 ...")
    ac_chats = await get_active_chats()
    for x in ac_chats:
        try:
            await app.send_message(
                chat_id=int(x),
                text=f"{app.mention} 𝖸𝖾𝗇𝗂𝖽𝖾𝗇 𝖻𝖺𝗌̧𝗅𝖺𝗍ı𝗅ı𝗒𝗈𝗋 .\n 20 𝗌𝖺𝗇𝗂𝗒𝖾 𝗌𝗈𝗇𝗋𝖺 𝖺𝗄𝗍𝗂𝖿 𝗈𝗅𝖺𝖼𝖺𝗄𝗍ı𝗋 :-)",
            )
            await remove_active_chat(x)
            await remove_active_video_chat(x)
        except:
            pass

    try:
        shutil.rmtree("downloads")
        shutil.rmtree("raw_files")
        shutil.rmtree("cache")
    except:
        pass
    await response.edit_text(
        "➻ 𝖸𝖾𝗇𝗂𝖽𝖾𝗇 𝖻𝖺𝗌̧𝗅𝖺𝗍ı𝗅ı𝗒𝗈𝗋...\n𝖡𝗂𝗋 𝗌𝗎̈𝗋𝖾 𝖻𝖾𝗄𝗅𝖾𝗒𝗂𝗇 :-)"
    )
    os.system(f"kill -9 {os.getpid()} && bash start")
