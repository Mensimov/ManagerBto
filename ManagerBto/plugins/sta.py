from telethon.tl.custom import Button
from telethon import events
from .. import klent, ADMIN, KANAL, add_to_db

# admine gonderilenler
@klent.on(events.NewMessage)
async def _(event):
    if event.sender_id != ADMIN:
        if event.is_private:
            if event.media:
                msgtoadmin = await event.client.send_file(ADMIN,event.media,caption=event.text,buttons=[Button.inline('Kanalda paylaş', b'post')])
            else:
                msgtoadmin = await event.client.send_message(ADMIN,event.text)
            add_to_db(msgtoadmin.id,event.sender_id,event.sender.first_name)
@klent.on(events.CallbackQuery(data=b'post'))
async def paylas(event):
    mesaj = await event.get_message()
    if mesaj.media:
        await event.client.send_file(KANAL,file=mesaj,caption=mesaj.text)
    else:
        await event.client.send_message(KANAL,mesaj.text)
    await event.answer('Kanalda Paylaşıldı.',alert=True)
