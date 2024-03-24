from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("𝖬𝗈𝗇𝗀𝗈𝖣𝖡 𝖡𝖺𝗀̆𝗅𝖺𝗇ı𝗅ı𝗒𝗈𝗋 ...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("𝖬𝗈𝗇𝗀𝗈𝖣𝖡 𝖡𝖺𝗀̆𝗅𝖺𝗇ı𝗅𝖽ı .")
except:
    LOGGER(__name__).error("𝖬𝗈𝗇𝗀𝗈𝖣𝖡 𝖡𝖺𝗀̆𝗅𝖺𝗇ı𝗅𝖺𝗆𝖺𝖽ı .")
    exit()
