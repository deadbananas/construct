import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '!bard':
        await client.send_message(message.channel,'https://www.youtube.com/watch?v=aAeU2SrLlQM')
    if message.content == '!dnd':
        await client.send_message(message.channel,'"math"')
client.run('NTE0MjcxNzAzNjY1NDc1NjEz.DtUIqg.0Nch_W4AJuoJj3hOoTDfYGvIPjc')
