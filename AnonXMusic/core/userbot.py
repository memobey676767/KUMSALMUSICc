from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="AnonXAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="AnonXAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="AnonXAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="AnonXAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="AnonXAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"𝖠𝗌𝗂𝗌𝗍𝖺𝗇 𝖺𝗄𝗍𝗂𝖿 𝖾𝖽𝗂𝗅𝖽𝗂 ...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("gecemavisisohbett")
                await self.one.join_chat("gecemavisisohbett")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "➻ 𝖠𝗌𝗂𝗌𝗍𝖺𝗇 𝖺𝗄𝗍𝗂𝖿 𝖾𝖽𝗂𝗅𝖽𝗂 ...\n𝖸𝖺𝗋𝖽ı𝗆 ➻ @gecemavisisohbett ")
            except:
                LOGGER(__name__).error(
                    "1. 𝖠𝗌𝗂𝗌𝗍𝖺𝗇ı 𝖫𝗈𝗀 𝖦𝗋𝗎𝖻𝗎𝗇𝖺 𝖤𝗄𝗌̧𝖾𝗒𝗂𝗉 𝖸𝗈̈𝗇𝖾𝗍𝗂𝖼𝗂 𝖸𝖺𝗉ı𝗇 !"
                )
                exit()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"1. 𝖠𝗌𝗂𝗌𝗍𝖺𝗇 𝖺𝗄𝗍𝗂𝖿 𝖾𝖽𝗂𝗅𝖽𝗂 {self.one.name}")

        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("gecemavisisohbett")
                await self.two.join_chat("gecemavisisohbett")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "➻ 𝖠𝗌𝗂𝗌𝗍𝖺𝗇 𝖺𝗄𝗍𝗂𝖿 𝖾𝖽𝗂𝗅𝖽𝗂 ...\n𝖸𝖺𝗋𝖽ı𝗆 ➻ @gecemavisisohbett")
            except:
                LOGGER(__name__).error(
                    "2. 𝖠𝗌𝗂𝗌𝗍𝖺𝗇ı 𝖫𝗈𝗀 𝖦𝗋𝗎𝖻𝗎𝗇𝖺 𝖤𝗄𝗌̧𝖾𝗒𝗂𝗉 𝖸𝗈̈𝗇𝖾𝗍𝗂𝖼𝗂 𝖸𝖺𝗉ı𝗇 !"
                )
                exit()
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"2. 𝖠𝗌𝗂𝗌𝗍𝖺𝗇 𝖺𝗄𝗍𝗂𝖿 𝖾𝖽𝗂𝗅𝖽𝗂 {self.two.name}")

        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("gecemavisisohbett")
                await self.three.join_chat("gecemavisisohbett")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOGGER_ID, "➻ 𝖠𝗌𝗂𝗌𝗍𝖺𝗇 𝖺𝗄𝗍𝗂𝖿 𝖾𝖽𝗂𝗅𝖽𝗂 ...\n𝖸𝖺𝗋𝖽ı𝗆 ➻ @gecemavisisohbett")
            except:
                LOGGER(__name__).error(
                    "3. 𝖠𝗌𝗂𝗌𝗍𝖺𝗇ı 𝖫𝗈𝗀 𝖦𝗋𝗎𝖻𝗎𝗇𝖺 𝖤𝗄𝗌̧𝖾𝗒𝗂𝗉 𝖸𝗈̈𝗇𝖾𝗍𝗂𝖼𝗂 𝖸𝖺𝗉ı𝗇 !"
                )
                exit()
            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(f"3. 𝖠𝗌𝗂𝗌𝗍𝖺𝗇 𝖺𝗄𝗍𝗂𝖿 𝖾𝖽𝗂𝗅𝖽𝗂 {self.three.name}")

        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("gecemavisisohbett")
                await self.four.join_chat("gecemavisisohbett")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOGGER_ID, "➻ 𝖠𝗌𝗂𝗌𝗍𝖺𝗇 𝖺𝗄𝗍𝗂𝖿 𝖾𝖽𝗂𝗅𝖽𝗂 ...\n𝖸𝖺𝗋𝖽ı𝗆 ➻ @gecemavisisohbett")
            except:
                LOGGER(__name__).error(
                    "4. 𝖠𝗌𝗂𝗌𝗍𝖺𝗇ı 𝖫𝗈𝗀 𝖦𝗋𝗎𝖻𝗎𝗇𝖺 𝖤𝗄𝗌̧𝖾𝗒𝗂𝗉 𝖸𝗈̈𝗇𝖾𝗍𝗂𝖼𝗂 𝖸𝖺𝗉ı𝗇 !"
                )
                exit()
            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(f"4. 𝖠𝗌𝗂𝗌𝗍𝖺𝗇 𝖺𝗄𝗍𝗂𝖿 𝖾𝖽𝗂𝗅𝖽𝗂 {self.four.name}")

        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("gecemavisisohbett")
                await self.five.join_chat("gecemavisisohbett")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOGGER_ID, "➻ 𝖠𝗌𝗂𝗌𝗍𝖺𝗇 𝖺𝗄𝗍𝗂𝖿 𝖾𝖽𝗂𝗅𝖽𝗂 ...\n𝖸𝖺𝗋𝖽ı𝗆 ➻ @gecemavisisohbett")
            except:
                LOGGER(__name__).error(
                    "5. 𝖠𝗌𝗂𝗌𝗍𝖺𝗇ı 𝖫𝗈𝗀 𝖦𝗋𝗎𝖻𝗎𝗇𝖺 𝖤𝗄𝗌̧𝖾𝗒𝗂𝗉 𝖸𝗈̈𝗇𝖾𝗍𝗂𝖼𝗂 𝖸𝖺𝗉ı𝗇 !"
                )
                exit()
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"5. 𝖠𝗌𝗂𝗌𝗍𝖺𝗇 𝖺𝗄𝗍𝗂𝖿 𝖾𝖽𝗂𝗅𝖽𝗂 {self.five.name}")

    async def stop(self):
        LOGGER(__name__).info(f"➻ 𝖠𝗌𝗂𝗌𝗍𝖺𝗇𝗅𝖺𝗋 𝖣𝗎𝗋𝖽𝗎𝗋𝗎𝗅𝖽𝗎 !")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except:
            pass
