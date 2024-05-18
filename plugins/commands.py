from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.script import Translation
import random

PICS = [
 "https://telegra.ph/file/38038a13c6bb18fb53e4b.jpg",
 "https://telegra.ph/file/fa9fc021314904dd6786a.jpg",
 "https://telegra.ph/file/28fcd1bbcfa206950ab8a.jpg",
 "https://telegra.ph/file/5c09d90da08efaef738fd.jpg",
 "https://telegra.ph/file/d1f8097bd011aafb75fb4.jpg",
 "https://telegra.ph/file/b7b2cc8dca3c27bf643aa.jpg",
 "https://telegra.ph/file/62f52d20b245b94926087.jpg",
 "https://telegra.ph/file/0c3f45c1c598e9ec2507e.jpg",
 "https://telegra.ph/file/3905e0dbfb73ba2d291f2.jpg",
 "https://telegra.ph/file/0f4db90df9f683e802326.jpg"
]


@Client.on_message(filters.command("start") & filters.private)
async def start_bot(_bot, m: Message):
    await m.reply_photo(
        photo=random.choice(PICS),
        Translation.START_TEXT.format(m.from_user.first_name),
        reply_markup=Translation.START_BUTTONS,
        quote=True,
    )


@Client.on_message(filters.command("help") & filters.private)
async def help_bot(_bot, m: Message):
    await m.reply_photo(
        photo=random.choice(PICS),
        Translation.HELP_TEXT,
        reply_markup=Translation.HELP_BUTTONS,
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command("about") & filters.private)
async def aboutme(_bot, m: Message):
    await m.reply_photo(
        photo=random.choice(PICS),
        Translation.ABOUT_TEXT,
        reply_markup=Translation.ABOUT_BUTTONS
    )
