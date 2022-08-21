import discord, json
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle

with open('./config/config.json', 'r') as sy:
    system = json.load(sy)

client = commands.Bot(command_prefix = system['prefix'], intents = discord.Intents.all())
DiscordComponents(client)

@client.event
async def on_ready():
    print(f'Bot Name: {client.user} / Bot Id: {client.user.id}')
    print(f'Bot participating servers: {client.guilds}')
    print('Bot Online / Dev. BestHentai0 / https://github.com/BestHentai0')

@client.command(name = 'button')
async def button_system(ctx):
    await ctx.send(embed = discord.Embed(title = 'Button system', description = 'This is the code that creates only the button.\n An error may appear without additional syntax.', color = 0x00ff00), 
        components = [[Button(label = 'Green Button', style = ButtonStyle.green),
        Button(label = 'Github Link',url='https://github.com/BestHentai0', style = ButtonStyle.URL)
        ]])

client.run(system['token'])