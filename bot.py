import random

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

client = commands.Bot(command_prefix='p_')

queues = {}


@client.event
async def on_ready():
    print("Boiadeiro is ready")


@client.event
async def on_member_join(member):
    print(f"{member} se juntou a um server.")


@client.event
async def on_member_remove(member):
    print(f"{member} saiu de um server.")


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
async def vidente(ctx, *, pergunta):
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
                 'serpente',
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
                 'primeiro',
                 'socorro',
                 'o meu deus',
                 'seu idiota',
                 'pode ter certeza',
                 'aprovado'
                 ]
    await ctx.send(f'Pergunta: {pergunta}\nResposta: {random.choice(respostas)}')


@client.command(name='clear', pass_context=True)
@has_permissions(administrator=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'limpado!')


@clear.error
async def clear_error(error, ctx):
    if isinstance(error, MissingPermissions):
        await ctx.send(f'"desculpe,você não possui permissão"')


@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick()

@kick.error
async def kick_error(error, ctx):
    if isinstance(error, MissingPermissions):
        await ctx.send("você não possui permissão!")


client.run('NzEwNTc4ODE5NDgzODI4MjU0.Xr2gGA.-HIzvU8tuF-EQlkbjYE-wUZP85w')
