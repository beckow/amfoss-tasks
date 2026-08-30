import discord
from discord.ext import commands
import random
from economy import add_user, get_balance, update_balance, set_last_daily,get_last_daily, set_last_rob,get_last_rob, get_top_users
import time
import aiohttp
#roasts
roasts = [
    "You're the human version of a typo.",
    "I've seen loading screens with more personality.",
    "You're proof that confidence doesn't require competence.",
    "Your Wi-Fi signal has more direction than you do.",
    "You're not useless, you can always be used as a bad example."
]
#rock paper scissors
bot_choices = ['stone', 'paper', 'scissors']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix ='!', intents = intents)

@bot.command()
async def support(ctx):
    await ctx.send("""```
╔══════════════════════════════════════════════════════╗
║                    BERRY BROKER                      ║
╠══════════════════╦═══════════════════════════════════╣
║ !bounty          ║ Check your Berry balance          ║
║ !setsail         ║ Claim your daily Berries          ║
║ !trade @user amt ║ Transfer Berries to another user  ║
║ !logpose         ║ Get random One Piece intel        ║
║ !roast @user     ║ Roast another pirate              ║
║ !duel <choice>   ║ Duel the bot for Berries          ║
║ !worstgeneration ║ View the top 5 richest pirates    ║
║ !raid @user      ║ Attempt to raid another pirate    ║
╚══════════════════╩═══════════════════════════════════╝
```""")

@bot.command()
async def bounty(ctx):
    add_user(ctx.author.id, ctx.author.name)
    balance = get_balance(ctx.author.id)
    await ctx.send(f"Your current Berry balance is {balance}")


@bot.command()
async def setsail(ctx):
    #update balance
    last_daily = get_last_daily(ctx.author.id)
    now = int(time.time())

    if now - last_daily < 43200:
        await ctx.send("You have already claimed your daily in the past 12 hours.")
        return
    
    update_balance(ctx.author.id, 500)
    set_last_daily(ctx.author.id, now)
    await ctx.send(f"You claimed your daily of 500")


@bot.command()
async def trade(ctx,user: discord.Member,amt :int):
    add_user(ctx.author.id, ctx.author.name)
    add_user(user.id, user.name)
    if amt <=0:
        await ctx.send("Amount must be greater than 0.")
        return
    if get_balance(ctx.author.id) < amt:
        await ctx.send("You don't have enough berries")
        return

    update_balance(ctx.author.id, -amt)
    update_balance(user.id, amt)
    await ctx.send(f"You transferred {amt} to {user.mention}")


@bot.command()
async def logpose(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.api-onepiece.com/v2/fruits/en') as response:
            data = await response.json()

    fruit = random.choice(data)
    await ctx.send(fruit)

    

@bot.command()
async def roast(ctx, user: discord.Member):
    randrost = random.choice(roasts)
    await ctx.send(f"{user.mention} {randrost}")


@bot.command()
async def duel(ctx, choice):
    choice = choice.lower()
    if get_balance(ctx.author.id) < 100:
        await ctx.send("You need 100 Berries to duel.")
        return
    
    compchoics = random.choice(bot_choices)
    if choice not in bot_choices:
            await ctx.send("Input a valid input")
    
    elif (choice == 'stone' and compchoics == 'paper') or (choice == 'paper' and compchoics == 'scissors') or (choice == 'scissors' and compchoics == 'stone'):
        update_balance(ctx.author.id, -100)
        await ctx.send(f"I chose {compchoics}, You lose")

    elif (choice == compchoics):
        await ctx.send(f"I chose {compchoics}, Its a draw, lets go again")
    else:
        update_balance(ctx.author.id, +100)
        await ctx.send(f"I chose {compchoics}, you win")
@bot.command()
async def worstgeneration(ctx):

    top_users = get_top_users()

    message = "**Worst Generation**\n"

    for i, (username, balance) in enumerate(top_users, start=1):
        message += f"{i}. {username} — {balance} Berries\n"

    await ctx.send(message)

@bot.command()
async def raid(ctx, user: discord.Member):
    chance = random.randint(1,10)
    last_rob = get_last_rob(ctx.author.id)
    now = int(time.time())
    if get_balance(ctx.author.id) < 600:
        await ctx.send("You need at least 600 Berries to raid.")
        return
    if user.id == ctx.author.id:
        await ctx.send("You can't raid yourself!")
        return
    
    if(now - last_rob >= 43200):
        if chance == 10:
            add_user(ctx.author.id, ctx.author.name)
            add_user(user.id, user.name)
            amt = 500
            if get_balance(user.id) < 500:
                amt = get_balance(user.id)
            
            update_balance(ctx.author.id, +amt)
            update_balance(user.id, -amt)
            await ctx.send(f"You raided {amt} from {user.mention}")
        else:
            await ctx.send("Raid failed miserably you lose 600 berries")
            update_balance(ctx.author.id, -600)
        set_last_rob(ctx.author.id, now)
    else:
        await ctx.send("You have already raided in the past 12hrs")


bot.run('MTU0MTM1MjI3MTY0MjYyNDExMQ.GssqqL.HwUaaxlrMgoe1aD9w6aDWDCl8b6XlzSFMnToXQ')
