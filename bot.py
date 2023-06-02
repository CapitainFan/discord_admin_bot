import discord
import conf  # мой файл в котом хранятся токен и пароли
from discord.ext import commands


TOKEN = conf.TOKEN
PREFIX = '/'
client = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())
client.remove_command('help')

hello_words = ['hello', 'hi', 'привет', 'privet', 'ky', 'ку', 'салам']
goodbye_words = ['bye', 'poka', 'удачи', 'пока']

@client.event
async def on_ready():
    print('BOT connected')

@client.event
async def on_message(message):
    msg = message.content.lower()
    await client.process_commands(message)
    if msg in hello_words:
        await message.channel.send('ну здравствуй, Рома')
        await message.channel.send("Инфу o сервере можно узнать c помощью команды  /help")
    if msg in goodbye_words:
        await message.channel.send('Пока')

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)

@client.command(pass_context=True)
async def hello(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    author = ctx.message.author
    await ctx.send(f" Hello {author.mention}")


#Kick
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await member.kick(reason=reason)
    await ctx.send(f'kick user {member.mention}')

#Ban
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None) :
    await ctx.channel.purge(limit=1)
    await member.ban(reason=reason)
    await ctx.send(f'ban user {member.mention }')

#Unban
@client.command(pass_context=True)
@commands.has_permissions( administrator = True )
async def unban(ctx, *, member):
    await ctx.channel.purge(limit=1)
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned user {user.mention}')

@client.command(pass_context=True)
async def help(ctx):
    emb = discord.Embed(title='навигация по командам')

    emb.add_field(name = '{}clear'.format(PREFIX), value='Отчистка чата')
    emb.add_field(name = '{}kick'.format(PREFIX), value='Удаление участника сервера')
    emb.add_field(name = '{}ban'.format(PREFIX), value='Ограничение доступа к серверу')
    emb.add_field(name = '{}unban'.format(PREFIX), value='Удаления ограничения доступа к серверу ')
    emb.add_field(name = '{}clear'.format(PREFIX), value='Отчистка чата')
    await ctx.send(embed=emb)

# Connect
client.run(TOKEN)
