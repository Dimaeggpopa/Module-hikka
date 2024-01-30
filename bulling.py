# meta developer: @hikkamodes
# scope: hikka_only
# scope: hikka_min 1.2.10
# requires: urllib requests

from asyncio import sleep
import os
from .. import loader, utils
from telethon.tl.functions.users import GetFullUserRequest
import time 
from telethon.tl.types import Message

class соси(loader.Module): 

    '''🙂Напиши любую команду!'''
     
    
    strings = {
    "name": "полностью",
    "loading": "<b>Загрузка...</b>",
    "not_chat": "<b>Test</b>",}

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client
        
        
    async def bullcmd(self, message: Message):
        """𐌿ρ᧐ ᥱδᥲᴛᥱ᧘ьᥴᴛʙ᧐ ᥴ ʍᥲʍ᧐ᥔ😎"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("ᴛʙᴏя ʍᴀᴛь быᴧᴀ ʙыᴇбᴀнᴀ ʍнᴏю, ᴏнᴀ ᴏбᴏᴄᴀннᴀя ᴨᴩᴏᴄᴛиᴛуᴛᴋᴀ</text>")
        
    async def bull2cmd(self, message: Message):
        """𐌿ρ᧐  ɯ᧘юɯᥱᥴᴛʙ᧐👹"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("ᴛы κᥲκ ᧐δ᧐ᥴρᥲннᥲя ɯ᧘юхᥲ, ʙыᥱδᥲннᥲя ᥙ ᧘ᥱжᥲщᥲя ʙ᧐ɜ᧘ᥱ ᥴʙ᧐ᥱᥔ ʍᥱρᴛʙ᧐ᥔ ʍᥲʍᥲɯᥙl</text>")
        
    async def bull3cmd(self, message: Message):
        """𐌿ρ᧐ ᥴᴛᥲρую ᴦнᥙ᧘ь🌫"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("ᴛы ᥱδᥲннᥲя ᥴᴛᥲρᥲя ᴦнᥙ᧘ь нᥱ᧐дуᥰ᧘яющᥲя ρᥱᥲ᧘ьн᧐ᥴᴛᥙ</text>")
        
    async def bull4cmd(self, message: Message):
        """𐌿ρ᧐ δ᧘ядᥙну🎤"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("ᴛы ᧐чκᥲᥴᴛᥲя δ᧘ядᥙнᥲ ᴦ᧐ʙ᧐ρящᥲя хуᥔню ʙʍᥱᥴᴛ᧐ ɸᥲκᴛ᧐ʙ</text>")
        
    async def bull5cmd(self, message: Message):
        """𐌿ρ᧐ κ᧐нчᥱнную ʍᥲᴛь🎹"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("ɜᥲʙᥲ᧘ᥙ ᥴʙ᧐ᥱ уᥱδᥙщн᧐ᥱ ᥱδ᧘᧐ д᧐ щᥱ᧘чκᥲ, ᴛʙ᧐я κ᧐нчᥱннᥲя ʍᥲᴛь ʍ᧐᧘чᥙᴛ дᥲжᥱ ᥴ хуᥱʍ ʙ᧐ ρᴛу</text>")
        
    async def bull6cmd(self, message: Message):
        """𐌿ρ᧐ ᥱδᥲᴛᥱ᧘ьᥴᴛʙ᧐🗿"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("δуду ᴛʙ᧐ю ʍᥲᴛь ᥱδᥲᴛь д᧐ ᴛ᧐ᴦ᧐ ʍ᧐ʍᥱнᴛᥲ ᥰ᧐κᥲ ʙρᥱʍя нᥱ ᧐ᴛʍᥲᴛᥲᥱᴛᥴя д᧐ ϶ρы дᥙн᧐ɜᥲʙρ᧐ʙ</text>")
        
    async def bull7cmd(self, message: Message):
        """𐌿ρ᧐ уδᥙᥔᥴᴛʙ᧐ ʍᥲᴛᥱρᥙ🌄"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("ᴛʙ᧐я ʍᥲᴛь ᥰ᧐ᥴ᧘ᥱ ᥴᥱδя ᧐ᥴᴛᥲʙᥙ᧘ᥲ ᧘ᥙɯь ᥰᥲρу κᥲᥰᥱ᧘ь нᥲ κᥙнжᥲ᧘ᥱ</text>")
        
    async def bull8cmd(self, message: Message):
        """𐌿ρ᧐ ᥲннᥙᴦ ʍᥲᴛᥱρᥙ⚓"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("хуᥱʍ ᴛᥱδя ᥲннᥙᴦᥙ᧘ᥙρ᧐ʙᥲ᧘ ɯ᧘юхᥲ ᴛᥱρᥰᥙ᧘ᥙʙᥲя</text>")
        
    async def bull9cmd(self, message: Message):
        """𐌿ρ᧐ хуᥔ ʙ᧐ ρᴛу🔫"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("ʙынунь хуᥔ ᥙɜ᧐ ρᴛᥲ ᥴын хуᥔнᥙ, я ᴛʙ᧐ё ᥱδᥲ᧘᧐ ʍяᴛ᧐ᥱ нᥲ κ᧐ᥴᴛёρ κᥙну ᥙ д᧐δᥲʙ᧘ю δᥱнɜᥙнᥲ чᴛ᧐δы яρчᥱ ᥰ᧐᧘ыхᥲ᧘ ᧐ᴦ᧐нь ᥰ᧐κᥲ ᴛы ᥰρячᥱɯьᥴя ᴛᥲʍ ɜᥲ юδκу ᥴʙ᧐ᥱᥔ ʍᥲᴛᥱρᥙ</text>")
        
    async def bull10cmd(self, message: Message):
        """𐌿ρ᧐ ᴦуδы ʍᥲᴛᥱρᥙ🫦"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("ᴛʙ᧐я ʍᥲᴛь нᥲκᥲчᥲ᧘ᥲ ᴦуδы ρᥲдᥙ ʍᥱня, ᴛᥱᥰᥱρь я ᥱë ᥱδу 24/7</text>")
        
    async def bull11cmd(self, message: Message):
        """𐌿ρ᧐ ᥴʍᥱρᴛь ρ᧐дных👣"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("κ᧐ᴦдᥲ ᴛы ρ᧐дᥙ᧘ᥴя ʙᥴᥱ ᴛʙ᧐ᥙ ρ᧐дныᥱ ᥰ᧐ʙᥱᥴᥙ᧘ᥙᥴь ᥙ ᥴд᧐х᧘ᥙ ᥰρᥙ ʙᥙдᥱ ᴛᥱδя</text>")
        
    async def bull12cmd(self, message: Message):
        """𐌿ρ᧐ х᧐х᧘᧐ʙᥴκую ɯ᧘юху🎃"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("ᴛы ʙыᥱδᥲннᥲя х᧐х᧘᧐ʙᥴκᥲя ɯ᧘юхᥲ ᧐ᴛᥴᥲᥴыʙᥲющᥲя ʙ᧐ɜ᧘ᥱ ᥰ᧐дʙ᧐ρ᧐ᴛнᥙ</text>")
        
    async def bull13cmd(self, message: Message):
        """𐌿ρ᧐ ρᥲᥴᥰ᧐ρяжᥱнᥙᥱ ʍᥲᴛᥱρᥙ👅"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("я ᴛᥱδя ᥱδу κᥲκ ᧐᧘ᥙᴦᥲρх ᥙ ρᥲᥴᥰ᧐ρяжᥲюᥴь ᴛʙ᧐ᥱᥔ ʍᥲᴛᥱρью κᥲκ х᧐чу</text>")
        
    async def bull14cmd(self, message: Message):
        """𐌿ρ᧐ ᴛᥲᥔᥴκую ɯ᧘юху🫂"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("ᴛы хуᥔ᧘᧐ ᴛᥲᥔᥴκ᧐ᥔ ʙыᥱδᥲнн᧐ᥔ ɯ᧘юхᥙ κ᧐ᴛ᧐ρую ᥰᥱρᥱᥱхᥲ᧘ᥙ κᥲʍᥲɜы ʍᥙ᧘᧘ᥙ᧐ны ρᥲɜ</text>")
        
    async def bull15cmd(self, message: Message):
        """𐌿ρ᧐ ʍᥱρᴛʙую ɯ᧘юху🧖"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("ᥰ᧐ʍ᧐᧘чᥙ хуᥱᴛᥲ, ᥴᥙдᥙ ʙ ᧐δᥙдᥱ уᥱδᥙщныᥔ ʍ᧘ᥲдᥱнᥱц ᥴʙ᧐ᥱᥔ ʍᥱρᴛʙ᧐ᥔ ɯ᧘юхᥙ</text>")
        
    async def bull16cmd(self, message: Message):
        """𐌿ρ᧐ ʙыᥱδᥲнную ᥰρ᧐ᥴᴛᥙᴛκу🌹"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("ᥰ᧐дᥲʙᥙᥴь ᥴʙ᧐ᥙʍ хуᥱʍ ʙ᧐ ρᴛу, ᴛы κᥲκ ʙыᥱδᥲннᥲя ᥰρ᧐ᥴᴛᥙᴛуᴛκᥲ ᧘ᥱжᥲщᥲя ʙ ʍ᧐ᴦᥙ᧘ᥱ ρᥲᥴᴛущᥲя ʙ ᴛ᧐чь ᴛ᧐чь κᥲκ ᥴʙ᧐я ʍᥲʍᥲɯᥲ</text>")
        
    async def bull17cmd(self, message: Message):
        """𐌿ρ᧐ ρ᧐ᴛ ʍᥲʍᥲɯᥙ💄"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("ρ᧐ᴛ ᴛʙ᧐ᥔ ʍᥲʍᥲɯᥙ δы᧘ ʙыᥱδᥲ᧘ ʍн᧐ю ʍн᧐жᥱᥴᴛʙ᧐ ρᥲɜ</text>")
        
    async def bull18cmd(self, message: Message):
        """𐌿ρ᧐ дᥱᥴяᴛь хуëʙ🔮"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("𐌺᧐ʍδᥙнᥙρ᧐ʙᥲнн᧐-ʙыᥱδᥲнныᥔ дᥱᥴяᴛью хуяʍᥙ ᥴын ɯʍᥲ᧘ᥱʙн᧐ᥔ ᥰρ᧐δ᧘ядᥙ</text>")
        
    async def bull19cmd(self, message: Message):
        """𐌿ρ᧐ ɜʍᥱя ᴦ᧐ρынычᥲ🐍"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("Я ᴛᥱδя ᧐ᴛᴛρᥲхᥲю, κᥲκ ᴛρёххуᥔныᥔ ɜʍᥱᥔ ᴦ᧐ρыныч, ρᥲɜ᧐ρʙᥲʙ ʙᥴᥱ ᥲнᥲ᧘ьныᥱ ᥴʙяɜκᥙ</text>")
        
    async def bull20cmd(self, message: Message):
        """𐌿ρ᧐ ᥰρ᧐ᥴᴛыню🥱"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("𐌿ᥙᴛᥱκᥲнᴛρ᧐ᥰ, ᧐δ᧐ᥴρᥲʙɯᥙᥔᥴя ʙ ᥰρ᧐ᥴᴛыню, нᥲдρ᧐чᥙ ᥴᥱδᥱ нᥲ ɯκ᧐᧘ьныᥔ ᥰ᧐дн᧐ᥴ ᥙ ᥴ᧐жρᥙ цᥱ᧘ᥙκ᧐ʍ, ᥰ᧐ᴛ᧐ʍ ᥰᥱρᥱʙᥲρᥙ ᥙ ᥴ᧐жρᥙ ᥱщё ρᥲɜ</text>")
        
    async def bull21cmd(self, message: Message):
        """𐌿ρ᧐ ᥴᥰᥱρʍᥲᴦ᧘᧐ᴛᥲ🫠"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        await message.edit ("Сᥰᥱρʍ᧐ᴦ᧘᧐ᴛ ᥰᥙɜдᥲ᧘᧐δныᥔ ᥴ ᥰ᧐ρʙᥲнныʍ ᥴρᥲκ᧐ᴛᥲн᧐ʍ ᥙ ᧐ᴛδᥙᴛыʍᥙ ᥰ᧐чκᥲʍᥙ</text>")