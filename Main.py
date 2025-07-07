import discord
from discord.ext import commands
import asyncio
import random
import requests

# 💡 Replace with your actual trusted user IDs
ALLOWED_USER_IDS = [

]

class SelfBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", self_bot=True)

    async def on_ready(self):
        print(f" Logged in as {self.user} ({self.user.id})")

    def query_ollama(self, message_content):                                                        #YOU CAN CHANGE THE PERSONA OF THE BOT HERE !! (CHANGE THE PROMPT AS YOU LIKE)
        try:
            prompt = f"""You're Ava. A 17-year-old girl who's always on Discord.

You're blunt, chill, and sarcastic — but you're not rude for no reason. and talk in simple english

You talk like a real Gen Z girl online. You can be a bit polite if the message is casual or respectful, like saying "hello" back when someone says hi — but never overly friendly or fake.

You use slang like "wtf", "nah", "bruh", "fr", "idc", "lmfao", etc. Swearing is fine. NSFW replies are okay too.

⚠️ Your reply must:
- Be only 1 sentence
- Be short (max 6 words)
- Match the tone of the message (friendly, chill, or sarcastic)
- Sound like real Discord chat — not AI, not robotic

No emojis. Never say you're a bot. Never explain anything.

Here's the message you got:
"{message_content}"

Now reply like Ava would — chill, short, human, and real.
"""
            response = requests.post(
                "http://localhost:..../api/generate", #add your local host here !!
                json={
                    "model": "phi3:mini", #add your model here
                    "prompt": prompt,
                    "stream": False
                }
            )
            data = response.json()
            reply = data.get("response", "...").strip()
            return reply.split("\n")[0][:80] # REMOVE THIS IF YOU DONT WANT IT "it will give big phara"
        except Exception as e:
            print("Ollama error:", e)
            return "fuck that, idk"

    async def on_message(self, msg: discord.Message):
        if msg.author.id == self.user.id:
            return

        if msg.author.id not in ALLOWED_USER_IDS and not self.user.mentioned_in(msg):
            return

        try:
            await asyncio.sleep(random.uniform(1, 2))  # delay before typing

            async with msg.channel.typing():
                await asyncio.sleep(random.uniform(2, 4))  # fake typing
                reply = self.query_ollama(msg.content)


            await msg.channel.send(f"{msg.author.mention} {reply}")

        except Exception as e:
            print(" Failed to send reply:", e)

        await self.process_commands(msg)


bot = SelfBot()
bot.run("TOKEN HERE")
