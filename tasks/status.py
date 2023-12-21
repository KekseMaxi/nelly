import discord
from discord.ext import commands, tasks

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # Start the task when the bot is ready
        self.update_status.start()

    @tasks.loop(seconds=10)  # Update status every 30 seconds (adjust as needed)
    async def update_status(self):
        total_members = sum(guild.member_count for guild in self.bot.guilds)
        game = discord.Game(name=f"with {total_members} users")
        await self.bot.change_presence(activity=game)

    # Rename this method to something without 'cog_'
    @commands.Cog.listener()
    async def unload_cog(self):
        self.update_status.stop()

def setup(bot):
    bot.add_cog(Status(bot))
