from telethon.tl.custom import Button
from telethon import events
from .. import klent, ADMIN_USERNAME, KANAL_USERNAME
@klent.on(events.NewMessage(pattern="/start"))
async def alive(event):
    mention = f"[{event.sender.first_name}](tg://user?id={event.sender_id})"
    start_msg = f"""
Salam, {mention}\n\nBu bota göndərdiyiniz mediya, mesaj Adminə göndərilir və Adminim təsdiqləsə göndərdiyiniz mediya, mesaj Kanalda paylaşılacaq.
"""
    await event.reply(start_msg,buttons=[
        [Button.url("Sahib 👑","t.me/" + ADMIN_USERNAME)],
        [Button.url("Kanal 📣","https://t.me/" + KANAL_USERNAME)],
        [Button.url("COD 🗄️","https://github.com/Mensimov/ManagerBto")]
    ])