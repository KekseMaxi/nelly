import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.commands import Option


class Greet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @slash_command(description="Begrüße einen User")
    async def greet(
            self, ctx,
            user: Option(discord.Member, "Der User, den du grüßen möchtest")
    ):
        await ctx.respond(f"Moin {user.mention}")


def setup(bot):
    bot.add_cog(Greet(bot))