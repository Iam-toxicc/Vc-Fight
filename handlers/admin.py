import os
import state
from telegram import Update
from telegram.ext import ContextTypes
from config import OWNER_ID
from vc.user import user
from vc.player import join_vc, leave_vc, stop_play
from utils import resolve_target

def sudo(uid):
    return uid == OWNER_ID or uid in state.sudo_users

# ───────── SESSION ─────────

async def addsession(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not sudo(update.effective_user.id):
        return await update.message.reply_text("❌ YOU MUST BE SUDO")
    await update.message.reply_text("✅ SESSION ACTIVE")

async def delsession(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not sudo(update.effective_user.id):
        return
    await user.stop()
    try:
        os.remove("sessions/user.session")
    except:
        pass
    await update.message.reply_text("♻️ SESSION RESET")

# ───────── SUDO ─────────

async def addsudo(update, context):
    if update.effective_user.id != OWNER_ID:
        return await update.message.reply_text("❌ ONLY OWNER")

    if not context.args:
        return await update.message.reply_text("Usage: /addsudo <id | @username>")

    uid = await resolve_target(context.args[0])
    if not uid:
        return await update.message.reply_text("❌ USER NOT FOUND")

    state.sudo_users.add(uid)
    await update.message.reply_text(f"✅ SUDO ADDED: `{uid}`")

async def rmsudo(update, context):
    if update.effective_user.id != OWNER_ID:
        return await update.message.reply_text("❌ ONLY OWNER")

    if not context.args:
        return await update.message.reply_text("Usage: /rmsudo <id | @username>")

    uid = await resolve_target(context.args[0])
    if not uid:
        return await update.message.reply_text("❌ USER NOT FOUND")

    state.sudo_users.discard(uid)
    await update.message.reply_text(f"🗑 SUDO REMOVED: `{uid}`")

# ───────── VC ─────────

async def setrecordgroup(update, context):
    if not sudo(update.effective_user.id):
        return
    state.record_group = update.effective_chat.id
    await update.message.reply_text("🎙 RECORD GROUP SET")

async def join(update, context):
    if not sudo(update.effective_user.id):
        return await update.message.reply_text("❌ YOU MUST BE SUDO")

    if not context.args:
        return await update.message.reply_text("Usage: /join <group_id | @username>")

    gid = await resolve_target(context.args[0])
    if not gid:
        return await update.message.reply_text("❌ GROUP NOT FOUND")

    try:
        await join_vc(gid)
        await update.message.reply_text(f"🔊 VC JOINED `{gid}`")
    except:
        await update.message.reply_text("❌ USER ACCOUNT NOT IN GROUP / VC OFF")

async def leave(update, context):
    if not sudo(update.effective_user.id):
        return
    await leave_vc(state.playing_group)
    await update.message.reply_text("👋 LEFT VC")

# ───────── CONTROLS ─────────

async def bass(update, context):
    if not sudo(update.effective_user.id):
        return
    state.bass_enabled = not state.bass_enabled
    if state.playing_group:
        await stop_play()
        await join_vc(state.playing_group)
    await update.message.reply_text("🎵 BASS TOGGLED")

async def mute(update, context):
    if not sudo(update.effective_user.id):
        return
    await user.mute_chat(state.playing_group)
    await update.message.reply_text("🔇 MUTED")

async def unmute(update, context):
    if not sudo(update.effective_user.id):
        return
    await user.unmute_chat(state.playing_group)
    await update.message.reply_text("🔊 UNMUTED")

async def leaverecord(update, context):
    state.record_group = None
    await update.message.reply_text("❌ RECORD GROUP LEFT")

async def leaveplay(update, context):
    await stop_play()
    await update.message.reply_text("⏹ PLAY STOPPED")
