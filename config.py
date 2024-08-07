import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "22160237"))
API_HASH = getenv("API_HASH", "095b9df69b08c2dcffbdd2f8542e3280")
BOT_TOKEN = getenv("BOT_TOKEN", "7066329662:AAFpadkd6qX7uQyCzayxRnfE7MyH9vNifkw")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://kurt67143:nays@cluster0.vjg7bma.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))
LOGGER_ID = int(getenv("LOGGER_ID", "-1002163362347"))
OWNER_ID = int(getenv("OWNER_ID", "5587097134"))
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "",
)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kumsaldestekkanal")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/gecemavisisohbett")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
STRING1 = getenv("STRING_SESSION", "BAHGTCYAECeeUJ4zpSdj2-k2-UtKxqoKIuPStIEXPHMte0SIj_KqNjPd0xg1opgHEkQq0XyM8T2bMDUR5j-tIiwYzIjUbkFDE1kRJ5V-qJjjruQ5k301V5eZHaUdn8ZQtC5wRpwLn8K5KS2k9TirtmNpHTS7bBrrTAkVVPu4AsI2mqctvdhxmIGl-gU-USBf4qF6s8prqcm5XsyskGa1iUSZ9kSy1duvprKFj0VbxKbUOfLyXPuedafhfx3r0_XfTxS_CtwDczdY9f40SFjW90zAJeN7EnQhH_ijDCP6BL-diwNv5RwBR_1Dn_B2stmp2mErbhO3EW5KWV5XW9w32kgpmKkQAAAAGxQGFHAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)



HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)
# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/e5a809fe337adff6f4d4a.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/0160271dbe745b3b02366.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
STATS_IMG_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
STREAM_IMG_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
