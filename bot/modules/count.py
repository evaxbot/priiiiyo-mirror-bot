# Implement By https://github.com/anasty17
# © https://github.com/breakdowns/slam-mirrorbot

from telegram.ext import CommandHandler
from bot.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from bot.helper.telegram_helper.message_utils import deleteMessage, sendMessage
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot import dispatcher


def countNode(update, context):
    args = update.message.text.split(" ", maxsplit=1)
    if len(args) > 1:
        link = args[1]
        msg = sendMessage(f"📚 Counting : <code>{link}</code>", context.bot, update)
        gd = GoogleDriveHelper()
        result = gd.count(link)
        deleteMessage(context.bot, msg)
        if update.message.from_user.username:
            uname = f'@{update.message.from_user.username}'
        else:
            uname = f'<a href="tg://user?id={update.message.from_user.id}">{update.message.from_user.first_name}</a>'
        if uname is not None:
            cc = f'\n\n👤 𝗖𝗼𝘂𝗻𝘁𝗲𝗿 : {uname}\n\n🔥 𝗣𝗿𝗶𝗶𝗶𝗶𝘆𝗼 𝗠𝗶𝗿𝗿𝗼𝗿 𝗭𝗼𝗻𝗘\n\n🔥 𝗚𝗿𝗼𝘂𝗽 : @PriiiiyoMirror\n\n▫️#Uploaded To Team Drive ✓ \n\n🚫 𝗗𝗼 𝗡𝗼𝘁 𝗦𝗵𝗮𝗿𝗲 𝗜𝗻𝗱𝗲𝘅 𝗟𝗶𝗻𝗸 \n\n✅ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 : @PriiiiyoBOTs'
        sendMessage(result + cc, context.bot, update)
    else:
        sendMessage("Provide G-Drive Shareable Link to Count.", context.bot, update)

count_handler = CommandHandler(BotCommands.CountCommand, countNode, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(count_handler)
