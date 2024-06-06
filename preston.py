import discord
import random
import asyncio

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await check_server()

async def check_server():
    server_id = 123456 ###################### YOUR SERVER ID
    server = client.get_guild(server_id)
    if server is None:
        print('Bot is not in the specified server.')
    else:
        print('Bot is in the specified server.')
        client.loop.create_task(main())

async def ping_user():
    channel = client.get_channel(123456)  ###################### YOUR CHANNEL ID
    server = client.get_guild(123456) ###################### YOUR SERVER ID
    members = server.members
    random_member = random.choice(members)
    await channel.send('https://media.tenor.com/hq0mGv1odF4AAAAC/fallout4.gif')
    message = f'Hey {random_member.mention}, another settlment needs your help!'
    await channel.send(message)
    await channel.send('Here, I\'ll mark it on your map.')

async def main():
    while True:
        server_id = 123456  ###################### YOUR SERVER ID
        server = client.get_guild(server_id)
        if server is not None:
            await ping_user()
        await asyncio.sleep(random.randint(3600, 86000)) ########## TIME IN SECONDS, MIN - MAX

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        phrases = ['Take care of yourself.', 'What?', 'Man, what are you waiting for? ', 'What can I do for you?']
        response = random.choice(phrases)
        await message.reply(response)

client.run('TOKEN')  ###################### YOUR BOT TOKEN
