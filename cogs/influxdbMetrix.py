from sqlite3 import Timestamp
from discord.ext import commands, tasks
import psutil, datetime, time

from influx.influxdbExport import sendingServers
from influx.influxdbExport import sendingSYS

# This file is used to get Metrix for InfluxDB about uptime number of servers and more
# it s in a cog to be initalized when the bot is starting up


class InfluxMetrix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.exportServer.start()
        self.getSysData.start()
        self.getUptime.start()

    global startTime, timeStamp
    startTime = time.time()

    @tasks.loop(minutes=10)
    async def exportServer(self):
        serversNum = len(self.bot.guilds)

        sendingServers(serversNum)

    @tasks.loop(minutes=5)
    async def getSysData(self):
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage("/")
        i = 0
        send = []

        cpuPerc = [psutil.cpu_percent(), "cpuUsed%", "cpu"]
        ramUsed = [ram.percent, "ramUsed%", "ram"]
        diskUsedPerc = [disk.percent, "diskUsed%", "disk"]

        send = [cpuPerc, ramUsed, diskUsedPerc]

        try: 
            latency = [round(self.bot.latency * 1000), "latency", "network"]
            send.append(latency)
        except:
            print("Failed to retrieve Latency")
        
        while i < len(send): #looping throught send array
            sendingSYS(send[i])
            i = i + 1

    @tasks.loop(minutes=1)
    async def getUptime(self):
        seconds = round(time.time() - startTime)
        
        #global timeStamp
        timeStamp = str(datetime.timedelta(seconds=seconds))
        return timeStamp
        


def setup(bot):
    bot.add_cog(InfluxMetrix(bot))