import os
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command(name='spam', help='Spams the input message for x number of times')
async def spam(ctx, amount:int, *, message):
    for i in range(amount): # Do the next thing amount times
        await ctx.send(message) # Sends message where command was called

keep_alive()
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
