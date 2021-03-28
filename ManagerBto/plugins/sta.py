from telethon.tl.custom import Button
from telethon import events
from .. import klent, ADMIN, KANAL

# admine gonderilenler
@klent.on(events.NewMessage)
async def _(event):
    if event.is_private:
        # media gelibse
        if event.media:
            x = event.media
            aydi = event.sender_id
            if aydi == int(ADMIN):
                return
            # medianin caption varsa
            if event.text:
                gonderen = f'Göndərən: [{event.sender.first_name}](tg://user?id={aydi})\nID: `{aydi}`'
                filee = await event.client.send_file(ADMIN,x,caption=event.text,buttons=[
                        Button.inline('Kanala göndər',b'post')
                        ])
                await event.client.send_message(ADMIN,gonderen,reply_to=filee)

            # caption yoxsa
            else:
                gonderen = f'Göndərən: [{event.sender.first_name}](tg://user?id={aydi})\nID: `{aydi}`'
                filee = await event.client.send_file(ADMIN,x,buttons=[
                    Button.inline('Kanala göndər',b'post')])
                await event.client.send_message(ADMIN,gonderen,reply_to=filee)
        # yazi gelibse
        else:
            y = event.text
            ad = event.sender.first_name
            aydii = event.sender_id
            if aydii == int(ADMIN):
                return
            if y == "/start":
                return
            msgtoadmin = await event.client.send_message(ADMIN,y)
            await event.client.send_message(ADMIN,f'Yazan: [{ad}](tg://user?id=' + str(aydii) + ')' + '\nID: ' + '`' + str(aydii) + '`',reply_to=msgtoadmin)
    else:
        pass
@klent.on(events.CallbackQuery(data=b'post'))
async def paylas(event):
    mesaj = await event.get_message()
    if mesaj.media:
        await event.client.send_file(KANAL,file=mesaj,caption=mesaj.text)
    else:
        await event.client.send_message(KANAL,mesaj.text)
    await event.answer('Kanalda Paylaşıldı.',alert=True)
