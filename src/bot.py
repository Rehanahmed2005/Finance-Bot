import os
import asyncio
import telegram

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

async def main():
    bot = telegram.Bot(TOKEN)
    async with bot:
        await bot.send_message(text='Hi Rehan!', chat_id=6584016896)

if __name__ == '__main__':
    asyncio.run(main())
