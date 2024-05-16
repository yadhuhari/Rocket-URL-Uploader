from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Translation:
    START_TEXT = """
Hᴇʏ {} 👋,

I ᴀᴍ URL Uᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ. Jᴜsᴛ sᴇɴᴅ ᴍᴇ ᴀɴʏ Dɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ᴀɴᴅ I ᴡɪʟʟ ᴜᴘʟᴏᴀᴅ ғɪʟᴇ ᴛᴏ ʏᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ 😍

Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : @RocketBotzz

"""

    HELP_TEXT = """

I ᴡɪʟʟ sᴜᴘᴘᴏʀᴛ YᴏᴜTᴜʙᴇ, Gᴏᴏɢʟᴇ Dʀɪᴠᴇ ᴏʀ Aɴʏ Oᴛʜᴇʀ Dɪʀᴇᴄᴛ Lɪɴᴋs..!

Jᴜsᴛ sᴇɴᴅ ᴛʜᴇ ʟɪɴᴋ.

Sᴇʟᴇᴄᴛ ᴛʜᴇ ᴅᴇsɪʀᴇᴅ ᴏᴘᴛɪᴏɴ.

Tʜᴇɴ ʙᴇ ʀᴇʟᴀxᴇᴅ ʏᴏᴜʀ ғɪʟᴇ ᴡɪʟʟ ʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ sᴏᴏɴ..

Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : @RocketBotzz

"""

    # give credit to developer

    ABOUT_TEXT = """
<b>🤖 Mʏ Nᴀᴍᴇ</b> : URL Uᴘʟᴏᴀᴅᴇʀ

<b>🌀 Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ</b> : <a href="https://t.me/RocketBotzz">Rᴏᴄᴋᴇᴛ Bᴏᴛᴢᴢ</a>

<b>🌐 Sᴇʀᴠᴇʀ</b> : <a href="https://render.com/">Rᴇɴᴅᴇʀ</a>

<b>📃 Lᴀɴɢᴜᴀɢᴇ :</b> <a href="https://www.python.org/">Pʏᴛʜᴏɴ</a>

<b>📝 Fʀᴀᴍᴇᴡᴏʀᴋ :</b> <a href="https://docs.pyrogram.org/">Pʏʀᴏɢʀᴀᴍ</a>

<b>👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ :</b> <a href="https://t.me/YourRocketTG">Rᴏᴄᴋᴇᴛ 𝚃𝙶</a>

"""

    PROGRESS = """
🚀 Sᴘᴇᴇᴅ : {3}/s\n\n
☑️ Dᴏɴᴇ : {1}\n\n
📂 Tᴏᴛᴀʟ Sɪᴢᴇ  : {2}\n\n
⏳ Tɪᴍᴇ ʟᴇғᴛ : {4}\n\n
"""
    ID_TEXT = """
🆔 Yᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ ɪᴅ ɪs :- <code>{}</code>
"""

    INFO_TEXT = """
 🤹 Fɪʀsᴛ Nᴀᴍᴇ : <b>{}</b>

 🚴‍♂️ Sᴇᴄᴏɴᴅ Nᴀᴍᴇ : <b>{}</b>

 🧑🏻‍🎓 Usᴇʀɴᴀᴍᴇ : <b>@{}</b>

 🆔 Tᴇʟᴇɢʀᴀᴍ Iᴅ : <code>{}</code>

 📇 Pʀᴏғɪʟᴇ Lɪɴᴋ : <b>{}</b>

 📡 Dᴄ : <b>{}</b>

 📑 Lᴀɴɢᴜᴀɢᴇ : <b>{}</b>

 👲 Sᴛᴀᴛᴜs : <b>{}</b>
"""

    START_BUTTONS = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Hᴇʟᴘ 🛠", callback_data="help"),
                InlineKeyboardButton("Aʙᴏᴜᴛ 🤠", callback_data="about"),
            ],
            [InlineKeyboardButton("Cʟᴏsᴇ 📛", callback_data="close")],
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Hᴏᴍᴇ 🏡", callback_data="home"),
                InlineKeyboardButton("Aʙᴏᴜᴛ 🤠", callback_data="about"),
            ],
            [InlineKeyboardButton("Cʟᴏsᴇ 📛", callback_data="close")],
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Hᴏᴍᴇ 🏡", callback_data="home"),
                InlineKeyboardButton("Hᴇʟᴘ 🛠", callback_data="help"),
            ],
            [InlineKeyboardButton("Cʟᴏsᴇ 📛", callback_data="close")],
        ]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Cʟᴏsᴇ 📛", callback_data="close")]]
    )
    FORMAT_SELECTION = "Nᴏᴡ Sᴇʟᴇᴄᴛ ᴛʜᴇ ᴅᴇsɪʀᴇᴅ ғᴏʀᴍᴀᴛs"
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    DOWNLOAD_START = "Tʀʏɪɴɢ ᴛᴏ Dᴏᴡɴʟᴏᴀᴅ ⌛\n\n <i>{} </i>"
    UPLOAD_START = "<i>{} </i>\n\n📤 Uᴘʟᴏᴀᴅɪɴɢ Pʟᴇᴀsᴇ Wᴀɪᴛ"
    RCHD_TG_API_LIMIT = "Dᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs. /n Dᴇᴛᴇᴄᴛᴇᴅ Fɪʟᴇ Sɪᴢᴇ: {} /nSᴏʀʀʏ. Bᴜᴛ, I ᴄᴀɴɴᴏᴛ ᴜᴘʟᴏᴀᴅ ғɪʟᴇs ɢʀᴇᴀᴛᴇʀ ᴛʜᴀɴ 2GB ᴅᴜᴇ ᴛᴏ Tᴇʟᴇɢʀᴀᴍ API ʟɪᴍɪᴛᴀᴛɪᴏɴs. "
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = (
        "Dᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs.\n\nTʜᴀɴᴋs Fᴏʀ Usɪɴɢ Mᴇ\n\nUᴘʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs"
    )
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = ""
    NO_VOID_FORMAT_FOUND = "ERROR... <code>{}</code>"
    FREE_USER_LIMIT_Q_SZE = "Cannot Process, Time OUT..."
    SLOW_URL_DECED = """
    Gosh that seems to be a very slow URL. Since you were screwing my home,
    I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6
    and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."""
