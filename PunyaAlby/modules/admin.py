# Copyright (C) 2020-2021 by Toni880@Github, < https://github.com/Toni880 >.
#
# This file is part of < https://github.com/Toni880/Prime-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Toni880/Prime-Userbot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio

from pyrogram import Client, filters
from pyrogram.methods.chats.get_chat_members import Filters as ChatMemberFilters
from pyrogram.types import ChatPermissions, Message

from config import CMD_HANDLER as cmd
from PunyaAlby.modules.help import *
from PunyaAlby.helpers.adminhelpers import CheckAdmin
from PunyaAlby.helpers.pyrohelper import get_arg, get_args

add_command_help(
    "admin",
    [
        ["`{cmd}ban`", "Ban pengguna dari obrolan."],
        ["`{cmd}unban`", "Unban pengguna dari obrolan."],
        ["`{cmd}promote`", "-> Promote pengguna sebagai admin grup."],
        ["`{cmd}demote`", _> Menurunkan pengguna dari admin grup."],
        ["`{cmd}mute`", -> Mute pengguna."],
        ["`{cmd}unmute`", -> Unmute pengguna."],
        ["`{cmd}kick`", -> Menendang keluar pengguna dari grup."],
        ["`{cmd}gmute`", -> Tidak memungkinkan pengguna berbicara (bahkan admin)."],
        ["`{cmd}ungmute`", -> Kebalikan dari apa yang dilakukan gmute."],
        ["`{cmd}pin`", -> Menyematkan Pesan.",
        ],
    ],
)

@Client.on_message(filters.command("ban", cmd) & filters.me)
async def ban_hammer(_, message: Message):
    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("**Saya tidak bisa ban siapapun**")
                return
        try:
            get_user = await app.get_users(user)
            await app.kick_chat_member(
                chat_id=message.chat.id,
                user_id=get_user.id,
            )
            await message.edit(f"**Banned {get_user.first_name} dari obrolan.**")
        except:
            await message.edit("**Saya tidak dapat ban akun tersebut**")
    else:
        await message.edit("**Saya bukan admin disini**")


@Client.on_message(filters.command("unban", cmd) & filters.me)
async def unban(_, message: Message):
    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("**Aku butuh seseorang untuk diblokir di sini.**")
                return
        try:
            get_user = await app.get_users(user)
            await app.unban_chat_member(chat_id=message.chat.id, user_id=get_user.id)
            await message.edit(f"**Unbanned {get_user.first_name} dari obrolan**")
        except:
            await message.edit("**Tidak dapat melakukan unban**")
    else:
        await message.edit("**Saya bukan admin disini**")


# Mute Permissions


@Client.on_message(filters.command("mute", cmd) & filters.me)
async def mute_hammer(_, message: Message):
    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("**Saya tidak dapat mute seseorang disini**")
                return
        try:
            get_user = await app.get_users(user)
            await app.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=get_user.id,
                permissions=ChatPermissions(),
            )
            await message.edit(f"**{get_user.first_name} telah di mute**")
        except:
            await message.edit("**Saya tidak dapat mute pengguna ini.**")
    else:
        await message.edit("**Saya bukan admin disini**")


# Unmute permissions


@Client.on_message(filters.command("unmute", cmd) & filters.me)
async def unmute(_, message: Message):
    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("**Siapa yang harus di unmute?**")
                return
        try:
            get_user = await app.get_users(user)
            await app.unban_member(user_id=get_user.id)
            await message.edit(f"**{get_user.first_name} telah di unmute.**")
        except:
            await message.edit("**Saya tidak dapat melakukan unmute ke pengguna ini.**")
    else:
        await message.edit("**Saya bukan admin disini**")


@Client.on_message(filters.command("kick", cmd) & filters.me)
async def kick_user(_, message: Message):
    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("**Siapa yang harus saya tendang?**")
                return
        try:
            get_user = await app.get_users(user)
            await app.kick_chat_member(
                chat_id=message.chat.id,
                user_id=get_user.id,
            )
            await message.edit(f"**Kicked {get_user.first_name} dari obrolan.**")
        except:
            await message.edit("**Saya tidak dapat menendang keluar pengguna itu.**")
    else:
        await message.edit("**Saya bukan admin disini**")


@Client.on_message(filters.command("pin", cmd) & filters.me)
async def pin_message(_, message: Message):
    # First of all check if its a group or not
    if message.chat.type in ["group", "supergroup"]:
        # Here lies the sanity checks
        admins = await app.get_chat_members(
            message.chat.id, filter=ChatMemberFilters.ADMINISTRATORS
        )
        admin_ids = [user.user.id for user in admins]
        me = await app.get_me()

        # If you are an admin
        if me.id in admin_ids:
            # If you replied to a message so that we can pin it.
            if message.reply_to_message:
                disable_notification = True

                # Let me see if you want to notify everyone. People are gonna hate you for this...
                if len(message.command) >= 2 and message.command[1] in [
                    "alert",
                    "notify",
                    "loud",
                ]:
                    disable_notification = False

                # Pin the fucking message.
                await app.pin_chat_message(
                    message.chat.id,
                    message.reply_to_message.message_id,
                    disable_notification=disable_notification,
                )
                await message.edit("`Pesan sudah disematkan!`")
            else:
                # You didn't reply to a message and we can't pin anything. ffs
                await message.edit(
                    "`Balas pesan agar saya dapat menyematkannya dalam grup...`"
                )
        else:
            # You have no business running this command.
            await message.edit("`Saya bukan admin, apa yang harus saya lakukan?`")
    else:
        # Are you fucking dumb this is not a group ffs.
        await message.edit("`Ini bukan tempat di mana saya bisa menyematkan.`")

    # And of course delete your lame attempt at changing the group picture.
    # RIP you.
    # You're probably gonna get ridiculed by everyone in the group for your failed attempt.
    # RIP.
    await asyncio.sleep(3)
    await message.delete()


@Client.on_message(filters.command("promote", cmd) & filters.me)
async def promote(client, message: Message):
    if await CheckAdmin(message) is False:
        await message.edit("**Saya bukan admin disini.**")
        return
    title = "Admin"
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
        title = str(get_arg(message))
    else:
        args = get_args(message)
        if not args:
            await message.edit("**Saya tidak dapat melakukan promote kepada siapapun**")
            return
        user = args[0]
        if len(args) > 1:
            title = " ".join(args[1:])
    get_user = await app.get_users(user)
    try:
        await app.promote_chat_member(message.chat.id, user, can_pin_messages=True)
        await message.edit(
            f"**{get_user.first_name} sekarang didukung dengan hak admin dengan {title} dengan title!**"
        )
    except Exception as e:
        await message.edit(f"{e}")
    if title:
        try:
            await app.set_administrator_title(message.chat.id, user, title)
        except:
            pass


@Client.on_message(filters.command("demote", cmd) & filters.me)
async def demote(client, message: Message):
    if await CheckAdmin(message) is False:
        await message.edit("**Saya bukan admin.**")
        return
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Saya tidak dapat melakukan demote kepada siapapun**")
            return
    get_user = await app.get_users(user)
    try:
        await app.promote_chat_member(
            message.chat.id,
            user,
            is_anonymous=False,
            can_change_info=False,
            can_delete_messages=False,
            can_edit_messages=False,
            can_invite_users=False,
            can_promote_members=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_post_messages=False,
        )
        await message.edit(
            f"**{get_user.first_name} sekarang dilepas dari hak admin mereka!**"
        )
    except Exception as e:
        await message.edit(f"{e}")
