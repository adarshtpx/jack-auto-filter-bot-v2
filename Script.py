import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://www.google.com/')
    START_TXT = environ.get("START_TXT", "Please Set Welcome Message To View This")
    HELP_TXT = """<b>Hey {}
Here is the Help For My Commands</b>"""
    ONE_TXT = """<b>Hey {}
Here is the Help For My Commands</b>"""
    TWO_TXT = """<b>Hey {}
Here is the Help For My Commands</b>"""
    BIO_TXT = """ My Name: {}
Creator: <a href=https://t.me/kkhanyaseen>Yaseen</a>
Library: Pyrogram 
Language : Python"""
    ABOUT_TXT = """ My Name: {}
Creator: <a href=https://t.me/kkhanyaseen>Yaseen</a>
Library: Pyrogram 
Language : Python"""
    SOURCE_TXT =  """<b>NOTE:</b>
- 👊👊👊👊👊"""
    DONATION_TXT = """<b>𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧 & 𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧</b> 
›› <b>𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧</b>
⪼ <b>𝐘𝐨𝐮 𝐂𝐚𝐧 𝐃𝐨𝐧𝐚𝐭𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 💳. 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐅𝐨𝐫 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/AboutAadhi><b>ꪖꪖᦔꫝỉ</b></a> ᚛━━━━━━━━━━━━
›› <b>𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧</b>
⪼ <b>𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐖𝐡𝐢𝐜𝐡 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 . 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮𝐫 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐀𝐧𝐝 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/AboutAadhi><b>ꪖꪖᦔꫝỉ</b></a> ᚛━━━━━━━━━━━━"""
    PROMOTION_TXT = """<b>〄 𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 〄</b>
⪼ <b>𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐖𝐡𝐢𝐜𝐡 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 . 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮𝐫 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐀𝐧𝐝 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/AboutAadhi><b>ꪖꪖᦔꫝỉ</b></a> ᚛━━━━━━━━━━━━""" 
    FILE_TXT = """<b>Commands and Usage.</b>
/autofilter on - Enable auto filter.
/autofilter off - Disable auto filter.
/set_template - Set custom ɪᴍᴅʙ template."""
    WHOIS_TXT ="""<b>Commands and Usage</b>
/whois - For user details"""
    FUN_TXT ="""<b>Games</b> 
    
𝟣. /dice - Role The Dice
𝟤. /Throw 𝗈𝗋 /Dart - To Make Dart 
3. /Runs - Some Random Dialogues
4. /Goal or /Shoot - To Make a Goal or Shoot
5. /luck or /cownd - Spin And Try Your Luck"""
    DEPLOY_TXT = """<b>𝙷𝙾𝚆 𝚃𝙾 𝙳𝙴𝙿𝙻𝙾𝚈..? 
  
<b>✮ Deploy Tutorial ››</b> <i><b>https://youtu.be/kB9TkCs8cX0</b></i>
<b>𝙸𝙵 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙷𝙴 𝙰𝙹𝙰𝚇-𝙿𝚁𝙾-𝙼𝙰𝚇 𝚁𝙴𝙿𝙾 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 <a href=https://t.me/AboutAadhi>𝙰𝙰𝙳𝙷𝙸</a></b>
<b>𝚂𝙷𝙰𝚁𝙴 𝙰𝙽𝙳 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴</b>
𝙲𝚁𝙴𝙳𝙸𝚃𝚂 ›› <a href=https://t.me/MWUpdatez><b>𝙼𝚆-𝚄𝙿𝙳𝙰𝚃𝙴𝚉</b></a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and I will respond whenever a keyword is found the message

<b>NOTE:</b>
1. I should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    SONG_TXT = """<b>Commands and Usage.</b>
</song Song Name>
📌 ᴡᴏʀᴋs ᴏɴʟʏ ᴏɴ ɢʀᴏᴜᴘs."""
    PIN_TXT ="""<b>Commands and Usage.</b>
/pin - To Pin The Message On Your Chat.
/unpin - To Unpin The Current Pinned Message."""
    PASTE_TXT = """<b>Commands and Usage.</b>
/paste [text] - paste the given text on Pasty
<b>NOTE:</b>
• These commands works on both pm and group.
• These commands can be used by any group member."""
    TTS_TXT = """<b>Commands and Usage.</b>
/tts <text> : convert text to speech
<b>NOTE:</b>
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>Usage.</b>
/ping - To get your ping."""
    TELE_TXT = """<b>Commands and Usage.</b>
/telegraph - Send me Picture or Video Under (5MB)
<b>NOTE:</b>
This Command Is Available in goups and pms.
This Command Can be used by everyone."""

    PRIVATEBOT_TXT = """Hey {} I'm Alive."""

    JSON_TXT ="""<b>JSON:</b>
Bot returns json for all replied messages with /json
<b>Features:</b>
Message Editting JSON.
Pm Support.
Group Support."""
    PURGE_TXT = """<b>Usage.</b>
   
/purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- I Support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/kkhanyaseen)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<code>TOTAL FILES: {}</code>
<code>TOTAL USERS: {}</code>
<code>TOTAL CHATS: {}</code>
<code>USED STORAGE: {}</code>
<code>FREE STORAGE: {}</code>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
REPORT_TXT = """<b>Usage.</b>
/report 𝗈𝗋 @admins """

    CORONA_TXT = """<b>Usage.</b>
/report 𝗈𝗋 @admins """

    URLSHORT_TXT = """This Command will Help You To short a Link.
<b>Usage: /short <link>
Example:
<code>/short https://t.me/ddrabit</code>"""

    VIDEO_TXT ="""<b>Youtube Video Downloader.</b>
<b>Usage:</b>
Type: /video <link>
Type: /mp4 <link>"""

    ZOMBIES_TXT = """<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>
<b>Commands and Usage.</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    IMAGE_TXT = """<b>Commands and Usage.</b>
• /imdb  - get the film information from IMDb source.
• /search  - get the film information from various sources."""

    STICKER_TXT = """<b>Usage.</b>
/stickerid - Reply to any sticker for sticker id."""

    YTTHUMB_TXT = """<b>Youtube Video Thumbnail Downloader.</b>
Usage: /ytthumb <video link>
Example: /ytthumb https://youtu.be/UyzJ9KEoU0w"""

    ABOOK_TXT = """<b>You can convert a pdf file to a audio file with this command.</b>
<b>Commands and Usage.</b>
/audiobook - <b>Reply to PDF file to generate the audio.</b>"""

    GTRANS_TXT = """<b>Help: Gᴏᴏɢʟᴇ Tʀᴀɴsʟᴀᴛᴏʀ
Tʀᴀɴsʟᴀᴛᴇ ᴛᴇxᴛs ᴛᴏ ᴀ sᴘᴇᴄɪғɪᴄ ʟᴀɴɢᴜᴀɢᴇ!
Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ: /tr [lang Code][reply] - ᴛʀᴀɴsʟᴀᴛᴇ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ᴛᴏ sᴘᴇᴄɪғɪᴄ ʟᴀɴɢᴜᴀɢᴇ.
NOTE:
While Using /tr you should specify the language code.
Example:
• en = english
• ml = malayalam
• hi = hindi
Type: /tr ml
For More Language Codes Click Here 👇</b>"""

    RESTRIC_TXT = """Some people need to be publicly banned; spammers, annoyances, or just trolls.
This module allows you to do that easily, by exposing some common actions, so everyone will see!
<b>Commands and Usage.</b>
/ban - Ban a user.
/unban - To unban a user.
/tban - Temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
/mute - To mute a user.
/unmute - To unmute a user.
/tmute - Temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks"""
    CREATOR_REQUIRED = """<b>You have To Be The Group Owner To Do That.</b>"""
      
    INPUT_REQUIRED = "**Arguments Required.**"
      
    KICKED = """✔️ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """🚮 Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """<b>Im Not Admin Here. Add Me Again with all admin rights.</b>"""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>Fetching User info...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
