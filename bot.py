import os
import random
import json
import discord

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = 'GODS RELENTLESS ARMY'

client = discord.Client()

#console
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')

#message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    martin_quotes = [
        'det der er faktisk ikke lov å si.',
        'skjerp deg, ingen ableisme på serveren.',
        'INGEN ABLEISME PÅ SERVEREN!',
        'advarsel, ingen ableisme.',
        'det ordet er ikke lov, bruk noe annet.',
        'ikke lov, bruk et annet ord.',
        'vennligst ikke bruk slike ord.',
        'har du tenkt på undertrykkelsen det ordet medfører?',
        'det er en null-toleranse for hatprat på denne serveren.',
        'du klarer bedre.',
        'seriøst? Bruk ord som ikke er undertrykkende for minoriteter i samfunnet.',
        'det finnes ingen unnskyldning for ordet du nettopp brukte',
        'du trenger terapi, det der blir for dumt.',
        'skjerp deg! Til og med Vemund ville ikke brukt det ordet.',
        'hvis du ikke bruker andre ord enn det fremover, kommer Ole til å banke deg opp.',
        'ikke vær helt Marcus, vær bedre.',
        'Martin kommer til å eksplodere, vennligst bruk et annet ord.',
        'Håkon godkjenner, men det gjør ikke jeg. Finn på noe annet.',
        'neste gang du bruker slike ord kommer du til å føle på William sin vrede.',
    ]

    keywords = [
        'retard',
        'retarded',
        'cripple',
        'krøpling',
        'handicap',
        'handikap',
        'downs',
    ]

    if any(keyword in message.content.lower() for keyword in keywords):
        response = (message.author.mention + ', ' + random.choice(martin_quotes))
        await message.channel.send(response)

client.run(TOKEN)