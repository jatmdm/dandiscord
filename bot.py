import io
import discord
import asyncio
import bot_token

from commandParser import *
from fearcommands import *


print("Running Discord Version ", discord.__version__)

client = discord.Client()

 token = open("TOKEN.token", 'r')

 token = token.readlines()




@client.event
async def on_message(message):
    if message.content.startswith('announce'):
        msg = message.content.replace('announce', '')
        temp = await client.send_message( discord.Object(id=416382795158650881), msg )
    elif message.content.startswith('!'):
        command = message.content
        print(message.author, 'used', command)
        command = command.split()

        if len(command) < 2:
            out = FearCommands.commands[command[0]]()
        else:
            out = FearCommands.commands[command[0]](command[1:])
        print(out)
        if out is not None:
            temp = await client.send_message(message.channel, out)

@client.event
async def on_ready():
    temp = await client.change_presence(game=discord.Game(name='!help'))
    print('Logged in as ')
    print(client.user.name)
    print(client.user.id)
    print('#############')
    

client.run(bot_token.getToken())