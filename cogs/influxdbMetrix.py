from sqlite3 import Timestamp
from discord.ext import commands, tasks

import psutil, datetime, time

from influx.influxdbExport import sendingServers
from influx.influxdbExport import sendingSYS

# This file is used to get Metrix for InfluxDB about uptime number of servers and more
# it s in a cog to be initalized when the bot is starting up


class InfluxMetrix(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
        global startTime, timeStamp
        startTime = time.time()
        self.uptime = 0
        
    async def exportServer(self):
        serversNum = 69 #len(self.bot.guilds)
        sendingServers(serversNum)
        return
    
    async def getSysData(self):
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage("/") # returns the disk usage on the disk the bot is running on
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
            print("        Failed to retrieve Latency")
        
        while i < len(send): #looping throught send array
            sendingSYS(send[i])
            i = i + 1

    async def getUptime(self):
        seconds = round(time.time() - startTime)
    
        timeStamp = str(datetime.timedelta(seconds=seconds))
        InfluxMetrix.uptime = timeStamp

    

def setup(bot):
    bot.add_cog(InfluxMetrix(bot))