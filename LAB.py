# T.ME/GGModules
# T.ME/ASaGGa1_TYT
# meta developer: @ASaGGa1_TYT
#           ░█████╗░░██████╗░█████╗░░██████╗░░██████╗░░█████╗░░░███╗░░░░░░░████████╗██╗░░░██╗████████╗  
#           ██╔══██╗██╔════╝██╔══██╗██╔════╝░██╔════╝░██╔══██╗░████║░░░░░░░╚══██╔══╝╚██╗░██╔╝╚══██╔══╝  
#           ███████║╚█████╗░███████║██║░░██╗░██║░░██╗░███████║██╔██║░░░░░░░░░░██║░░░░╚████╔╝░░░░██║░░░  
#           ██╔══██║░╚═══██╗██╔══██║██║░░╚██╗██║░░╚██╗██╔══██║╚═╝██║░░░░░░░░░░██║░░░░░╚██╔╝░░░░░██║░░░  
#           ██║░░██║██████╔╝██║░░██║╚██████╔╝╚██████╔╝██║░░██║███████╗███████╗██║░░░░░░██║░░░░░░██║░░░  
#           ╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░░╚═╝░░░░░░╚═╝░░░  
#           ░██████╗░░██████╗░███╗░░░███╗░█████╗░██████╗░██╗░░░██╗██╗░░░░░███████╗░██████╗
#           ██╔════╝░██╔════╝░████╗░████║██╔══██╗██╔══██╗██║░░░██║██║░░░░░██╔════╝██╔════╝
#           ██║░░██╗░██║░░██╗░██╔████╔██║██║░░██║██║░░██║██║░░░██║██║░░░░░█████╗░░╚█████╗░
#           ██║░░╚██╗██║░░╚██╗██║╚██╔╝██║██║░░██║██║░░██║██║░░░██║██║░░░░░██╔══╝░░░╚═══██╗
#           ╚██████╔╝╚██████╔╝██║░╚═╝░██║╚█████╔╝██████╔╝╚██████╔╝███████╗███████╗██████╔╝
#           ░╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝░╚════╝░╚═════╝░░╚═════╝░╚══════╝╚══════╝╚═════╝░
from telethon import events, functions, types
from .. import loader, utils
import asyncio

@loader.tds
class LAB(loader.Module):
    """По командам 'л' и 'бл' пишет млаб/блаб\n by @GGModules & @ASaGGa1_TYT"""
    strings = {'name': 'Лаб'}

    async def client_ready(self, client, db):
        self.client = client
        self.db = db

        # Получаем ID владельца бота
        self.owner_id = (await self.client.get_me()).id  

        # Настройки базы данных
        if not self.db.get(__name__, "public_groups"):
            self.db.set(__name__, "public_groups", [])
        if not self.db.get(__name__, "private_groups"):
            self.db.set(__name__, "private_groups", [])
        if not self.db.get(__name__, "direct_chats"):
            self.db.set(__name__, "direct_chats", [])

    async def watcher(self, message):
        """Обработчик сообщений для всех команд и проверки владельца бота."""

        # Проверяем, что сообщение отправлено владельцем
        if message.sender_id != self.owner_id:
            return  # Игнорируем сообщение, если отправитель не владелец

        # Приводим текст сообщения к нижнему регистру для удобства
        text = message.text.lower()

        # Проверяем команды
        if text == "л":
            # Отправляем команду "млаб" боту @bio_attacker_bot
            bot_response = await self.client.send_message("@bio_attacker_bot", "млаб")
            await asyncio.sleep(0.3)

            # Ищем ответное сообщение от бота
            async for response in self.client.iter_messages("@bio_attacker_bot", limit=1):
                if response.reply_to_msg_id == bot_response.id:
                    await self.client.forward_messages(
                        entity=message.chat_id,
                        messages=response.id,
                        from_peer="@bio_attacker_bot"
                    )
                    break

        elif text == "бл":
            # Отправляем команду "блаб" боту @bio_attacker_bot
            bot_response = await self.client.send_message("@bio_attacker_bot", "блаб")
            await asyncio.sleep(0.3)

            # Ищем ответное сообщение от бота
            async for response in self.client.iter_messages("@bio_attacker_bot", limit=1):
                if response.reply_to_msg_id == bot_response.id:
                    await self.client.forward_messages(
                        entity=message.chat_id,
                        messages=response.id,
                        from_peer="@bio_attacker_bot"
                    )
                    break
