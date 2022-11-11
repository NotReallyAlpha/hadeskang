from telegram import Update 
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
from config import BOT_TOKEN, SUDO_USERS

async def start(u: Update, c: CallbackContext):
    await u.message.reply_text(f"Hello ! {u.effective_user.mention_html()}, Am kang bot of Hades Network, only Sudos can use me !")

ALPHA = False

ARGS = None

ENTERED = False

V = []

YashuAlpha_oP = True

async def kang(u: Update, c: CallbackContext):
    global ALPHA
    global ARGS
    global ENTERED
    global V
    m = u.effective_message
    user = u.effective_user
    if not user.id in SUDO_USERS:
        return
    text = c.args
    if len(text) != 2:
        return await m.reply_text("/hkang [emoji] [packnum]")
    emoji = text[0]
    pack = text[1]
    if not m.reply_to_message.sticker:
        return await m.reply_text("BRUH ! 🥲🥲\n\nReply to sticker !")
    type = m.reply_to_message.sticker
    if type.is_video:
        format = "video"
    elif type.is_animated:
        format = "animated"
    else:
        format = "normal"
    sticid = type.file_id
    pack_name = f"Hades_of_{user.id}_by_{c.bot.username}_{format}_{pack}"
    x = c.bot.get_sticker_set(pack_name)
    if not x:
        await m.reply_text("Seems like new pack !\n\nSet name of new pack by using `/setpname` [name]")
        ALPHA = True
        V = user.id
        if ENTERED:
            title = ARGS
            if format == "video":
                c.bot.create_new_sticker_set(user_id=user.id, name=pack_name, title=title, emojis=emoji, webm_sticker=sticid)
            elif format == "animated":
                c.bot.create_new_sticker_set(user_id=user.id, name=pack_name, title=title, emojis=emoji, tgs_sticker=sticid)
            else:
                c.bot.create_new_sticker_set(user_id=user.id, name=pack_name, title=title, emojis=emoji, png_sticker=sticid)
            ENTERED = False
            ARGS = None
            return await m.reply_text(f"your pack is [here](t.me/addstickers/{pack_name})")
    else:
        if format == "video":
            c.bot.add_sticker_to_set(user_id=user.id, name=pack_name, emojis=emoji, webm_sticker=sticid)
        elif format == "animated":
            c.bot.add_sticker_to_set(user_id=user.id, name=pack_name, emojis=emoji, tgs_sticker=sticid)
        else:
            c.bot.add_sticker_to_set(user_id=user.id, name=pack_name, emojis=emoji, png_sticker=sticid)
        return await m.reply_text(f"your pack is [here](t.me/addstickers/{pack_name})")

async def get_args(u: Update, c: CallbackContext):
    global ALPHA
    global ENTERED
    global ARGS
    global V
    if not u.effective_user.id == V:
        return
    if ALPHA:
        args = c.args
        x = []
        for arg in args:
            x.append(arg)
        ARGS = x
        ENTERED = True
        ALPHA = False

async def del_sticker(u: Update, c: CallbackContext):
    m = u.effective_message
    if not user.id in SUDO_USERS:
        return
    if not m.reply_to_message.sticker:
        return await m.reply_text("reply to a stixker vruh! ")
    try:
        c.bot.delete_sticker_from_set(m.reply_to_message.sticker.file_id)
    except Exception as e:
        await m.reply_text(f"can't delete.. \n\n{e}")

async def get_pack(u: Update, c: CallbackContext):
    m = u.effective_message
    user = u.effective_user
    if not user.id in SUDO_USERS:
        return
    text = c.args
    if len(text) != 2:
        return await m.reply_text("/getpack [format] [packnum]")
    pack_name = f"Hades_of_{user.id}_by_{c.bot.username}_{text[0]}_{text[1]}"
    await m.reply_text(f"your pack is [here](t.me/addstickers/{pack_name})")

def Asynchorous():
    print("Asyncio bot started !\nYashuAlpha ✨💭❤️")
    Yashu = ApplicationBuilder().token(BOT_TOKEN).build()
    Yashu.add_handler(CommandHandler("hkang", kang))
    Yashu.add_handler(CommandHandler("setpname", get_args))
    Yashu.add_handler(CommandHandler("dsticker", del_sticker))
    Yashu.add_handler(CommandHandler("getpack", get_pack))
    Yashu.add_handler(CommandHandler("start", start))

    Yashu.run_polling()

if YashuAlpha_oP:
    Asynchorous()
