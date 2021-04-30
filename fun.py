from discord.ext import commands
import discord

class fun(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

        @commands.command()
        async def diggah(ctx):
            embed = discord.Embed(title="Wat?")
            embed.set_image(url="https://media.tenor.com/images/2c474b0b4404b624d80df839bc688b5f/tenor.gif")
            await ctx.send(embed=embed)
            return

def setup(bot):
    bot.add_cog(fun(bot))