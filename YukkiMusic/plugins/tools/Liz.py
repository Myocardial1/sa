import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from YukkiMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

@app.on_message(filters.regex("^روابط الحذف$"))
async def delet(client: Client, message: Message):
    await message.reply_text(f"""**- اهلين عمري\n-› هذول روابط حذف جميع مواقع التواصل بالتوفيق**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Telegram •", url=f"https://my.telegram.org/auth?to=delete"),
                    InlineKeyboardButton(
                        "• Instagram •", url=f"https://www.instagram.com/accounts/login/?next=/accounts/remove/request/permanent/"),
                ],[
                    InlineKeyboardButton(
                        "• Snapchat •", url=f"https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fdeleteaccount"),
                    InlineKeyboardButton(
                        "• Facebook •", url=f"https://www.faecbook.com/help/deleteaccount"),
                ],[
                    InlineKeyboardButton(
                        "• Twitter •", url=f"https://mobile.twitter.com/settings/deactivate"),
                    InlineKeyboardButton(
                        "• قناة المطور •", url=f"https://t.me/sx_hu"),

                ],
            ]
        ),
    )



@app.on_message(filters.command("نادي المطور", [".", ""]) & filters.group)
async def kstr(client: Client, message: Message):
       chat = message.chat.id
       gti = message.chat.title
       link = await app.export_chat_invite_link(chat)
       usr = await client.get_users(message.from_user.id)
       chatusername = f"@{message.chat.username}"
       user_id = message.from_user.id
       user_ab = message.from_user.username
       user_name = message.from_user.first_name
       buttons = [[InlineKeyboardButton(gti, url=f"{link}")]]
       reply_markup = InlineKeyboardMarkup(buttons)
       
       await app.send_message(1576257432, f"- قام {message.from_user.mention}\n- بمناداتك عزيزي المطور\n- ايديه {user_id}\n- يوزره @{user_ab}\n- ايدي القروب {message.chat.id}\n- يوزر القروب {chatusername}",
       reply_markup=reply_markup,
       )
       await message.reply_text(
        f"""- **عمري راسلت المطور يدخل للكروب ويشوف مشكلتك بأقرب وقت\n\n- تابع قناة البوت** -› [ᴋᴏʏᴇʙ sᴏᴜʀᴄᴇ](t.me/sx_hu)""", disable_web_page_preview=True     
    )


        
@app.on_message(filters.group & command("السورس"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""**- اهلين فيك بسورس كويب ياحلو
• عندك استفسار او اقتراح بخصوص البوت تواصل مع مطور البوت**
مطور السورس -› [𝑂𝑚𝑎𝑟 𝑎𝑙’𝑠ℎ𝑢𝑗𝑒𝑟𝑦](t.me/nnhnn)
قناة المطور -› [ᴋᴏʏᴇʙ sᴏᴜʀᴄᴇ](https://t.me/sx_hu)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "تحديثات البوت 〆", url=f"https://t.me/sx_hu"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لكروبك 🎻", url=f"https://t.me/Hdtkbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )
   
