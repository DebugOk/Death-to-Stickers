import discord
client = discord.Client()
blacklist = []

@client.event
async def on_ready():
    print(f'We have logged in as {client.user} with a ping of {client.latency}ms\n\nVersion: {discord.__version__}, Info: {discord.version_info}')
    await client.change_presence(status=discord.Status.invisible)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if len(message.stickers) != 0 and message.channel.id in blacklist:
        await message.delete()

client.run('')