#!/usr/bin/python
# -*- coding: UTF-8 -*-
# walker

"""A bot to list all members of a server."""
import sys
import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = Bot(command_prefix = ">")

@bot.event
async def on_ready():
    print('bot login>', )
    print('  bot.user.name: ', bot.user.name)
    print('  bot.user.id:   ', bot.user.id)

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandNotFound):
        return
    else:
        print(error)

@bot.command(pass_context=True)
async def list(ctx):
    fname = '{}.csv'.format(ctx.message.guild)
    with open(fname, mode='w') as f:
        f.write('joined_at, @name, name, discriminator\n')
        for m in ctx.message.guild.members:
            #str = '{},{},{},{},{},{}\n'.format(m.joined_at.__format__('%Y-%m-%d'), m, m.display_name, m.name, m.discriminator, m.id)
            str = '{},{},{},{}\n'.format(m.joined_at.__format__('%Y-%m-%d'), m, m.name, m.discriminator)
            f.write(str)
    
    await ctx.message.author.send(content="用户一览表", file=discord.File(fname))
    await ctx.send(content="sent ok!")
    
    #await ctx.send(content="用户一览表", file=discord.File('temp.csv'))
    print("command >list done!")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="users2csv bot", description="csv格式输出服务器的用户一览表", color=0xeee657)
    embed.add_field(name="作者", value="walker#9296")
    # Shows the number of servers the bot is member of.
    embed.add_field(name="服务器", value=f"{len(bot.guilds)}")
    # give users a link to invite thsi bot to their server
    embed.add_field(name="邀请", value="[邀请链接](https://discord.com/api/oauth2/authorize?client_id=750373870745288756&permissions=0&scope=bot)")

    await ctx.send(embed=embed)
    
    
bot.remove_command('help')
 
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="users2csv bot", description="export user list.", color=0xeee657)
    embed.add_field(name=">list", value="export user list", inline=False)
    embed.add_field(name=">info", value="about this bot", inline=False)
    embed.add_field(name=">help", value="bot help", inline=False)
 
    await ctx.send(embed=embed)


if __name__ == '__main__':
    # python userlistbot.py [bot's TOKEN]
    #   sys.argv[0] - userlistbot.py
    #   sys.argv[1] - [bot's TOKEN]
    if(len(sys.argv) == 2):
        bot.run(sys.argv[1])
    else:
        print("Usage:")
        print("  python userlistbot.py [bot's TOKEN]")
        print("  python userlistbot.py XXXXXXXXODcwNzQ1Mjg4NzU2.X05mIA.6NzSx3ec6azsGAqogaLPiKpLbX8")