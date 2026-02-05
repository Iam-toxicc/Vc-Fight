from pyrogram import Client
from config import API_ID, API_HASH

user = Client(
    "sessions/user",
    api_id=API_ID,
    api_hash=API_HASH
)
