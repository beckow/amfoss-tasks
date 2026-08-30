import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix ='!', intents = intents)

@bot.command()
async def test(ctx, *argi):
    argus = ' '.join(argi)
    await ctx.send(f"nigga balls {argus}")

bot.run('MTU0MTM1MjI3MTY0MjYyNDExMQ.GssqqL.HwUaaxlrMgoe1aD9w6aDWDCl8b6XlzSFMnToXQ')