from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🤖 Update Channel", url="https://t.me/BX_Botz"),
         InlineKeyboardButton(
            "👥Support Group", url="https://t.me/BXsupport")]])
    welcomed = f"Hai <b>{message.from_user.mention}</b>\n\n`Iam simple YouTube downloader bot. I Will Convert Youtube Link to Video/File & Mp3.` \n\nFor more details Press /help. \n\n👲 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : [ʙx ʙᴏᴛᴢ](https://t.me/BX_Botz)"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
