import disnake
from disnake.ext import commands


token = "OTAyNzA2OTQ5MDM1MDEyMTE4.YXiVXA.SU4x6lT82EKsyaSt-ZRN2M3XqYg"
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("El bot esta listo")
    print(f"Corriendo con disnake version {disnake.__version__}")

@client.command(description = "primer comando")
async def ping(ctx):
    await ctx.send(f"pong :ping_pong: `{round(client.latency*1000)}ms`")

client.run(token)