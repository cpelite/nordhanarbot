from discord.ext import commands
import discord

class monarchen(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

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
        embed.add_field(name="Dienstgrad", value="-")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def jennifer(self, ctx):
        embed = discord.Embed(title="Fakten über die Erzherzogin von Seyffenstein")
        embed.add_field(name="Name der Person", value="Jennifer Theresa Lisa Deborah von Seyffenstein")
        embed.add_field(name="Geburtsdatum und Alter", value="25.03.1975, 46 Jahre alt")
        embed.add_field(name="Dienstgrad", value="Generaloberst e.H")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def fritzviktor(self, ctx):
        embed = discord.Embed(title="Fakten über den Bajarischen König")
        embed.add_field(name="Name der Person", value="Friedrich Viktor August von Bajar")
        embed.add_field(name="Geburtsdatum und Alter", value="-")
        embed.add_field(name="Dienstgrad", value="-")
        await ctx.send(embed=embed)
        return

class personen(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def svh(self, ctx):
        embed = discord.Embed(title="Fakten über Sebastian von Hammer")
        embed.add_field(name="Name der Person", value ="Sebastian von Hammer")
        embed.add_field(name="Geburtsdatum und Alter", value="18.08.1980, 40 Jahre alt")
        embed.add_field(name="Dienstgrad", value="Oberst e.H.")
        embed.add_field(name="Ämter die die Person aktuell bekleidet", value = "Präsident der Regierung, Parteipräsident der Liberalen")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def drechsler(self, ctx):
        embed = discord.Embed(title="Fakten über Sarah Drechsler")
        embed.add_field(name="Name der Person", value="Sarah von Drechsler")
        embed.add_field(name="Geburtsdatum und Alter", value="19.02.1971, 50 Jahre alt")
        embed.add_field(name="Dienstgrad", value="-")
        embed.add_field(name="Ämter die die Person aktuell bekleidet", value ="2. Präsidentin der Reichsdiät")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def daimek(self, ctx):
        embed = discord.Embed(title="Fakten über Rainer von Daimek")
        embed.add_field(name="Name der Person", value="Rainer von Daimek")
        embed.add_field(name="Geburtsdatum und Alter", value="05.10.1938, 82 Jahre alt")
        embed.add_field(name="Dienstgrad", value="Brigadier a. D.")
        embed.add_field(name="Ämter die die Person aktuell bekleidet", value="Vizepräsident der Regierung, Minister für Verteidigung")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def langbrook(self, ctx):
        embed = discord.Embed(title="Fakten über Leonidas Langbrook")
        embed.add_field(name="Name der Person", value="Leonidas Langbrook")
        embed.add_field(name="Geburtsdatum und Alter", value="17. April 1939")
        embed.add_field(name="Dienstgrad", value="-")
        embed.add_field(name="Ämter die die Person aktuell bekleidet", value="Präsident der kaiserlichen Justiz")
        await ctx.send(embed=embed)
        return

def setup(bot):
    bot.add_cog(monarchen(bot))
    bot.add_cog(personen(bot))