# meta developer: @hikkamodes
# scope: hikka_only
# scope: hikka_min 1.2.10
# requires: urllib requests
import random
from asyncio import sleep
import os
from .. import loader, utils
from telethon.tl.functions.users import GetFullUserRequest
import time 
from telethon.tl.types import Message

class voicemal(loader.Module): 

    '''🙂Напиши любую команду!'''
     
    
    strings = {
    "name": "полностью",
    "loading": "<b>Загрузка...</b>",
    "not_chat": "<b>Test</b>",}

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client
       
    async def gqcmd(self, message):
        """- А ɜᴀчᴇʍ  ᴛᴇбᴇ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
        
            message.to_id,
            "https://t.me/gs12lett/5", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gwmd(self, message):
        """- Дᥲ ᥲ ᴛы"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/7", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gecmd(self, message):
        """- А ᴛы"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/8", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def grcmd(self, message):
        """- А чᴛᴏ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/9", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gtcmd(self, message):
        """- Вᴏɜʍᴏжнᴏ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
        
            message.to_id,
            "https://t.me/gs12lett/10", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gycmd(self, message):
        """- Обиднᴏ ᴋᴀᴋ бы"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/11", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gucmd(self, message):
        """- Мᴏй ᴀйди ʙᴋ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/12", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gicmd(self, message):
        """- Мᴏй ɜᴀйᴋᴀ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/13", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gocmd(self, message):
        """- Ну ʍнᴇ инᴛᴇᴩᴇ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
        
            message.to_id,
            "https://t.me/gs12lett/14", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gpcmd(self, message):
        """- Мнᴇ 13"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/15", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gscmd(self, message):
        """- Мᴏжᴇᴛ ᴨᴏйᴛи ʙ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/17", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gdcmd(self, message):
        """- Мᴏжᴇᴛ быᴛь"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
        
            message.to_id,
            "https://t.me/gs12lett/18", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def ggcmd(self, message):
        """- Нᴏᴩʍᴀᴧьнᴏ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/20", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def ghcmd(self, message):
        """- Аᴧᴏ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/21", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gjcmd(self, message):
        """- Нᴇ ᴨᴏᴋᴀжу"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
        
            message.to_id,
            "https://t.me/gs12lett/23", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gkcmd(self, message):
        """- Ой ʙᴄë"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/24", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def glcmd(self, message):
        """- Нᴇ ᴄᴋᴀжу"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/25", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gzcmd(self, message):
        """- Нᴇ ʙᴩи"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/26", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gxcmd(self, message):
        """- Нᴇ дуʍᴀю"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
        
            message.to_id,
            "https://t.me/gs12lett/27", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gccmd(self, message):
        """- Нᥱ ᥰ᧐ня᧘ᥲ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/28", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gvcmd(self, message):
        """- Нᴇ ᴨиɯи ʍнᴇ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/29", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gbcmd(self, message):
        """- Нᴇᴀ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/30", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gncmd(self, message):
        """- Нᴇ буду"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
        
            message.to_id,
            "https://t.me/gs12lett/31", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def gmcmd(self, message):
        """- Нᴇ ɜнᴀю"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/32", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qqcmd(self, message):
        """- Нᴇ ᴨᴧᴏхᴏ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/33", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qwcmd(self, message):
        """- Я бᴇᴄᴨᴧᴀᴛнᴏ нᴇ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/34", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qecmd(self, message):
        """- Нᴇᴛ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
        
            message.to_id,
            "https://t.me/gs12lett/35", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qrcmd(self, message):
        """- Нᴇᴛу"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/36", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qtcmd(self, message):
        """- Вᴄë удᴀчи"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/37", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qycmd(self, message):
        """- Вᴄë"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/38", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qucmd(self, message):
        """- Оᴛᴋудᴀ ᴛы"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/39", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qicmd(self, message):
        """- Оᴛᴋудᴀ ᴛы ɜн"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/40", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qpcmd(self, message):
        """- Ну бᴧин"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/41", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qacmd(self, message):
        """- Ну дᴀ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/42", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qscmd(self, message):
        """- Ну ᴨᴏдуʍᴀю"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/43", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qdcmd(self, message):
        """- Ну чᴛᴏ ᴛᴀʍ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/44", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qfcmd(self, message):
        """- Муɜыᴋу ᴄᴧуɯᴀю"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/45", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qgcmd(self, message):
        """- Очᴇнь ᴨᴩияᴛнᴏ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/46", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
       
    async def qhcmd(self, message):
        """- Дᴀ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/47", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qjcmd(self, message):
        """- Дᴏбᴀʙь ʍᴇня ʙ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/48", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qkcmd(self, message):
        """- Дᴀʙᴀй ɜᴀʙᴛᴩᴀ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/49", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qlcmd(self, message):
        """- Дᴀʙᴀй ᴄᴇйчᴀᴄ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/50", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qzcmd(self, message):
        """- Дᴏбᴩᴏᴇ уᴛᴩᴏ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/51", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qxcmd(self, message):
        """- Дᴏбᴩый ʙᴇчᴇᴩ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
        
            message.to_id,
            "https://t.me/gs12lett/52", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qccmd(self, message):
        """- Дᴏбᴩый дᴇнь"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/53", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qvcmd(self, message):
        """- Зᴀʙᴛᴩᴀ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/54", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qbcmd(self, message):
        """- Лᴀднᴏ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/55", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qncmd(self, message):
        """- Пᴏᴨᴏɜжᴇ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
        
            message.to_id,
            "https://t.me/gs12lett/56", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def qmcmd(self, message):
        """- Зᴀй"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/57", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wqcmd(self, message):
        """- Пᴏйдᴇᴛ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/58", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wwcmd(self, message):
        """- Пᴏᴋᴀ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/59", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wecmd(self, message):
        """- Пᴏᴛᴏʍ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
        
            message.to_id,
            "https://t.me/gs12lett/60", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wrcmd(self, message):
        """- Иди нᴀхуй"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/61", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wtcmd(self, message):
        """- Иɜʙини ᴨᴏжᴀᴧуйᴄᴛᴀ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/62", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wycmd(self, message):
        """- Иɜʙини"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/63", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wucmd(self, message):
        """- Пᴧᴏхᴏ ᴄᴧыɯнᴏ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
        
            message.to_id,
            "https://t.me/gs12lett/64", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wocmd(self, message):
        """- Пидр"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/66", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wpcmd(self, message):
        """- Прости"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/67", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wacmd(self, message):
        """- Пᴩиʙᴇᴛ дᴀʙᴀй"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
        
            message.to_id,
            "https://t.me/gs12lett/68", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wscmd(self, message):
        """- Пᴩиʙᴇᴛ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/69", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wdcmd(self, message):
        """- Пᴩиʙᴇᴛиᴋ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/70", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wfcmd(self, message):
        """- Пᴩиᴋинь"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/71", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def whcmd(self, message):
        """- Пᴧᴏхᴏ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
        
            message.to_id,
            "https://t.me/gs12lett/72", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def whcmd(self, message):
        """- Плохо"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/73", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wjcmd(self, message):
        """- Кᴀᴋ хᴏчᴇɯь"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/74", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wkcmd(self, message):
        """- Кидᴀй"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/75", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wlcmd(self, message):
        """- Кᴩᴀᴄиʙᴏ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
        
            message.to_id,
            "https://t.me/gs12lett/76", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wzcmd(self, message):
        """- Кᴩуᴛᴏ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/77", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wxcmd(self, message):
        """- Кᴛᴏ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/78", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wccmd(self, message):
        """- Гуᴧяᴛь ᴄᴏбиᴩᴀюᴄь"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/79", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wvcmd(self, message):
        """- С ᴨᴩᴀɜдниᴋᴏʍ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
        
            message.to_id,
            "https://t.me/gs12lett/106", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wbcmd(self, message):
        """- Виᴋᴀ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/81", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wncmd(self, message):
        """- Сᴧᴀдᴋих ᴄнᴏʙ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/108", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def wmcmd(self, message):
        """- Сᴨᴏᴋᴏйнᴏй нᴏчи"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/109", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def eqcmd(self, message):
        """- Сᴋᴏᴧьᴋᴏ ᴛᴇбᴇ ᴧᴇᴛ"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/110", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def ewcmd(self, message):
        """- Сᴋинь"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/111", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def ercmd(self, message):
        """- Ты хᴏчᴇɯь ʍᴇня """
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/113", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def etcmd(self, message):
        """- Я ᴏбидᴇᴧᴀᴄь"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/gs12lett/114", 
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return