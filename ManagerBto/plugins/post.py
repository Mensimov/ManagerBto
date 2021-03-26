from .. import klent, ADMIN, KANAL
from telethon import events

@klent.on(events.NewMessage(pattern=".post"))
async def post(event):
    try:
        if event.sender_id == ADMIN:
            msg = await event.get_reply_message()
            #await event.reply(msg.file.id)
            if msg.media:
                x = msg.file.id
                if msg.text:
                    await event.client.send_file(KANAL,x,caption=msg.text)
                else:
                	try:
	                	y = event.text
	                	split = y.split(" ", 1)
	                	cap = str(split[1])
	                except:
	                	cap = ''
                	await event.client.send_file(KANAL,x,caption=cap)
            else:
                await event.client.send_message(KANAL,msg)
            await event.reply("Kanalda paylaşıldı")
        else:
            return
    except Exception as e:
        print(e)