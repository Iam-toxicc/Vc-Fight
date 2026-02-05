from vc.user import user

async def resolve_target(text: str):
    try:
        if text.lstrip("-").isdigit():
            return int(text)
        chat = await user.get_chat(text)
        return chat.id
    except:
        return None
