# bot.py
import urllib.request
import random
import discord
from bs4 import BeautifulSoup

TOKEN = 'API_KEY'

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
    elif user_message.lower() == '!jojo_stands':
        await message.channel.send("!jojo: Random quotes from various anime.\n"
                                   "!jojo_jojo: 10 random quotes from various anime.\n")
        await message.channel.send("!jojo_(name of title with spaces in between words): " +
                                   "Quotes from that particular anime if it is present in the database.\n"
                                   "!anime_list: List of anime from which quotes are taken.")
    elif user_message.lower() == '!jojo_jojo':
        url = 'https://animechan.vercel.app/api/quotes'
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        result = soup.get_text().split(':')
        for a in result:
            final = a.split('}')
            if ('anime' in final[0]) or ('character' in final[0]) or ('quote' in final[0]):
                print()
            else:
                await message.channel.send(final[0])
    elif '!jojo_' in user_message:
        anime = user_message.split('_')
        name = anime[1].replace(' ', '%20')
        print(name)
        url = 'https://animechan.vercel.app/api/quotes/anime?title=' + name
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        result = soup.get_text().split(':')
        n = random.randrange(1, 10)
        c = 1
        for a in result:
            final = a.split('}')
            if ('anime' in final[0]) or ('character' in final[0]) or ('quote' in final[0]) or not(' ' in a):
                print()
            else:
                if c == n:
                    await message.channel.send(final[0])
                    break
                c += 1
client.run(TOKEN)
