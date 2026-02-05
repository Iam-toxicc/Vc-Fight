from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import SUPPORT_GROUP, SUPPORT_CHANNEL, OWNER_LINK

def start_keyboard():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("SUPPORT GROUP", url=SUPPORT_GROUP),
                InlineKeyboardButton("SUPPORT CHANNEL", url=SUPPORT_CHANNEL),
            ],
            [
                InlineKeyboardButton("OWNER", url=OWNER_LINK),
                InlineKeyboardButton("SOURCE", callback_data="source"),
            ],
            [
                InlineKeyboardButton("HELP", callback_data="help"),
            ],
            [
                InlineKeyboardButton("CLOSE", callback_data="close"),
            ],
        ]
          )
