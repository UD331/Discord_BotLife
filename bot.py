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


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    url_x = 'https://animechan.vercel.app/api/available/anime'
    html = urllib.request.urlopen(url_x).read()
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.get_text().split(',')

    if message.author == client.user:
        return

    if user_message.lower() == '!jojo':
        url = 'https://animechan.vercel.app/api/random'
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        result = soup.get_text().split(':')
        final = result[3].split('}')
        await message.channel.send(final[0])
        return
    elif user_message.lower() == '!anime_list':
        for a in result:
            if "[" in a:
                b = a.split('[')
                await message.channel.send(b[1])
            elif "]" in a:
                b = a.split(']')
                await message.channel.send(b[0])
            else:
                await message.channel.send(a)
        return
    elif user_message == '!jojo_stands':
        await message.channel.send("!jojo- Random quotes from various anime."
                                   "\n!anime_list- List of anime from which quotes are taken.")

    for a in result:
        if "[" in a:
            b = a.split('[')
            a = b[1]
            if a.lower() in user_message.lower():
                url = 'https://animechan.vercel.app/api/quotes/anime/title?=' + a;
                html = urllib.request.urlopen(url).read()
                soup = BeautifulSoup(html, 'html.parser')
                print(soup[1])
        elif "]" in a:
            b = a.split(']')
            a = b[0]
            if a.lower() in user_message.lower():
                url = 'https://animechan.vercel.app/api/quotes/anime/title?=' + a;
                html = urllib.request.urlopen(url).read()
                soup = BeautifulSoup(html, 'html.parser')
                print(soup[1])
        else:
            if a.lower() in user_message.lower():
                url = 'https://animechan.vercel.app/api/quotes/anime/title?=' + a;
                html = urllib.request.urlopen(url).read()
                soup = BeautifulSoup(html, 'html.parser')
                print(soup[1])

client.run(TOKEN)
