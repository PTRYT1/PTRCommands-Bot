import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game

name = 'PTRBot'
link = "Invite Link: https://discordapp.com/oauth2/authorize?&client_id=566704244074348566&scope=bot&permissions=8"
Client = discord.client
client = commands.Bot(command_prefix = '!!')
Clientdiscord = discord.Client()

@client.event
async def on_member_join(member):
    await client.send_message(member, 'Welcome To The Server, Enjoy Your Time Here!')
    print('Sent message to ' + member.name)
    
@client.event
async def on_message(message):
    if message.content == '!founder':
        await client.send_message(message.channel,'The Founder orignal is pineapple#1234 on discord, modified by ★NotFunctional★#7659!')
    if message.content == '!help':
        await client.send_message(message.channel,'Commands: !!founder, !!help, !!v')


@client.event
async def on_member_join(member):
           print('Member' + member.name + ' joined')
           await client.send_message(member, 'Welcome To Pineapples Server, Enjoy Your Time Here! :wave:   (:clap: meme review :clap:')
           print('Sent message to ' + member.name) 



@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Pineapple: The Movie', type = 3))
    print(name+' is online.')
    print(" ")
    print("Bot Running...")
    print(" ")
    print(link)
    print(" ")
    print("Player Messeges")
    print("---------------------")
    print(" ")
client.run('NTY3MTEzNjc2MjAxNjU2MzQx.XLOz7w.jqH23SI_l4CFdolXihSQpGJPR9g')
