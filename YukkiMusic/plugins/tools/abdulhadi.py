import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
import re
import sys
from config import BANNED_USERS, MUSIC_BOT_NAME
from pyrogram import filters
import config
from YukkiMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)

@app.on_message(
    command(["المطور","مطور السورس","مطور"])
    & ~filters.edited
)
async def zohary(client: Client, message: Message):
    usr = await client.get_users(5338950085)
    name = usr.first_name
    user = await client.get_chat(5338950085)
    Bio = user.bio
    async for photo in client.iter_profile_photos(5338950085, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""𝘿𝙚𝙫 | - [{usr.first_name}](https://t.me/AAAQQQ) 🕷
                        
𝙐𝙨𝙚𝙧 𝘿𝙚𝙫 | - @AAAQQQ 🕷
                           
𝘽𝙞𝙤 | - {Bio} 🕷           
                          
𝙄𝙙 | - 5148163805 🕷 """, 
reply_markup=InlineKeyboardMarkup(
          [                   
            [                   
              InlineKeyboardButton (name, url=f"https://t.me/AAAQQQ")
            ],               
          ]              
       )              
    )                     
                    sender_id = message.from_user.id
                    message_link = await Telegram.get_linok(message)
                    adox = "@AAAQQQ"
                    sender_name = message.from_user.first_name
                    invitelink = await client.export_chat_invite_link(message.chat.id)
                    await app.send_message(5293360705, f"مطوري العزيز {adox}\n\n هاذ {message.from_user.mention} بينادي عليك \n\n الايدي : {sender_id} \n\n اسمه : {sender_name} \n\n رابط الرسالة : {message_link} \n\n رابط الكروب : {invitelink}")
                    if await is_on_off(config.LOG):
                       return await app.send_message(
                           config.LOG_GROUP_ID,
                           f"مطوري العزيز {adox}\n\n هاذ {message.from_user.mention} بينادي عليك \n\n الايدي : {sender_id} \n\n اسمه: {sender_name}",
                       )                 
