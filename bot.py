# bot.py
import os

import discord

TOKEN = 'OTc1ODIyNjQ3Mzg2NTg3MTY2.GecGQQ.EKhnHTPE6TIyy2OlLLRltzeeEcVt6QYUuwcKiU'
#GUILD = 'Test Server'

client = discord.Client()

@client.event
async def on_ready():
    @client.event
    async def on_ready():
        print(f'{client.user.name} has connected to Discord!')

    @client.event
    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to my Discord server!'
        )

client.run(TOKEN)
