import discord
import os
import dotenv
import searchWikipedia

from discord.ext import commands
from discord import message
from dotenv import load_dotenv
load_dotenv()

wikipedia_web = searchWikipedia.searchClass

client = commands.Bot(command_prefix= '>')


no_result_message = 'No results found, please correct any grammatical errors and try again.'


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    message_content = message.content.lower() #sets user input to lowercase for evaluations during the search function
    
    if message.content.startswith(f'>hello'):
        await message.channel.send('Sheesh, go use >help or something to see some ACTUAL commands.')
    
    if f'>help' in message_content:
        new_line = '\n'
        await message.channel.send(f'{new_line}Welcome to Promethian Bot!{new_line}{new_line} To search an article, try typing ">search " followed by the item you would like to recieve a Wikipedia article from!')
    
    if f'>search' in message_content:
        key_words, search_words = searchWikipedia.searchClass.key_words_search_words(message_content)
        result_links = searchWikipedia.search(key_words)
        links = searchWikipedia.send_link(result_links, search_words)
        
        if len(links) > 0:
            for link in links:
                await message.channel.send(link)
        else:
            await message.channel.send(no_result_message)


@commands.command()
async def hello(ctx):
    await ctx.send('Hello {0.display_name}.'.format(ctx.author))

def setup(bot):
    bot.add_command(hello)

client.run(os.getenv('TOKEN'))