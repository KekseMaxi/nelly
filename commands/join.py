import discord
from discord.ext import commands


class Join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(
            title="Wilkommen!",
            description=f"Moin {member.mention}",
            color= discord.Color.purple()
        )

        channel = await self.bot.fetch_channel(1155984518071717990)
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Join(bot))