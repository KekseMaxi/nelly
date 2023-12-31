import os

import discord
from discord.commands import slash_command, Option
from dotenv import load_dotenv


intents = discord.Intents.default()

intents.members = True
intents.message_content = True

bot = discord.Bot(
    intents=intents,
    debug_guilds=None
)

@bot.event
async def on_ready():
    print(f"{bot.user} ist nun Hochgefahren!")


@bot.slash_command(description="Lass den Bot eine wichtige Ankündigung senden")
async def announce(
        ctx,
        text: Option(str, "Die Ankündigung, die du machen möchtest"),
        channel: Option(discord.TextChannel)
):
    await channel.send(text)
    await ctx.respond("Die Ankündigung wurde gesendet", ephemeral=True)



#automatischer cog loader
if __name__ == "__main__":
    for category in ['commands', 'tasks', 'listener']:
        for filename in os.listdir(f'./{category}'):
            if filename.endswith('.py'):
                bot.load_extension(f'{category}.{filename[:-3]}')
                
load_dotenv()
bot.run(os.getenv("TOKEN"))


#@bot.event
#async def on_message(self, msg):
#    if msg.author.bot:
#        return
#    print(f"Nachricht von {msg.author} enthält {msg.content}")




#@bot.event
#async def on_message_delete(msg):
#    await msg.channel.send(f"Eine Nachricht vom {msg.author} wurde gelöscht: {msg.content}")