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
async def lists(ctx):
    isAdmin = ctx.message.channel.permissions_for(ctx.message.author).administrator
    if not isAdmin:
        permission_error = str('Sorry ' + ctx.message.author + ' you do not have permissions to do that!')
        await ctx.send(content=permission_error)
        return

    fname = 'server.csv'
    with open(fname, mode='w') as f:
        f.write('joined_at, @name, name, discriminator\n')
        for m in ctx.message.guild.members:
            str = '{},{},{},{}\n'.format(m.joined_at.__format__('%Y-%m-%d'), m, m.name, m.discriminator)
            f.write(str)
    
    await ctx.message.author.send(content="服务器-用户一览表", file=discord.File(fname))
    await ctx.send(content="sent file ok!")
    print("command >lists done!")

@bot.command(pass_context=True)
async def listc(ctx):
    """isAdmin = ctx.message.channel.permissions_for(ctx.message.author).administrator
    if not isAdmin:
        permission_error = str('Sorry ' + ctx.message.author + ' you do not have permissions to do that!')
        await ctx.send(content=permission_error)
        return"""
        
    fname = 'channel.csv'
    with open(fname, mode='w') as f:
        f.write('joined_at, @name, name, discriminator\n')
        for m in ctx.message.channel.members:
            str = '{},{},{},{}\n'.format(m.joined_at.__format__('%Y-%m-%d'), m, m.name, m.discriminator)
            f.write(str)
    
    await ctx.message.author.send(content="频道-用户一览表", file=discord.File(fname))
    await ctx.send(content="sent file ok!") 
    print("command >listc done!")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="users2csv bot", description="以csv格式输出服务器/频道用户的一览表", color=0xeee657)
    embed.add_field(name="作者", value="walker#9296")
    # Shows the number of servers the bot is member of.
    embed.add_field(name="服务器", value=f"{len(bot.guilds)}")
    # give users a link to invite this bot to their server
    embed.add_field(name="邀请", value="[邀请链接](https://discord.com/api/oauth2/authorize?client_id=750373870745288756&permissions=0&scope=bot)")

    await ctx.send(embed=embed)
    
    
bot.remove_command('help')
 
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="users2csv bot", description="export user list.", color=0xeee657)
    embed.add_field(name=">lists", value="export currnet server user list", inline=False)
    embed.add_field(name=">listc", value="export currnet channel user list", inline=False)
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