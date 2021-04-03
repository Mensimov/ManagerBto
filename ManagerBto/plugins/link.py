from .. import klent, ADMIN, con, cursor
from telethon import events

@klent.on(events.NewMessage(pattern='/link'))
async def link(event):
    if event.sender_id == ADMIN:
        rep = await event.get_reply_message()
    if not rep:
        await event.reply('Bir mesaja yanıt ver')
        return
    try:
        a = cursor.execute(f"SELECT ad, userid FROM users WHERE msgid = {rep.id}")
        mesaj = a.fetchall()
        await event.reply(f'İstifadəçi: [{mesaj[0][0]}](tg://user?id={mesaj[0][1]})\nID: {mesaj[0][1]}')
    except:
        await event.reply('Mesaj DataBase də tapılmadı')
