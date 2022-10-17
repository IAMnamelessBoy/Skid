import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandNotFound
import asyncio
import os
import requests
import json

intents=discord.Intents.all()


client = commands.Bot(command_prefix = '.',intents=intents)
client.remove_command('help')
client.owner_ids = [981497848711479316, 937605085788250152]


#os.system("pip install PyNaCl")
#os.system("clear")

tkn = "MTAzMTA1MjU3MzQ4Mzk5OTMzMg.G4I3Vf.qarXo61X3sbPbf9_BnF1ahOLZjUy2EwwCTQKgo"
tick = "<a:RRQredtick:1030149339823214693>"
annc = ":joy:"
rep = "<:reply:1030346679758630912>"
dash = "<:emoji_10:1030346902367125564>"
cross = "<a:spy_cross:1030888026429194391>"
dot = "<a:blackdot:1030890151515267132>"
inf = "<a:lgn_infinity:1030890199250636912>"
success = "<a:success:1030356353581076491>"
officialrole = 1026367694074826822
tagxd = "VLƬ"
import time
                  
#---help---#

@client.command(name='cmds')
async def cmds(ctx):
  cmds = discord.Embed(title=f' {cross} /vltop',description=f'''{cross} Commands: 

**prefix is .**

{inf}**ban**
{inf}**Membercount**
{inf}**ping**
{inf}**unbanall**
{inf}**giverole**
{inf}**removerole**
{inf}**hideall**
{inf}**unhideall**
{inf}**unban**
{inf}**kick**
{inf}**purge**
{inf}**hide**
{inf}**unhide**
{inf}**make_embed**
{inf}**log**
{inf}**mute**
{inf}**unmute**
{inf}**lock**
{inf}**unlock**
{inf}**lockall**
{inf}**unlockall**
{inf}**onc**
''') 


  await ctx.message.reply(embed=cmds)


@client.command(name='help')
async def help(ctx):
  help = discord.Embed(title=f' {cross} /vltop',description=f'''{cross} Help Panel: 

**prefix is .**

<a:blackdot:1030890151515267132> **Cmds** - shows cmds panel of vltop
<a:blackdot:1030890151515267132> **Vanity** - shows vanity
''')

  await ctx.message.reply(embed=help)

@client.command()
async def vanity(ctx):
  await ctx.send("<a:lgn_infinity:1030890199250636912> discor.gg/vltop")

#---embed---complete---#

#restart#
def restart_client(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@client.command()
@commands.is_owner()
async def restart(ctx):
  await ctx.send(f"**{tick} | Successfully Restarted The Bot**")
  restart_client()

#end#
#ping#
@client.command()
async def ping(ctx):
    ed(title=f"Ping!",
        description=
        f"**`{int(client.latency * 1000)}ms`**")
    await ctx.send(embed=embed)
#end#
#hide-&-unhide-#
@client.command()
@commands.has_permissions(administrator=True)
async def hide(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,view_channel=False)
    await ctx.send('<a:success:1030356353581076491> | **This Channel is Now Hidden From Everyone**')

@client.command()
@commands.has_permissions(administrator=True)
async def unhide(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,view_channel=True)
    await ctx.send('<a:success:1030356353581076491> | **This Channel is Now Visible To Everyone**')

@commands.has_guild_permissions(manage_channels=True) 
@client.command()
async def unhideall(ctx):
   await ctx.send(f"**{tick} | UnHiding All Channels Please Wait!**")
   for x in ctx.guild.channels:
      await x.set_permissions(ctx.guild.default_role,view_channel=True)
   await ctx.send(f"**{tick} | Successfully UnHidden All Channels**")

@commands.has_guild_permissions(manage_channels=True)    
@client.command()
async def hideall(ctx):
   await ctx.send(f"**{tick} | Hiding All Channels Please Wait!**")
   for x in ctx.guild.channels:
      await x.set_permissions(ctx.guild.default_role,view_channel=False)
   await ctx.send(f"**{tick} | Successfully Hidden All Channels**")

#end#
#ban-&-unban-&-kick

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason=" no reason provided"
    await ctx.guild.kick(member)
    await ctx.send(f'{tick} | Successfully Kicked {member.mention} Reason: {reason}')
#end

#ban
@client.command(aliases=["fban"])
@commands.has_permissions(ban_members=True)
async def fuckban(ctx, user: discord.Member, *, reason="No reason provided"):
  await user.ban(reason=f"Banned by {ctx.author.name} reason: {reason}.")
  await ctx.send(f"**<a:success:1030356353581076491> | Successfully fuckBanned {user.name}, Responsible:{ctx.author.name}.**", mention_author=False)

@client.command(aliases=["log", "logs", "audit", "audit-logs", "audit-log", "auditlogs"])
async def auditlog(ctx, lmt:int):
  idk = []
  str = ""
  async for entry in ctx.guild.audit_logs(limit=lmt):
    idk.append(f'''{dash} User: `{entry.user}`
{rep} Action: `{entry.action}`
{rep} Target: `{entry.target}`
{rep} Reason: `{entry.reason}`\n\n''')
  for n in idk:
       str += n
  str = str.replace("AuditLogAction.", "")
  embed = discord.Embed(title=f"Audit Actions!", description=f"{str}")
  await ctx.send(embed=embed)

@client.command(name='',

                description='Bans mentioned user.',

                usage="ban <user> [reason]",

                inline=True)

@commands.has_guild_permissions(administrator=True)

@commands.cooldown(1, 5, commands.BucketType.channel)

async def ban(ctx, member: discord.Member, *, reason=None):
    
    await ctx.message.delete()

    guild = ctx.guild

    if ctx.author == member:

        await ctx.send(

            (f'{ctx.author.mention}, Do you really want me to ban you?'),

            delete_after=20)

    elif ctx.author.top_role <= member.top_role:

        await ctx.send((f"**<a:error:1030396429761531904> | You can't ban a member above you.**"),

                       delete_after=20)

    elif ctx.author.top_role == member.top_role:

        await ctx.send((f"**<a:error:1030396429761531904> | You can't ban member having same role as you**"))

    elif ctx.guild.owner == member:

        await ctx.send(('<a:error:1030396429761531904> | Server owners can\'t be banned!!'),

                       delete_after=20)

    else:

        if reason == None:

            try:

                try:

                    #   await member.send(embed=create_embed(f"**You have been banned from, {guild.name}**"))

                    await member.ban(reason=f"Responsible: {ctx.author}")

                    banembed = discord.Embed(

                        description=f'**<a:success:1030356353581076491> | {member} Has Been Banned**')

                    banembed.set_footer(text=f"Responsible: {ctx.author}")

                    await ctx.send(embed=banembed)

                except:

                    await member.ban(reason=f"Responsible: {ctx.author}")

                    ban2embed = discord.Embed(

                        description=f'<a:success:1030356353581076491> | {member} Has Been Banned**')

                    ban2embed.set_footer(text=f"Responsible: {ctx.author}")

                    await ctx.send(embed=ban2embed)

            except Exception as e:

                await ctx.send(f"**<a:success:1030356353581076491> | {member} Has Been Banned**")

        else:

            try:

                try:

                    #    await member.send(embed=create_embed(f"**You have been banned from {guild.name} for *{reason}***"))

                    await member.ban(reason=reason)

                    ban3embed = discord.Embed(

                        description=

                        f'**<a:success:1030356353581076491> | {member} Has Been Banned**\nReason: `{reason}`')

                    ban3embed.set_footer(text=f"Responsible: {ctx.author}")

                    await ctx.send(embed=ban3embed)

                except:

                    await member.ban(reason=reason)

                    ban4embed = discord.Embed(

                        description=

                        f'**<a:success:1030356353581076491> | {member} Has Been Banned**\nReason: `{reason}`')

                    ban4embed.set_footer(text=f"Responsible: {ctx.author}")

                    await ctx.send(embed=ban4embed)

            except Exception as e:

                await ctx.send(f"**<a:error:1030396429761531904> | Failed To Ban, {member}**")
 

@client.command(aliases=["mc"])
async def membercount(ctx):
    embed = discord.Embed(title=f"**{dash} Members!**",
        description=
        f"**{rep} {ctx.guild.member_count}**")
    await ctx.send(embed=embed)

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(f"moderating /vltop"))

@client.command()
async def warn(ctx, member: discord.Member, * , reason="`No Reason Provided`"):
        await ctx.send(f"**{tick} | `{member.display_name}` Has Been Warned For :`{reason}`**")
        await member.send(f"**You Have Been Warned In `{ctx.guild.name}` for: `{reason}`**")

@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    embed = discord.Embed(title="/vltop")
    embed.add_field(name="<a:success:1030356353581076491> Unmuted", value=f"{member.mention}" , inline = False)
    embed.set_footer(text="/vltop", icon_url="https://cdn.discordapp.com/avatars/968425218144079913/63b021f7d084709ed06406237d3dff4a.webp?size=1024")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/968425218144079913/63b021f7d084709ed06406237d3dff4a.webp?size=1024")
    await ctx.send(embed = embed , mention_author = False)

@client.command("purge")
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send((f"** {tick} Successfully Purged {amount} Messages**"), delete_after=5)

@client.command(aliases=["Roleremove", "rr", "remove"])
@commands.has_permissions(administrator=True)
async def removerole(ctx, member : discord.Member, role : discord.Role):
    await member.remove_roles(role)
    await ctx.send(f"**{tick} | SuccessFully Removed {role} from {member.mention}**")

@client.command(aliases=["addrole", "give", "add"])
@commands.has_permissions(administrator=True)
async def ar(ctx, member : discord.Member, role : discord.Role):
    await member.add_roles(role)
    await ctx.send(f"**{tick} | SuccessFully Added {role} to {member.mention}**")

#lock cmds

@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    channel = ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role,
                                      overwrite=overwrite)
    await ctx.send(f'**{tick} | SuccessFully Locked {channel.mention}**')

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    channel = ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await ctx.channel.set_permissions(ctx.guild.default_role,
                                      overwrite=overwrite)
    await ctx.send(f'**{tick} | SuccessFully Unlocked {channel.mention}**')

@client.command(

    name="unlockall",

    description=

    "Unlocks the server. | Warning: this unlocks every channel for the everyone role.",

    usage="unlockall")

@commands.has_permissions(administrator=True)

@commands.cooldown(1, 5, commands.BucketType.channel)

async def unlockall(ctx, server: discord.Guild = None, *, reason=None):

    await ctx.message.delete()

    if server is None: server = ctx.guild

    try:

        for channel in server.channels:

            await channel.set_permissions(

                ctx.guild.default_role,

                overwrite=discord.PermissionOverwrite(send_messages=True),

                reason=reason)

        await ctx.send(f"**{tick} | Successfully UnLocked All Channels Of The Server**")

    except:

        await ctx.send(f"**{cross} | Failed to unlock, {server}**")

    else:

        pass
@client.command(name="lockall",

                description="Locks down the server.",

                usage="lockall")

@commands.has_permissions(administrator=True)

@commands.cooldown(1, 5, commands.BucketType.channel)

async def lockall(ctx, server: discord.Guild = None, *, reason=None):

    await ctx.message.delete()

    if server is None: server = ctx.guild

    try:

        for channel in server.channels:

            await channel.set_permissions(

                ctx.guild.default_role,

                overwrite=discord.PermissionOverwrite(send_messages=False),

                reason=reason)

        await ctx.send(f"**{tick} | Successfully Locked All Channels Of The Server**")

    except:

        await ctx.send(f"{cross} | **Failed To Lockdown, {server}**```")

    else:

        pass
#end
#onc
@client.command(aliases=["onc"])
@commands.guild_only()
@commands.cooldown(1, 2, commands.BucketType.guild)
async def onlinecount(ctx):
    onmc = 0
    idlemc = 0 
    dndmc = 0 
    offmc = 0
    estmem = 0
    for mem in list(ctx.guild.members):
        estmem += 1
        if f"{mem.status}" == "online":
            onmc += 1
        elif f"{mem.status}" == "idle":
            idlemc += 1
        elif f"{mem.status}" == "dnd":
            dndmc += 1
        elif f"{mem.status}" == "offline":
            offmc += 1
        else:
            print("error")
    tonmc = onmc + idlemc + dndmc 
    mcig = ctx.guild.member_count
    embed = discord.Embed(title=f"{ctx.guild.name}", description=f"\n<:online:1031104295870922772> {onmc}\n<:idle_static:1031104207907999854> {idlemc}\n<:dnd_static:1031104263499292744> {dndmc}\n<:offline_static:1031104426666102845> {offmc}\n\n**Total Online - {tonmc}\nTotal Members - {mcig}**")
    await ctx.send(embed=embed)

@client.command(aliases=["make-embed", "embed"])
async def make_embed(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    await ctx.send('**Please Enter A Title For Your Embed!**')
    title = await client.wait_for('message', check=check)
  
    await ctx.send('**Please Enter A Description For Your Embed!**')
    desc = await client.wait_for('message', check=check)

    embed = discord.Embed(title=title.content, description=desc.content)
    await ctx.send(embed=embed)

import datetime
import humanfriendly

@client.command()
async def mute(ctx, mem:discord.Member, time, *, reason):
  if mem == None:
    em = discord.Embed(description="Mention a member")
    await ctx.send(embed=em)
  if time == None:
    emm = discord.Embed(description="Give amount of time", colour=000000)
    await ctx.send(embed=emm)
  if reason == None:
    pass
  time = humanfriendly.parse_timespan(time)
  await mem.edit(timeout=datetime.datetime.utcnow()+datetime.timedelta(seconds=time))
  emmm = discord.Embed(description=f"Timeout given to {mem} for {time} reason : {reason}", colour=000000)
  await ctx.send(embed=emmm)

#truth&dare

truth_msg = [
    "How would you rate your looks on a scale from 1-10?",
    "What is one thing that brings a smile to your face, no matter the time of day?",
    "What’s is one thing that you’re proud of?",
    "Have you ever broken anything of someone else's and not told the person?",
    "Who is your boyfriend/girlfriend/partner?",
    "When was the last time you lied?", "When was the last time you cried?",
    "What's your biggest fear?", "What's your biggest fantasy?",
    "Do you have any fetishes?",
    "What's something you're glad your mum doesn't know about you?",
    "Have you ever cheated on someone?",
    "What was the most embarrassing thing you’ve ever done on a date?",
    "Have you ever accidentally hit something (or someone!) with your car?",
    "Name someone you’ve pretended to like but actually couldn’t stand.",
    "What’s your most bizarre nickname?",
    "What’s been your most physically painful experience?",
    "What bridges are you glad that you burned?",
    "What’s the craziest thing you’ve done on public transportation?",
    "If you met a genie, what would your three wishes be?",
    "If you could write anyone on Earth in for President of the United States, who would it be and why?",
    "What’s the meanest thing you’ve ever said to someone else?",
    "Who was your worst kiss ever?",
    "What’s one thing you’d do if you knew there no consequences?",
    "What’s the craziest thing you’ve done in front of a mirror?",
    "What’s the meanest thing you’ve ever said about someone else?",
    "What’s something you love to do with your friends that you’d never do in front of your partner?",
    "Who are you most jealous of?", "What do your favorite pajamas look like?",
    "Have you ever faked sick to get out of a party?",
    "Who’s the oldest person you’ve dated?",
    "How many selfies do you take a day?",
    "How many times a week do you wear the same pants?",
    "Would you date your high school crush today?", "Where are you ticklish?",
    "Do you believe in any superstitions? If so, which ones?",
    "What’s one movie you’re embarrassed to admit you enjoy?",
    "What’s your most embarrassing grooming habit?",
    "When’s the last time you apologized? What for?",
    "How do you really feel about the Twilight saga?",
    "Where do most of your embarrassing odors come from?",
    "Have you ever considered cheating on a partner?", "Boxers or briefs?",
    "Have you ever peed in a pool?",
    "What’s the weirdest place you’ve ever grown hair?",
    "If you were guaranteed to never get caught, who on Earth would you murder?",
    "What’s the cheapest gift you’ve ever gotten for someone else?",
    "What app do you waste the most time on?",
    "What’s the weirdest thing you’ve done on a plane?",
    "Have you ever been nude in public?",
    "How many gossip blogs do you read a day?",
    "What is the youngest age partner you’d date?",
    "Have you ever lied about your age?", "Have you ever used a fake ID?",
    "Who’s your hall pass?", "What is your greatest fear in a relationship?",
    "Have you ever lied to your boss?", "Who would you hate to see naked?",
    "Have you ever regifted a present?",
    "Have you ever had a crush on a coworker?",
    "Have you ever ghosted a friend?", "Have you ever ghosted a partner?",
    "What’s the most scandalous photo in your cloud?",
    "When’s the last time you dumped someone?",
    "What’s one useless skill you’d love to learn anyway?",
    "If I went through your cabinets, what’s the weirdest thing I’d find?",
    "Have you ever farted and blamed it on someone else?"
]


@client.command()
@commands.cooldown(1, 2, commands.BucketType.user)
async def truth(ctx):
    await ctx.send(f"`{random.choice(truth_msg)}`", mention_author=False)

dare_msg = [
    "Let the person on your right take an ugly picture of you and your double chin and post it on IG with the caption, “I don’t leave the house without my double chin",
    " Eat a raw potato",
    "Order a pizza and pay the delivery guy in all small coins",
    "Open the window and scream to the top of our lungs how much you love your mother",
    "Kiss the person who is sitting beside you",
    "Beg for a cent on the streets",
    "Go into the other room, take your clothes off and put them on backward",
    "Show everyone your search history for the past week",
    "Set your crush’s picture as your FB profile picture",
    "Take a walk down the street alone and talk to yourself",
    "Do whatever someone wants for the rest of the day",
    " Continuously talk for 3 minutes without stopping",
    " Draw something on the face with a permanent marker",
    " Peel a banana with your feet",
    " Lay on the floor for the rest of the game",
    " Drink 3 big cups of water without stopping",
    "Go back and forth under the table until it’s your turn again",
    " Close your mouth and your nose: try to pronounce the letter ‘“A” for 10 seconds",
    "Ask someone random for a hug",
    "Call one of your parents and then tell them they are grounded for a week",
    "Have everyone here list something they like about you",
    "Wear a clothing item often associated with a different gender tomorrow",
    "Prank call your crush",
    "Tweet 'insert popular band name here fans are the worst' and don't reply to any of the angry comments.",
    "List everyone as the kind on animal you see them as.",
    "Talk in an accent for the next 3 rounds",
    "Let someone here do your makeup.", "Spin around for 30 seconds",
    "Share your phone's wallpaper",
    "Ask the first person in your DMs to marry you.",
    "Show the last DM you sent without context",
    "Show everyone here your screen time.", "Try to lick your elbow",
    "Tie your shoe strings together and try to walk to the door and back",
    "Everything you say for the next 5 rounds has to rhyme.",
    "Text your crush about how much you like them, but don't reply to them after that.",
    "Ask a friend for their mom's phone number",
    "Tell the last person you texted that you're pregnant/got someone pregnant.",
    "Do an impression of your favorite celebrity",
    "Show everyone the last YouTube video you watched.",
    "Ask someone in this server out on a date.",
    "Kiss the player you think looks the cutest."
]


@client.command()
@commands.cooldown(1, 2, commands.BucketType.user)
async def dare(ctx):
  await ctx.send(f"`{random.choice(dare_msg)}`", mention_author=False)

#etx

@client.command(aliases=["solve", "calculate"])
async def math(ctx, *, expression:str):
    calculation = eval(expression)
    await ctx.send('Expression: {}\nAnswer: {}'.format(expression, calculation))

@client.command(aliases=["ri"])
async def roleinfo(ctx, role: discord.Role = None):
  riembed = discord.Embed(title=f"**{role.name}'s Information**")
  riembed.add_field(name='**<:emoji_10:1030346902367125564>__General info__**', value=f"**<:reply:1030346679758630912> Name: {role.name}\n<:reply:1030346679758630912> Role ID: {role.id}\n<:reply:1030346679758630912> Position: {role.position}\n<:reply:1030346679758630912> Hex Code: {role.color}\n<:reply:1030346679758630912> Mentionable: {role.mentionable}\n<:reply:1030346679758630912> Created At: {role.created_at}**")
  await ctx.send(embed=riembed, mention_author=False)

#off
@client.command()
@commands.cooldown(1, 12, commands.BucketType.user)
@has_permissions(manage_roles=True)
@commands.guild_only()
async def official(ctx, member: discord.Member, *reason):
    if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.", mention_author=False)
     return None
    elif reason == " ":
      reason = None 
    else:
      reason = " ".join(reason)
    responsible = f"Action done by {ctx.message.author.name}#{ctx.author.discriminator}, Reason: {reason}."
    role = discord.utils.get(ctx.guild.roles, id=officialrole)
    toprol = discord.utils.get(ctx.guild.roles, id=toprole)
    if toprol in member.roles:
       await ctx.reply("Action rejected, unable to add roles to this user.", mention_author=False, delete_after=6)
       return
    elif role in member.roles:
       await ctx.reply("Action rejected, This user is already an official.", mention_author=False, delete_after=6)
       return
    await member.add_roles(role, reason=responsible)
    try:
       await member.send(f"You have been successfully added to TEAM SPY™ Official Team!!\nReason: `{reason}`.\n Join in - || {official_sv} ||")
       await ctx.reply(f"Added {member.mention} to Official Team, *User was notified*, Reason: `{reason}`.", mention_author=False) 
    except: 
       await ctx.reply(f"Added {member.mention} to Official Team, *User was not notified*, Reason: `{reason}`.", mention_author=False) 
@client.command(aliases=["officialscount", "countofficials", "countofficial", "officialcount"])
@commands.cooldown(1, 60, commands.BucketType.user)
#@has_permissions(manage_roles=True)
@commands.guild_only()
async def officials(ctx):
  role = ctx.guild.get_role(officialrole)
  tag = 0
  for m in ctx.guild.members:
        if tagxd in m.name:
             tag += 1
        continue
  total = len(role.members)
  sup = total - tag
  embed = discord.Embed(color=00000, title=f"{guildname}", description=f">>> __Officials__ - {tag}\n__Supporters__ - {sup}\n__Total__ - {total}")
  embed.set_footer(text=f"/{vanitycode} | officials", icon_url=ctx.guild.icon_url) 
  await ctx.reply(embed=embed, mention_author=False)
@client.command(aliases=["rmofficial"])
@commands.cooldown(1, 12, commands.BucketType.user)
@has_permissions(manage_roles=True)
@commands.guild_only()
async def rofficial(ctx, member: discord.Member, *reason):
    if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
    elif reason == " ":
      reason = None 
    else:
      reason = " ".join(reason)
    responsible = f"Action done by {ctx.message.author.name}#{ctx.author.discriminator}, Reason: {reason}."
    role = discord.utils.get(ctx.guild.roles, id=officialrole)
    await member.remove_roles(role, reason=responsible)
    try:
       await member.send(f"You have been removed from TEAM SPY™ official Team, wanna get back in? Add the vanity in your status / about.\nReason: `{reason}`.")
       await ctx.reply(f"Removed {member.mention} from Official Team, *User was notified*, Reason: `{reason}`.") 
    except: 
       await ctx.reply(f"Removed {member.mention} from Official Team, *User was not notified*, Reason: `{reason}`.") 
@client.command()
@commands.cooldown(1, 250, commands.BucketType.guild)
@commands.guild_only()
@has_permissions(manage_roles=True)
#@commands.is_owner()
async def syncofficials(ctx, *reason):
    if pforp == True:
     await ctx.reply("Command execution cancelled | P4P mode is enabled.")
     return None
    elif reason == " ":
      reason = None 
    else:
      reason = " ".join(reason)
    await ctx.reply(f"syncing officials with the role • Officials™, Reason: `{reason}`.")
    responsible = f"Officials sync | Action done by {ctx.message.author.name}#{ctx.author.discriminator}"
    role = discord.utils.get(ctx.guild.roles, id=officialrole)   
    mem = await ctx.guild.chunk()
    membercount = 0
    for user in mem:
        if tagxd in user.name:
            if role in user.roles:
                continue 
            else: 
                await user.add_roles(role, reason=responsible)
                try: 
                   await user.send(f"You have been successfully added to TEAM SPY™ Official Team!!\n Join in - || {official_sv} ||")
                except: 
                   await ctx.reply(f"Unable to add roles to {user.name} or failed to send a dm.")
                   continue
        else:
            pass
#             if role in user.roles: 
#                 try:
#                    for x in user.roles:
#                      try:
#                         await user.remove_roles(x, reason=responsible)
#                      except: 
                        
#                         continue  
#                    await user.send("You have been removed from TEAM SPY™ official Team, wanna get back in? Apply the Tag.")
#                 except: 
#                    try: 
#                       await user.remove_roles(role, reason=responsible)
#                       await user.send("You have been removed from TEAM SPY™ official Team, wanna get back in? Apply the Tag.")
#                    except:
#                       await ctx.reply(f"Unable to remove roles from {user.name} or failed to send a dm.")
#                       continue 
                #try: 
                  # await user.send("You have been removed from TEAM SPY™ official team, wanna get back in? Apply the tag.")
              #  except: 
                 #  continue   


client.run(tkn)
