from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from . import bot_methods

PREFIX = '>'
OWNER_IDS = [360693334014164994, 567726815922225157]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.guild = None
        self.ready = False
        self.scheduler = AsyncIOScheduler()

        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

    def run(self, version):
        self.VERSION = version

        with open('./lib/bot/token.0', 'r', encoding='utf-8') as tokenfile:
            self.TOKEN = tokenfile.read()

        bot_methods.botlog('Running bot')
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        bot_methods.botlog('Bot connected')

    async def on_disconnect(self):
        bot_methods.botlog('Bot disconnected')
    
    async def on_ready(self):
        if not self.ready:
            self.ready = True
            bot_methods.botlog('Bot ready')

        else:
            bot_methods.botlog('Bot reconnected')
    
    async def on_message(self, on_message):
        pass

bot = Bot()