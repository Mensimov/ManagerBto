from .. import klent
from telethon import events
from .. import ADMIN
@klent.on(events.NewMessage(pattern=".send"))
async def send(event):
    if event.sender_id == ADMIN:
        try:
            rep = await event.get_reply_message()
            if rep:
                if rep.media:
                    message = event.text
                    split = message.split(" ", 2)
                    try:
                        user = int(split[1])
                        try:
                            if str(split[2]):
                                cap = str(split[2])
                        except:
                            cap = ''
                    except:
                        user = str(split[1])
                        try:
                            if str(split[2]):
                                cap = str(split[2])
                        except:
                            cap = ''
                    await event.client.send_file(user,rep.file.id,caption=cap)
                    await event.reply('Mesaj göndərildi')
            else:
                message = event.text
                split = message.split(" ", 2)
                try:
                    user = int(split[1])
                    text = str(split[2])
                except:
                    user = str(split[1])
                    text = str(split[2])
                await event.client.send_message(user,text)
                await event.reply('Mesaj göndərildi')
        except Exception as e:
            await event.reply(f'Bir xəta yarandı:\n`{e}`')