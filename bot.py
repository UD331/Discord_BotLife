# bot.py
import os

import discord
import random

TOKEN = 'OTc1ODIyNjQ3Mzg2NTg3MTY2.GecGQQ.EKhnHTPE6TIyy2OlLLRltzeeEcVt6QYUuwcKiU'
#GUILD = 'Test Server'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if user_message.lower() == 'hello':
        await message.channel.send(f'Hello {username}!')
        return
    elif user_message.lower() == 'bye':
        await message.channel.send(f'See you later {username}!')
        return
    elif user_message.lower() == '!random':
        response = f'This is your random number: {random.randrange(1000000)}'
        await message.channel.send(response)
        return
client.run(TOKEN)
