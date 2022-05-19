# bot.py
import urllib.request

import discord
import random
import urllib3
import requests
from bs4 import BeautifulSoup

TOKEN = 'OTc1ODIyNjQ3Mzg2NTg3MTY2.GecGQQ.EKhnHTPE6TIyy2OlLLRltzeeEcVt6QYUuwcKiU'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    url = 'https://animechan.vercel.app/api/random'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.get_text().split(':')
    final = result[3].split('}')
    print(final[0])

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
