import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='&')

@bot.event
async def on_message(msg):
    if "858060188119597087/858060748256575488" in msg.content:
        await kick(msg, msg.author)

@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.message.add_reaction("reaction")

token = 'OTAyNzA2OTQ5MDM1MDEyMTE4' + '.YXiVXA.y6rb5FBWdqtVg_LIh3rl1c6pVFU'
bot.run(token)