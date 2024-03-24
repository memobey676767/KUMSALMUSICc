from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("otoson") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆 :</b>\n\n/otoson [ 𝗄𝖺𝗉𝖺𝗅ı | 𝖺𝖼ı𝗄 ]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "acik":
        await autoend_on()
        await message.reply_text(
            "➻ 𝖡𝖺𝗌̧𝖺𝗋ı𝗒𝗅𝖺 𝖺𝖼̧ı𝗅𝖽ı ."
        )
    elif state == "kapali":
        await autoend_off()
        await message.reply_text("➻ 𝖡𝖺𝗌̧𝖺𝗋ı𝗒𝗅𝖺 𝗄𝖺𝗉𝖺𝗍ı𝗅𝖽ı .")
    else:
        await message.reply_text(usage)
