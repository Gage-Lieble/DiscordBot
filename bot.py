import discord
import random
import requests 


TOKEN = ''

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    guild = client.get_guild(1022317834677784678)
    channel = guild.get_channel(1022317834677784681)
    await channel.send(f'Welcome {member.mention}! Type "!help" to see avaliable the functions. ')
    

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
        if um == '!help':
            await message.channel.send(f'''
            Hello {username}, 
            The commands are: 
            -MISC 
            1. !hello
            2. !bye 
            3. !dad joke
            4. !bitcoin

            -EMOJIS-GIFS 
            1. !lmao 
            2. !rage 
            3. !gasp
            ''')
            return

        # MISC
        elif um == '!hello':
            await message.channel.send(f'Hey {username}!')
            return

        elif um == '!bye':
            await message.channel.send(f'See ya {username}!')
            return

        elif um == '!dad joke' or um == '!dadjoke':
            response = requests.get( f"https://icanhazdadjoke.com/", headers={
                'Accept': 'application/json'
            })
            
            search_result = response.json()['joke']
            await message.channel.send(f'{search_result}')
            return

        elif um == '!bitcoin':
    
            response = requests.get( f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd", headers={
                'Accept': 'application/json'
            })
            output = response.json()['bitcoin']['usd']
            currency = "${:,.2f}".format(output)
            await message.channel.send(f'Bitcoin is priced at {currency}')
            return

        elif um == '!whatisthebestwebsiteever':
            await message.channel.send(f'WOAH {username}! you found a hidden command 🎉. The best website ever is https://www.gagelieble.com/')
            await message.channel.send(f'https://www.gagelieble.com/static/portfolio/imgs/gagehead.png')
            return

        # elif '!html' in um:
        #     site = um.split(' ')[1]
        #     print(site)
        #     response = re.get(site)
        #     html = response.text
        #     print(html)
        #     await message.channel.send(f'fds')
        #     return


        # EMOJI GIFS
        elif um == '!lmao':
            await message.channel.send(f'{username} reacted: (lmao)')
            await message.channel.send(f'https://media.giphy.com/media/XJVn8fwq27Jl7kwbqP/giphy.gif')
            return

        elif um == '!rage':
            await message.channel.send(f'{username} reacted: (rage)')
            await message.channel.send(f'https://media.giphy.com/media/WoF3yfYupTt8mHc7va/giphy.gif')
            return

        elif um == '!gasp':
            await message.channel.send(f'{username} reacted: (gasp)')
            await message.channel.send(f'https://media.giphy.com/media/QE8hREXIgRXeo/giphy.gif')
            return

        
client.run(TOKEN)