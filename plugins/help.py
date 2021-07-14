from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def help(client, message):
    helptxt = f"➠ `Send Me YouTube Video Link`\n\n➠ `Wait For Checking Link`\n\n➠ `Select Desired Format`\n\n➠ `Downloading..`\n\n➠ `Uploading To Telegram`\n\n👲 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : [ʙx ʙᴏᴛᴢ](https://t.me/BX_Botz)"
    helpbtn = InlineKeyboardMarkup([[InlineKeyboardButton("Channel ⭕️", url ="https://t.me/EKBOTZ_UPDATE")]])
    await message.reply_text(helptxt, reply_markup = helpbtn)
