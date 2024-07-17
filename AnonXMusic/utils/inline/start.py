from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url="https://t.me/DelularSohbet"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_2"], url="https://t.me/Sohbet_Kazani"),
            InlineKeyboardButton(text=_["S_B_6"], url="https://t.me/DelularSohbet"),
        ],
        [
            InlineKeyboardButton(text="✚ BOT SAHİP  ", url="https://t.me/Meyitzade"),
        ],
    ]
    return buttons
