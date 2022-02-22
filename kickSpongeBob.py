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

# SUPER IMPORTANTE ----> ANTES DE HACER UN COMMIT / PUSH, PONER UN ESPACIO EN BLANCO (" ") DENTRO DEL TOKEN PARA QUE DISCORD NO LO DETECTE EN GITHUB Y CAMBIE LA CLAVE AUTOMATICAMENTE. NO COMPARTIR LA CLAVE CON NADIE!

token = 'OTAyNzA2OTQ5MDM1MDEyMTE4' '.YXiVXA.0-uVBR-9AkSihWI33Of5VKuY9MM'
bot.run(token)