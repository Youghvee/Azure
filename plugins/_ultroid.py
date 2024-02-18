# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, ultroid_cmd

REPOMSG = """
▢ **RYN UBOT** •\n
▢ Owner - [Klik disini](https://t.me/Usern4meDoestExist404)
▢ Group - [Klik disini](https://t.me/carisahabatonline_id)
▢ Support - @TatsuyaMusicStream
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://t.me/TatsuyaMusicAss_Bot"),
        Button.url("Developer", "https://t.me/Usern4meDoestExist404"),
    ],
    [Button.url("Support Group", "t.me/Cari_Teman_Virtual_Online_Id")],
]

ULTSTRING = """🎇 **Thanks for Deploying Ryn Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@ultroid_cmd(
    pattern="repo$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info(f"Error while repo command : {str(er)}")
    await e.eor(REPOMSG)


@ultroid_cmd(pattern="ultroid$")
async def useUltroid(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://mallucampaign.in/images/img_1708225735.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
