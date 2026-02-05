from telegram import Update
from telegram.ext import ContextTypes
from keyboards.start import start_keyboard
from config import START_VIDEO
import state

START_TEXT = (
    "HEY, I CAN BOOST YOUR VOICE VOLUME\n"
    "IN REAL TIME, EVEN IN SAANS LOGY FIR\n"
    "V BOM BOM JAYEGA.\n\n"
    "POWERING LOUDER, CLEARER CALLS\n"
    "WITH A SMART REAL-TIME VOICE BOOST ENGINE 😎"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    # 🔥 DELETE OLD START MESSAGE
    if user_id in state.last_start_msg:
        try:
            await context.bot.delete_message(
                chat_id=chat_id,
                message_id=state.last_start_msg[user_id]
            )
        except:
            pass

    # ✅ SEND NEW START MESSAGE
    msg = await update.message.reply_video(
        video=open(START_VIDEO, "rb"),
        caption=START_TEXT,
        reply_markup=start_keyboard()
    )

    # 💾 SAVE MESSAGE ID
    state.last_start_msg[user_id] = msg.message_id
