from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["about"]))
async def start(client, message):

    about = "➠ **Bot** : `Youtube Downloader` \n\n➠ **Creator** : [ᴍʜᴅ ᴍᴜꜰᴀz](https://telegram.dog/Mufaz123) \n\n➠ **Channel** : @BX_Botz \n\n➠ **Source** : [Click here](https://t.me/nokiyirunnoippokitum) \n\n➠ **Language** : [Python3](https://python.org/) \n\n➠ **Library** : [Pyrogram](https://pyrogram.org/) \n\n➠ **Server** : [Heroku](https://heroku.com/)"
    await message.reply_text(about)
