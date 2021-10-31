import disnake
from disnake import reaction
from disnake.ext import commands

# SUPER IMPORTANTE ----> ANTES DE HACER UN COMMIT / PUSH, PONER UN ESPACIO EN BLANCO (" ") DENTRO DEL TOKEN PARA QUE DISCORD NO LO DETECTE EN GITHUB Y CAMBIE LA CLAVE AUTOMATICAMENTE. NO COMPARTIR LA CLAVE CON NADIE!
token = "OTAyNzA2OTQ5MDM       1MDEyMTE4.YXiVXA.y6rb5FBWdqtVg_LIh3rl1c6pVFU"
client = commands.Bot(command_prefix='')

@client.event
async def on_ready():
    print("El bot esta listo")
    print(f"Corriendo con disnake version {disnake.__version__}")

@client.event
async def on_message(msg):
    if "test" in msg.content:
        await msg.add_reaction("<:nomanquienesesahijaderemilputaxd:842438178236661831>")    
    
    await client.process_commands(msg)

@client.command(description = "primer comando")
async def ping(ctx):
    await ctx.send(f"pong :ping_pong: `{round(client.latency*1000)}ms`")

@client.command(description = "segundo comando")
async def nig(ctx):
    await ctx.send("ger")

@client.command(description = "cuarto comando")
async def sexo(ctx):
    await ctx.send("sexo <:nomanquienesesahijaderemilputaxd:842438178236661831>")


    
client.run(token)