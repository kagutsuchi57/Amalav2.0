## ©copyright infringement on Telugu Code

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters          
import asyncio
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream
from modules.clientbot import clientbot
from modules.config import GROUP, NETWORK, BOT_USERNAME

## don't change any value in this repo if you change the value bot will crash your heroku accounts. 


@Client.on_callback_query(filters.regex("home_start"))
async def start_set(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👋🏻 **ʜᴇʟʟᴏ {query.message.from_user.mention()} ɪᴀᴍ ᴀ ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ ᴍᴜsɪᴄ ʙᴏᴛ ɪᴀᴍ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ.. 

ɢʀᴏᴜᴘs ᴡɪᴛʜ sᴏᴍᴇ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.. ᴀɴʏ ʜᴇʟᴘ ʏᴏᴜ ᴡᴀɴᴛ ʜɪᴛ ᴛʜᴇ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅ /help.
""", 
    reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("🧧 ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs 🧧", callback_data="command_list"), 
            ],[
            InlineKeyboardButton("💬 ɪɴғᴏʀᴍᴀᴛɪᴏɴ", callback_data="info"), 
            ],[
            InlineKeyboardButton("🍃 sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP}"), 
            InlineKeyboardButton("📡 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{NETWORK}"), 
            ],[
            InlineKeyboardButton("🍀 ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🍀", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ]]
            ) 
        ) 
   

@Client.on_callback_query(filters.regex("command_list"))
async def commands_set(_, query: CallbackQuery): 
    await query.edit_message_text(
        f"""💗 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 
➠ ʜᴇʟʟᴏ ᴛʜɪs ɪs ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ ɢᴜɪᴅᴇ ᴡʜᴀᴛ ᴄᴏᴍᴍᴀɴᴅ ʏᴏᴜ ɴᴇᴅᴅ sᴇʟᴇᴄᴛ ʜᴇʀᴇ.
""", 
    reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("🧧ɢᴇɴᴇʀᴀʟ ᴄᴏᴍᴍᴀɴᴅs", callback_data="general_list"), 
            ],[
            InlineKeyboardButton("sᴋɪᴘ", callback_data="skip_list"), 
            InlineKeyboardButton("ᴘᴀᴜsᴇ", callback_data="pause_list"), 
            ],[
            InlineKeyboardButton("ʀᴇsᴜᴍᴇ", callback_data="resume_list"), 
            InlineKeyboardButton("sᴛᴏᴘ", callback_data="stop_list"), 
            ],[
            InlineKeyboardButton("ᴘʟᴀʏ", callback_data="play_list"), 
            ],[
            InlineKeyboardButton("◁", callback_data="home_start"), 
            ]]
            ) 
        ) 
    

@Client.on_callback_query(filters.regex("general_list"))
async def general_list(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʜᴇʟʟᴏ 🦊 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

➠ /play - reply to a youtube link or audio to play song.\n
➠ /vplay - reply to a video file for streming it.\n
➠ /vstream - reply to a youtube/live-link/m3u8 url to play video in vc.
➠ /ping - show the bot ping status\n
➠ /uptime - show the bot uptime(group only)\n
➠ /alive - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴀʟɪᴠᴇ ɪɴғᴏ (group help)\n
➠ /help - To know bot cmds.\n
➠ /ghelp - open help menu in grp""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("skip_list"))
async def skip_list(_, query: CallbackQuery): 
    await query.edit_message_text(
        f"""ʜᴇʟʟᴏ 🦊 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

➠ **/skip ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ sᴋɪᴘ ᴛᴏ ɴᴇxᴛ sᴏɴɢ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("pause_list"))
async def pause_list(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʜᴇʟʟᴏ 🦊 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/pause ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ ɪɴ ɢʀᴏᴜᴘ/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("resume_list")) 
async def resume_list(_, query: CallbackQuery): 
    await query.edit_message_text(
        f"""ʜᴇʟʟᴏ 🦊 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ **/resume ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ ʀᴇsᴜᴍᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's..**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("stop_list"))
async def stop_list(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👋🏻 ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

➠ **/end ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ sᴜᴘᴇʀ ɢʀᴏᴜᴘs ғᴏʀ ᴇɴᴅ sᴏɴɢs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's.**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("play_list"))
async def play_list(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

➠ **/play ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ ᴘʟᴀʏ ᴀ sᴏɴɢs(also video) ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs/nᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴀᴅᴍɪɴs ᴀɴᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ's.**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("info"))
async def info(_, query: CallbackQuery):
    await query.answer("information")
    await query.edit_message_text(
        f"""✨ ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
➠ Hey I'm Naomi A Music Robot.\nI Can Stream Video And Audio In High Quality Without Lag.\n\n Just Add Me In Your Group And Make Sure I,m Admin.""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🗑 ʙɪɴ", callback_data="close_panel")]]
        ),
    ) 


@Client.on_callback_query(filters.regex("set_close"))
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("❗ ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs ʙᴜᴛᴛᴏɴ !", show_alert=True)
    await query.message.delete()

@Client.on_callback_query(filters.regex("close_panel"))
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()
