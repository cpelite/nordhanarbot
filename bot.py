## imports

import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# loading token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# intents festlegen
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

#load extensions
bot.load_extension("personennordhanar")
bot.load_extension("commonfacts")

#welcome message
@bot.event
async def on_ready():
    print('Bot wurde als {0.user} eingeloggt.')
    print("Bot aktiv. Warte auf Befehle.")

@bot.event
async def botinfo(ctx):
    embed = discord.Embed(title="Botinfo")
    embed.add_field(name="Entwickler", value="SvH")
    embed.add_field(name="Botversion", value="Beta 2 - Operation Stahlrim.")
    embed.add_field(name="Verwendete Programmiersprache", value="Python 3.9")
    await ctx.send(embed=embed)

# nicht existierender befehl.
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Sorry!")
        embed.add_field(name="Es tut mir leid..", value = "...aber dieser Befehl existiert leider noch nicht.")
        await ctx.send(embed=embed)



bot.run(TOKEN)