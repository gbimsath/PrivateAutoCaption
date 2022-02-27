#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (C) PR0FESSOR-99

import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

USERNAME=Config.BOT_USERNAME


# start_Msg, help_msg, about_msg


@Client.on_message(filters.private & filters.command("start"))
async def start_meg(client, update):
    text = f"""<b> 👋Hello {update.from_user.mention}\n\nI am an AutoCaption bot\n\nAll you have to do is add me to your channel and I will show you my power\n\nFor more info check help Button\n\n {MT}</b>"""
    reply_markup =  InlineKeyboardMarkup( [[
        InlineKeyboardButton("help↗️", callback_data="heroku"),
        InlineKeyboardButton("🗣️Group", url="https://t.me/+rWHmdVt3NythYzI1"),
        InlineKeyboardButton("Channel📢", url="https://t.me/MOHLK_MG_UPDATES")
        ]]
    )
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )

@Client.on_callback_query(filters.regex(r"^(heroku|about|ImError_X)$"))
async def callback_data(client, update: CallbackQuery):

    query_data = update.data

    if query_data == "heroku":
        buttons = [[
            InlineKeyboardButton("🖥️ Tutorial Video 🖥️", url="https://youtu.be/p4Z9ZN1lZUk")
            ],[
            InlineKeyboardButton("🏠Home", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("❌️Close", callback_data="ImError_X"),
            InlineKeyboardButton("About↗️", callback_data="about")
            ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            f"""<b>🔻AutoCaption Bot🔻\n\nTake a look at the end of the video\nIt has to say\n\n🖥️Youtube Tutorial Video\n\nHeroku 👉 https://dashboard.heroku.com/\n\n {MT}</b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    if query_data == "about":
        buttons = [[
            InlineKeyboardButton("🗣️Group", url="https://t.me/+rWHmdVt3NythYzI1"),
            InlineKeyboardButton("Channel📢", url="https://t.me/MOHLK_MG_UPDATES"),
            InlineKeyboardButton("My Father", url="https://t.me/ImError_X")
            ],[
            InlineKeyboardButton("🏠Home", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("🔙Back", callback_data="heroku"),
            InlineKeyboardButton("❌️Close", callback_data="ImError_X")
            ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            """<b>➪ Bot Name</b> AutoCaptionBot\n\n➪ <b>Framework : Pyrogram</b>\n\n➪<b> Language : Python</b>\n\n➪<b> Server : Heroku</b> \n\n<b>➪ Version : 2.0.1</b>\n\n<b>➪ Source Code  : <a href="https://github.com/PR0FESS0R-99/PrivateAutoCaption">Touch Me 🤗</a>\n\n➪ Developer :  ImError_X\n\n➪ Credits : <a href="https://github.com/PR0FESS0R-99/PrivateAutoCaption/blob/main/mt_privateautocaption/Credits.md">Credits</a></b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

 
