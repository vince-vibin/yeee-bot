import discord
from discord.ext import commands, tasks

from influx.influxdbExport import sendingServers

class InfluxMetrix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.exportServer.start()

    @tasks.loop(minutes=1)
    async def exportServer(self):
        serversNum = len(self.bot.guilds)
        serverList = self.bot.guilds

        print(serverList, serversNum)

        sendingServers(serversNum)

def setup(bot):
    bot.add_cog(InfluxMetrix(bot))