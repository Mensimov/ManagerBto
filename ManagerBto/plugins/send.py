from .. import klent, ADMIN, con, cursor
from telethon import events
import asyncio

@klent.on(events.NewMessage)
async def main(event):
    if event.sender_id == ADMIN:
        if event.is_private:
            if event.text == '/link' or event.text == '/post':
                return
            if event.text.startswith('/post'):
                return
            if event.is_reply:
                rep = await event.get_reply_message()
                try:
                    a = cursor.execute(f"SELECT userid FROM users WHERE msgid = {rep.id}")
                    mesaj = a.fetchall()
                    aydi = mesaj[0][0]
                except:
                    await event.reply('Mesaj DataBase- də tapılmadı')
                try:
                    if event.media:
                        await event.client.send_file(aydi,event.media,caption=event.text)
                    else:
                        await event.client.send_message(aydi,event.text)
                except:
                    x = await event.reply('Mesaj göndərilə bilmədi')
                    await asyncio.sleep(5)
                    await x.delete() #mirta
