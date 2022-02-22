import discord
from discord.ui import Button, View
from discord.ext import commands

bot = commands.Bot(command_prefix="-")

@bot.command()
async def buttons(ctx):
    button1 = Button(style=discord.ButtonStyle.green, emoji="🐍")
    button2 = Button(style=discord.ButtonStyle.red, emoji="🥺")
    button3 = Button(style=discord.ButtonStyle.danger, emoji="<:acTrolly:901213127478247535>")
    button4 = Button(style=discord.ButtonStyle.primary, emoji="<:nigger:914609767052378132>")
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    await ctx.send("asd", view=view)

token = "OTAyNzA2OTQ5MDM1MDEyMTE4.YXiVXA.y6rb5FBWdqtVg_LIh3rl1c6pVFU"
bot.run(token)