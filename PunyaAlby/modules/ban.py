from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message
from PunyaAlby.modules.help import *

@Client.on_message(filters.group & filters.command("ban", ["."]) & filters.me)  
async def member_ban(client: Client, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        chat_id = message.chat.id
        me_m =await client.get_me
        me_ = await message.chat.get_member(int(me_m.id))
        if not me_.can_restrict_members:
         await message.edit("`You Don't Have Ban Permission!`")
         return
        can_ban= True
        if can_ban:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id
                else:
                    usr = await client.get_users(message.command[1])
                    user_id = usr.id
            except IndexError:
                await message.edit_text("I cant ban a void xD")
                return
            if user_id:
                try:
                    await client.kick_chat_member(chat_id, user_id)
                    await message.delete()
                except UsernameInvalid:
                    await message.edit_text("`invalid username`")
                    return

                except PeerIdInvalid:
                    await message.edit_text("`invalid username or userid`")
                    return

                except UserIdInvalid:
                    await message.edit_text("`invalid userid`")
                    return

                except ChatAdminRequired:
                    await message.edit_text("`permission denied`")
                    return

                except Exception as e:
                    await message.edit_text(f"**Log:** `{e}`")
                    return

        else:
            await message.edit_text("`permission denied`")
            return
    else:
        await message.delete()

@Client.on_message(filters.group & filters.command("unban", ["."]) & filters.me)  
async def member_unban(client: Client, message: Message):
    msg_id=message.message_id
    chat_msg=message.text
    username=None
     
    if "@" in chat_msg:
        index=chat_msg.index("@")     
        chat_msg=str(chat_msg)
        username=chat_msg[index+1:len(chat_msg)]
    else:                   
        username=message.reply_to_message.from_user.id

    chat_id=message.chat.id
    me_m =await client.get_me()
    me_ = await message.chat.get_member(int(me_m.id))
    user_info=await client.get_users(username)
    if me_.can_restrict_members:      
        await client.unban_chat_member(chat_id , username)
        if(user_info.username):
            usercontact=user_info.username
            reply_string="@"+usercontact+" has been picked up from hell 😈"
            await client.edit_message_text(chat_id , msg_id , reply_string)
        else:
            usercontact=user_info.first_name
            reply_string=usercontact+" has been picked up from 😈"
            await client.edit_message_text(chat_id , msg_id , reply_string)
    else:
        reply_string="Noob,you can't unban members 😂 !"
        await client.edit_message_text(chat_id , msg_id , reply_string )

add_command_help(
    "ban",
    [
        [".ban", "ban akun target."],
    ],
)

add_command_help(
    "unban",
    [
        [".unban", "mengembalikan akun target yang terkena ban."],
    ],
)
