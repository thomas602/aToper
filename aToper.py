import disnake
from disnake import reaction
from disnake.ext import commands

# SUPER IMPORTANTE ----> ANTES DE HACER UN COMMIT / PUSH, PONER UN ESPACIO EN BLANCO (" ") DENTRO DEL TOKEN PARA QUE DISCORD NO LO DETECTE EN GITHUB Y CAMBIE LA CLAVE AUTOMATICAMENTE. NO COMPARTIR LA CLAVE CON NADIE!
token = "OTAyNzA2OTQ5MDM1       MDEyMTE4.YXiVXA.y6rb5FBWdqtVg_LIh3rl1c6pVFU"
client = commands.Bot(command_prefix='')

@client.event
async def on_ready():
    print("El bot esta listo")
    print(f"Corriendo con disnake version {disnake.__version__}")

@client.event
async def on_message(msg):
    if "test" in msg.content:
        await msg.add_reaction("<:Gayge:896509343158136862>")    
    if "master" in msg.content:
        await msg.add_reaction("<:COPIUM:819330184774680587>")
    if msg.author.id == 199336424091156481:
        await msg.add_reaction("<:Pepepains:914611218403188779>")

    await client.process_commands(msg)


@client.command(description = "primer comando")
async def ping(ctx):
    await ctx.send(f"pong :ping_pong: `{round(client.latency*1000)}ms`")

@client.command(description = "segundo comando")
async def nig(ctx):
    await ctx.send("ger")

@client.command(description = "cuarto comando")
async def sexo(ctx):
    await ctx.send("sexo <:second30Nice:914609948531511326>")


    
client.run(token)