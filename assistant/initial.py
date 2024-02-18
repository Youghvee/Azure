# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import re

from . import *

STRINGS = {
    1: """🎇 **Thanks for Deploying RynUBot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage.""",
    2: """🎉** About RynUBot**

🧿 RynUBot is Pluggable and powerful Telethon Userbot, made in Python from Scratch. It is Aimed to Increase Security along with Addition of Other Useful Features.

❣ Made by **@Usern4meDoestExist404**""",
    3: """**💡• FAQs •**

-> [Username Tracker](https://t.me/Usern4meDoestExist404)
-> [Keeping Custom Addons Repo](https://t.me/Usern4meDoestExist404)
-> [Disabling Deploy message](https://t.me/Usern4meDoestExist404)
-> [Setting up TimeZone](https://t.me/Usern4meDoestExist404)
-> [About Inline PmPermit](https://t.me/Usern4meDoestExist404)
-> [About Dual Mode](https://t.me/Usern4meDoestExist404)
-> [Custom Thumbnail](https://t.me/Usern4meDoestExist404)
-> [About FullSudo](https://t.me/Usern4meDoestExist404)
-> [Setting Up PmBot](https://t.me/Usern4meDoestExist404)
-> [Also Check](https://t.me/Usern4meDoestExist404)

**➻ To Know About Updates**
  - Join @carisahabatonline_id.""",
    4: f"""➻ `To Know All Available Commands`

  - `{HNDLR}help`
  - `{HNDLR}cmds`""",
    5: """➻ **For Any Other Query or Suggestion**
  - Move to **@carisahabatonline_id**.

• Thanks for Reaching till END.""",
}


@callback(re.compile("initft_(\\d+)"))
async def init_depl(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 5:
        return await e.edit(
            STRINGS[5],
            buttons=Button.inline("◁ ʙᴀᴄᴋ", "initbk_4"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", f"initbk_{str(CURRENT - 1)}"),
            Button.inline(">>", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )


@callback(re.compile("initbk_(\\d+)"))
async def ineiq(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 1:
        return await e.edit(
            STRINGS[1],
            buttons=Button.inline("sᴛᴀʀᴛ ʙᴀᴄᴋ ▷", "initft_2"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", f"initbk_{str(CURRENT - 1)}"),
            Button.inline(">>", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )
