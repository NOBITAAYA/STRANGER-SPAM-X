from telethon import events, Button
from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10
from AltronX.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("⚡️𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦⚡️", data="help_back")
        ],
        [
        Button.url("⚡️𝗖𝗛𝗔𝗡𝗡𝗘𝗟⚡️", "https://t.me/MRATYU"),
        Button.url("⚡️𝗦𝗨𝗣𝗣𝗢𝗥𝗧⚡️", "https://t.me/MRATYU")
        ],
        [
        Button.url("⚡️𝗣𝗔𝗣𝗔⚡️", "https://t.me/MRATYU")
        ]
        ]


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**𝗛𝗘𝗬 [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n𝗜 𝗔𝗠  [{BotName}](tg://user?id={BotId})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **✦ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗗 𝗕𝗬 :~ [KAIRV](https://t.me/MRATYU)**\n\n"
        TEXT += f"» **NOBITA 𝗦𝗣𝗔𝗠  :** `3.2`\n"
        TEXT += f"» **𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡 𝗩𝗘𝗥𝗦𝗜𝗢𝗡:** `{telethon.__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                event.chat_id,
                "https://telegra.ph/file/0ffefe8fa1edc1a6d0416.jpg",
                caption=TEXT, 
                buttons=PythonButton)
