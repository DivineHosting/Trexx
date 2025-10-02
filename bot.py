import discord
from discord.ext import commands
import os
import main
import gen

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def check(ctx):
    result = main.run_checker()
    await ctx.send(result)

@bot.command()
async def gen(ctx):
    account = gen.generate_account()
    await ctx.send(f"Generated account: {account}")

bot.run(os.getenv("DISCORD_TOKEN"))
