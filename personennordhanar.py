from discord.ext import commands
import discord

class personen(commands.Cog):
    def __init__(self,mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def kaiser(self, ctx):
        embed = discord.Embed(title="Fakten über den Nordhanarischen Kaiser")
        embed.add_field(name="Name der Person", value="Benedikt Franz Kurt Johann von Seyffenstein-Brülitz")
        embed.add_field(name="Geburtsdatum und Alter", value="10.07.1997, 23 Jahre alt")
        embed.add_field(name="Dienstgrad", value="Reichsmarschall")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def kaiserin(self, ctx):
        embed = discord.Embed(title="Fakten über die Nordhanarische Kaiserin")
        embed.add_field(name="Name der Person", value="Maja von Seyffenstein-Brülitz")
        embed.add_field(name="Geburtsdatum und Alter", value="09.10.1995, 25 Jahre alt")
        embed.add_field(name="Dienstgrad", value="Reichsmarschall")
        await ctx.send(embed=embed)
        return

def setup(bot):
    bot.add_cog(personen(bot))