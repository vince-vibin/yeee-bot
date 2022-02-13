from discord.ext import commands
import discord

from utils import mods_or_owner


class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(description="Kick a member",brief="Kick a member")
    @mods_or_owner()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, reason: str = "He got kicked. Probably cause he is dumb"):
        if member is not None:
            embed = discord.Embed(colour=discord.Colour.orange())
            embed.add_field(name="Kicked", value=member)
            embed.add_field(name="Reason", value=reason, inline=False)
            await ctx.guild.kick(member, reason=reason)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(colour=discord.Colour.orange())
            embed.add_field(name="Bruh", value="Add member if you are to incompetent to do that i dont know why you are in the server team.")
            await ctx.send(embed=embed)

    @commands.command(description="Ban a member",brief="Ban a member")
    @mods_or_owner()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, reason: str = "He got banned. Probably cause he is dumb"):
        if member is not None:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.add_field(name="Banned", value=member, inline=False)
            embed.add_field(name="Reason", value=reason, inline=False)
            await ctx.guild.ban(member, reason=reason)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.add_field(name="Bruh", value="Add member if you are to incompetent to do that i dont know why you are in the server team.")
            await ctx.send(embed=embed)

    @commands.command(description="Unban a Member",brief="Unban a Member")
    async def unban(self, ctx, *, member):
       banned_users = await ctx.guild.bans()
       member_name, member_discriminator = member.split("#")

       for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
               embed = discord.Embed(colour=discord.Colour.green())
               embed.add_field(name="Unbanned", value=user, inline=False)
               await ctx.guild.unban(user)
               await ctx.send(embed=embed)
               return
            else:
               embed = discord.Embed(colour=discord.Colour.green())
               embed.add_field(name="Unbanned", value=user, inline=False)
               await ctx.guild.unban(user)
               await ctx.send(embed=embed)

    @commands.command(description="Get server status",brief="Get server status")
    @mods_or_owner()
    async def serverinfo(self, ctx, *args):
        guild = ctx.guild
        embed = discord.Embed(colour=0xA8FFD5)
        numb_voicechannels = len(guild.voice_channels)
        numb_textchannels = len(guild.text_channels)
        numb_member = len(guild.members)
        owner = (guild.owner)
        server_icon = ctx.guild.icon_url
        server_region = (guild.region)
        description = (guild.description)
        max_members = (guild.max_members)
        system_channel = (guild.system_channel)
        rules_channel = (guild.rules_channel)
        afk_channel = (guild.afk_channel)

        embed.set_thumbnail(url=server_icon)
        embed.add_field(name="Server Name", value=guild.name, inline=False)
        embed.add_field(name="Region", value=server_region)
        embed.add_field(name="Owner", value=owner, inline=False)
        embed.add_field(name="Voice Channels", value=numb_voicechannels, inline=True)
        embed.add_field(name="Text Channels", value=numb_textchannels, inline=False)
        embed.add_field(name="System Channel", value=system_channel)
        embed.add_field(name="Rules Channel", value=rules_channel)
        embed.add_field(name="AFK Channel", value=afk_channel)
        embed.add_field(inline=False, name="Member Count", value=numb_member)
            
        emoji_string = ""
        for e in guild.emojis:
            if e.is_usable():
                emoji_string += str(e)
        embed.add_field(name="Emojies",
                        value=emoji_string or "No emojis setup", inline=False)


        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Moderator(bot))