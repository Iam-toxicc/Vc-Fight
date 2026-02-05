from telegram import Update
from telegram.ext import ContextTypes
from keyboards.start import start_keyboard
from config import START_VIDEO

START_TEXT = (
    "HEY, I CAN BOOST YOUR VOICE VOLUME\n"
    "IN REAL TIME, EVEN IN SAANS LOGY FIR\n"
    "V BOM BOM JAYEGA.\n\n"
    "POWERING LOUDER, CLEARER CALLS\n"
    "WITH A SMART REAL-TIME VOICE BOOST ENGINE 😎"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_video(
        video=open(START_VIDEO, "rb"),
        caption=START_TEXT,
        reply_markup=start_keyboard()
    )
