import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler
from config import BOT_TOKEN
from vc.player import start_clients
from handlers import admin

async def main():
    await start_clients()

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("addsession", admin.addsession))
    app.add_handler(CommandHandler("delsession", admin.delsession))
    app.add_handler(CommandHandler("addsudo", admin.addsudo))
    app.add_handler(CommandHandler("rmsudo", admin.rmsudo))
    app.add_handler(CommandHandler("setrecordgroup", admin.setrecordgroup))
    app.add_handler(CommandHandler("join", admin.join))
    app.add_handler(CommandHandler("leave", admin.leave))
    app.add_handler(CommandHandler("bass", admin.bass))
    app.add_handler(CommandHandler("mute", admin.mute))
    app.add_handler(CommandHandler("unmute", admin.unmute))
    app.add_handler(CommandHandler("leaverecord", admin.leaverecord))
    app.add_handler(CommandHandler("leaveplay", admin.leaveplay))

    print("🔥 VC BOOST BOT STARTED")
    await app.run_polling()

asyncio.run(main())
