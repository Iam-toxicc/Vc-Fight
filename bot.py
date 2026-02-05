import asyncio
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
)
from config import BOT_TOKEN, SOURCE_VIDEO
from vc.player import start_clients
from handlers import admin
from handlers.start import start


# ───────── CALLBACK BUTTON HANDLER ─────────
async def callbacks(update, context):
    query = update.callback_query
    await query.answer()

    if query.data == "help":
        await query.message.reply_text(
            "/addsession\n"
            "/delsession\n"
            "/addsudo <id | @user>\n"
            "/rmsudo <id | @user>\n"
            "/setrecordgroup\n"
            "/join <group_id | @username>\n"
            "/leave\n"
            "/bass\n"
            "/mute\n"
            "/unmute\n"
            "/leaverecord\n"
            "/leaveplay"
        )

    elif query.data == "source":
        await query.message.reply_video(
            video=open(SOURCE_VIDEO, "rb"),
            caption="SOURCE PREVIEW"
        )

    elif query.data == "close":
        try:
            await query.message.delete()
        except:
            pass


# ───────── MAIN ─────────
async def main():
    # start user account + pytgcalls
    await start_clients()

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # START
    app.add_handler(CommandHandler("start", start))

    # SESSION
    app.add_handler(CommandHandler("addsession", admin.addsession))
    app.add_handler(CommandHandler("delsession", admin.delsession))

    # SUDO
    app.add_handler(CommandHandler("addsudo", admin.addsudo))
    app.add_handler(CommandHandler("rmsudo", admin.rmsudo))

    # VC
    app.add_handler(CommandHandler("setrecordgroup", admin.setrecordgroup))
    app.add_handler(CommandHandler("join", admin.join))
    app.add_handler(CommandHandler("leave", admin.leave))

    # CONTROLS
    app.add_handler(CommandHandler("bass", admin.bass))
    app.add_handler(CommandHandler("mute", admin.mute))
    app.add_handler(CommandHandler("unmute", admin.unmute))
    app.add_handler(CommandHandler("leaverecord", admin.leaverecord))
    app.add_handler(CommandHandler("leaveplay", admin.leaveplay))

    # INLINE BUTTONS
    app.add_handler(CallbackQueryHandler(callbacks))

    print("🔥 VC BOOSTER BOT RUNNING")
    await app.run_polling()


if __name__ == "__main__":
    asyncio.run(main())
