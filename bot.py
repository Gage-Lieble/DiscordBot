import discord
import random
import requests


TOKEN = 'HIDDEN'


client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    guild = client.get_guild(1022317834677784678)
    channel = guild.get_channel(1022317834677784681)
    await channel.send(f'Welcome {member.mention}! Type "!commands" to see avaliable the functions. ')
    

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_msg = str(message.content)
    channel = str(message.guild.name)
    print(f'{username}: {user_msg} - ({channel})')

    if message.author == client.user:
        return
    
    if channel == 'Laborone-Bot-server':
        um = user_msg.lower()
        if um == '!commands':
            await message.channel.send(f'Hello {username}, \nThe commands are: \n-MISC \n1. hello \n2. bye \n3. dad joke \n-EMOJIS \n1. lmao \n2. rage \n3. gasp')
            return
        elif um == 'hello':
            await message.channel.send(f'Hey {username}!')
            return
        elif um == 'bye':
            await message.channel.send(f'See ya {username}!')
            return
        elif um == 'dad joke':
            response = requests.get( f"https://icanhazdadjoke.com/", headers={ # Gathers API
                'Accept': 'application/json'
            })
            
            search_result = response.json()['joke']
            await message.channel.send(f'{search_result}')
            return
        elif um == 'lmao':
            await message.channel.send(f'https://media.giphy.com/media/XJVn8fwq27Jl7kwbqP/giphy.gif')
            return
        elif um == 'rage':
            await message.channel.send(f'https://media.giphy.com/media/WoF3yfYupTt8mHc7va/giphy.gif')
            return
        elif um == 'gasp':
            await message.channel.send(f'https://media.giphy.com/media/QE8hREXIgRXeo/giphy.gif')
            return
client.run(TOKEN)
