import discord
from discord.ext import commands
from gtts import gTTS
import os
from discord import File

TOKEN = 'YOUR TOKEN HERE'
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='!help'))
    print('bot ready')
    









@client.command()
async def tts(ctx, *, message: str):
    '''Makes a mp3 file of your message, usage: !tts message'''
    mytext = message
    language = "en"
    title = "tts"
    myobj = gTTS(text= mytext, lang=language, slow=False)
    myobj.save("tts.mp3")
    await ctx.send("Here's your tts mp3:")
    await ctx.send(file=discord.File('tts.mp3'))
    




client.run(TOKEN)
