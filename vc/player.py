from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
from vc.user import user
import state

pytg = PyTgCalls(user)

async def start_clients():
    await user.start()
    await pytg.start()

async def join_vc(chat_id: int):
    audio = "audio/bass.mp3" if state.bass_enabled else "audio/normal.mp3"
    await pytg.join_group_call(chat_id, AudioPiped(audio))
    state.playing_group = chat_id

async def leave_vc(chat_id: int):
    await pytg.leave_group_call(chat_id)
    state.playing_group = None

async def stop_play():
    if state.playing_group:
        await pytg.leave_group_call(state.playing_group)
        state.playing_group = None
