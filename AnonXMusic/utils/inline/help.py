from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AnonXMusic import app
import config

from typing import Union

def help_pannel(_, START: Union[bool, int] = None):
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        )
    ]
    mark = second if START else None
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_3"],
                    url=f"https://t.me/{app.username}?startgroup=true"
                )
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_1"],
                    callback_data="help_callback hb1"
                ),
                InlineKeyboardButton(
                    text=_["H_B_2"],
                    callback_data="help_callback hb2"
                )
            ],
            [
                InlineKeyboardButton(
                text=_["H_B_3"],
                        callback_data="help_callback hb3"
                )
            ],
            [
                InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
                InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT)
            ],
            *((mark,) if mark else ())
        ]
        )


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
