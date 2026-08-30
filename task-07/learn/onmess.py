# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello!, {message.author}')
        await message.channel.send(f'you sent this in {message.channel}')



client.run('MTU0MTM1MjI3MTY0MjYyNDExMQ.GssqqL.HwUaaxlrMgoe1aD9w6aDWDCl8b6XlzSFMnToXQ')  