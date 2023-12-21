import discord
from discord.ext import commands
from discord.commands import slash_command, Option


class Activity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @slash_command(description="Ändere den Status beliebig")
    async def activity(
            self, ctx,
            typ: Option(str, choices=["game", "stream"]),
            name: Option(str)
    ):
        if typ == "game":
            act = discord.Game(name=name)

        else:
            act = discord.Streaming(
                name=name,
                url="https://www.twitch.tv/bastighg"
            )

        await self.bot.change_presence(activity=act, status=discord.Status.online)
        await ctx.respond("Status wurde geändert!", ephemeral=True)


    @slash_command(description="Setze den Status zurück")
    async def online(self, ctx):
        total_members = sum(guild.member_count for guild in self.bot.guilds)
        game = discord.Game(name=f"with {total_members} users")
        await self.bot.change_presence(activity=game)
        await ctx.respond("Status wurde zurückgesetzt!", ephemeral=True)

def setup(bot):
    bot.add_cog(Activity(bot))