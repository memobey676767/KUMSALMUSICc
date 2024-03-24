from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class Anony(Client):
    def __init__(self):
        LOGGER(__name__).info(f"𝖡𝗈𝗍 𝖺𝗄𝗍𝗂𝖿 𝖾𝖽𝗂𝗅𝖽𝗂 ...\n𝖸𝖺𝗋𝖽ı𝗆 ➻ @BotsDestek")
        super().__init__(
            name="AnonXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>{self.mention} 𝖠𝗄𝗍𝗂𝖿 :</b><u>\n\n𝖨𝖽 : <code>{self.id}</code>\n𝖠𝖽ı : {self.name}\n𝖫𝗂𝗇𝗄𝗂 : @{self.username}\n\n𝖸𝖺𝗋𝖽ı𝗆 ➻ @BotsDestek",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "𝖫𝗎̈𝗍𝖿𝖾𝗇 𝖡𝗈𝗍𝗎 & 𝖠𝗌𝗂𝗌𝗍𝖺𝗇ı 𝖫𝗈𝗀 𝖦𝗋𝗎𝖻𝗎𝗇𝗎𝗓𝖺 𝖤𝗄𝗅𝖾𝗒𝗂𝗇.."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"𝖡𝗈𝗍 𝖫𝗈𝗀 𝖦𝗋𝗎𝖻𝗎𝗇𝖺 𝖤𝗋𝗂𝗌̧𝖾𝗆𝖾𝖽𝗂 .\n𝖭𝖾𝖽𝖾𝗇 : {type(ex).__name__}."
            )
            exit()

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "𝖫𝗎̈𝗍𝖿𝖾𝗇 𝖡𝗈𝗍𝗎 & 𝖠𝗌𝗂𝗌𝗍𝖺𝗇ı 𝖫𝗈𝗀 𝖦𝗋𝗎𝖻𝗎𝗇𝗎𝗓𝖽𝖺 𝖸𝗈̈𝗇𝖾𝗍𝗂𝖼𝗂 𝖸𝖺𝗉ı𝗇."
            )
            exit()
        LOGGER(__name__).info(f"𝖡𝗈𝗍 𝖺𝗄𝗍𝗂𝖿 𝖾𝖽𝗂𝗅𝖽𝗂 {self.name}")

    async def stop(self):
        await super().stop()
