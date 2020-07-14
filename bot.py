import discord
import youtube_dl
import os
from discord.utils import get
import random
from discord.ext import commands

client = commands.Bot(command_prefix= 'p_')

players = {}

@client.event
async def on_ready():
    print("Boiadeiro is ready")

@client.event
async def on_member_join(member):
        print(f"{member} se juntou a baderna.")

@client.event
async def on_member_remove(member):
    print(f"{member} saiu da baderna.")

@client.command()
async def lexo(ctx):
    await ctx.send('you lexo!')

@client.command()
async def eae(ctx):
    await ctx.send("eae bro")

#async def play(ctx):
    #channel = ctx.message.author.voice.channel
    #await channel.connect()
    #guild = ctx.message.guild
    #voice_client = guild.voice_client
    #player = await voice_client.create_ytdl_player(url)
    #players[guild.id] = player
    #player.start()

@client.command()
async def stop(ctx):
    guild = ctx.message.guild
    voice_client = ctx.guild.voice_client
    await voice_client.disconnect()
@client.command()
async def mongoloide(ctx):
    await ctx.send(" foi banido para sempre da twitch!")

@client.command()
async def fraserandom(ctx):
    inicio = ['você',
              'eu',
              'tu',
              'nós',
              'vós',
              ]
    meio = ['subir',
            'fugir',
            'matar',
            'correr',
            'lutar',
            'destruir',
            'pegar',
            'despegar',
            'arruinar',
            'latir',
            'ir contra',
            'ir a favor de',
            'derrotar',
            'ser derrotado',
            'roubar',
            'drogar',
            'assaultar',
            'latifundiar',
            'endorzar',
            'punir',
            'botificar',
            'comeste',
            'foges e',
            'consegues',
            'falhas',
            'fracassas',
            'sucedes',
            'espera por',
            'fica para trás por'
            ]
    fim = ['lemme smash',
           'dogoso',
           'Fenekito',
           'python',
           'no step on snek!',
           'mermão',
           'shadow',
           'davi',
           'enzo',
           'seu bugado',
           'lokão',
           'morre porque é lexo',
           'supera o bolsa familia',
           'derrota o PT',
           'escapa do Brasil',
           'põe um fim a escravidão',
           'vira um wacky wocker'
           ]
    await ctx.send(f'{random.choice(inicio)} {random.choice(meio)} {random.choice(fim)}')

@client.command()
async def vidente(ctx,*,pergunta):
    respostas = ['certamente que sim.',
                 'provavelmente sim',
                 'talvez',
                 'pode ter certeza',
                 'nice',
                 'gay',
                 'hetero',
                 'porque você quer que um bot autoconsciente responda isso?',
                 'suas definições de vírus foram atualizadas',
                 'oh no',
                 'lá no posto ipiranga',
                 'pede pro trunhan',
                 'claro',
                 'de jeito nenhum',
                 '100%',
                 '0%',
                 'cuidado',
                 'vou te quebrar por isso',
                 'yup',
                 'sorvete',
                 'arco-iris gay',
                 'chovendo',
                 'nem que tu morra',
                 'bolado msm',
                 'usando drogas',
                 'reportando o kayo',
                 'te reportando',
                 'erro 404 erro não localizado',
                 'usando coisas ilicitas',
                 'passando no enem',
                 'sua bunda',
                 'minha bunda',
                 'serpernte',
                 'a bunda do fene',
                 'trabalho escravo',
                 'superando a fome',
                 'ultrapassando limites',
                 'ligando',
                 'desligando',
                 'pode pá',
                 'corre mano',
                 'criminoso',
                 'lambida',
                 'cortando o cabelo',
                 'Y E S',
                 'Pau Genial',
                 'Periquito Boiadeiro',
                 'Calopsita Vaqueira',
                 'lemme smash',
                 'armado',
                 'pacifico',
                 'amor',
                 'sabedoria',
                 'petroleo',
                 'wiu wiu',
                 'sei la',
                 'puts',
                 'nazista',
                 'primeiro',
                 'socorro',
                 'o meu deus',
                 'seu idiota'
                 ]
    await ctx.send(f'Pergunta: {pergunta}\nResposta: {random.choice(respostas)}')

@client.command()
async def clear(ctx,amount = 5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("limpado")

@client.command(pass_context=True)

async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.send(f"entrou em {channel}")

client.run('BOT-KEY')

@client.command()
@commands.command(name = 'kick')
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
