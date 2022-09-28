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
            5. !pic
            6. !kanye

            -EMOJIS-GIFS 
            1. !lmao 
            2. !rage 
            3. !gasp
            4. !cry
            5. !cringe
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

        elif um == '!eth':
    
            response = requests.get( f"https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd", headers={
                'Accept': 'application/json'
            })
            output = response.json()['ethereum']['usd']
            currency = "${:,.2f}".format(output)
            await message.channel.send(f'Ethereum is priced at {currency}')
            return

        elif um == '!whatisthebestwebsiteever':
            await message.channel.send(f'WOAH {username}! you found a hidden command 🎉. The best website ever is https://www.gagelieble.com/')
            await message.channel.send(f'https://www.gagelieble.com/static/portfolio/imgs/gagehead.png')
            return

        elif um == '!pic':
            await message.channel.send(f'https://picsum.photos/id/{random.randint(0,999)}/200/200')
            return

        elif um == '!ye' or um == '!kanye':
            response = requests.get( f"https://api.kanye.rest", headers={
                'Accept': 'application/json'
            })
            
            search_result = response.json()['quote']
            await message.channel.send(f'{search_result} - Ye West')
            return

        elif um == '!theft':
            response = requests.get( f"https://uinames.com/api/", headers={
                'Accept': 'application/json'
            })
            
            search_result = response.json()
            await message.channel.send(f'{search_result}')
            return
         
        

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
        elif um == '!cry':
            await message.channel.send(f'{username} reacted: (cry)')
            await message.channel.send(f'https://media.giphy.com/media/KDRv3QggAjyo/giphy.gif')
            return
        elif um == '!cringe':
            await message.channel.send(f'{username} reacted: (cringe)')
            await message.channel.send(f'https://media.giphy.com/media/3otPoPoCbPjSP4ktGw/giphy.gif')
            return
client.run(TOKEN)