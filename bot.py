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
        'Det der er faktisk ikke lov å si.',
        'Skjerp deg, ingen ableisme på serveren.',
        'INGEN ABLEISME PÅ SERVEREN!',
        'Advarsel, ingen ableisme.',
        'Det ordet er ikke lov, bruk noe annet.',
        'Ikke lov, bruk et annet ord.',
        'Vennligst ikke bruk slike ord.',
        'Har du tenkt på undertrykkelsen det ordet medfører?',
        'Det er en null-toleranse for hatprat på denne serveren.',
        'Du klarer bedre.',
        'Seriøst? Bruk ord som ikke er undertrykkende for minoriteter i samfunnet.',
        'Det finnes ingen unnskyldning for ordet du nettopp brukte',
        'Du trenger terapi, det der blir for dumt.',
        'Skjerp deg! Til og med Vemund ville ikke brukt det ordet.',
        'Hvis du ikke bruker andre ord enn det fremover, kommer Ole til å banke deg opp.',
        'Ikke vær helt Marcus, vær bedre.',
        'Martin kommer til å eksplodere, vennligst bruk et annet ord.',
        'Håkon godkjenner, men det gjør ikke jeg. Finn på noe annet.',
        'Neste gang du bruker slike ord kommer du til å føle på William sin vrede.',
    ]

    keywords = [
        'retard',
        'retarded',
        'cripple',
        'krøpling',
        'handicap',
        'handikap',
        'downs',
        'aids',
    ]

    if any(keyword in message.content.lower() for keyword in keywords):
        response = (message.author.mention + ' ' + random.choice(martin_quotes))
        await message.channel.send(response)

client.run(TOKEN)