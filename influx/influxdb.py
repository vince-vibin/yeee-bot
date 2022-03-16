from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS


from .influxSecrets import influxDB; # importing vars for InfluxDBClient

#defining var's for InfluxDBClient from secrets.py
url = influxDB[0]
token = influxDB[1]
bucket = influxDB[2]
org = influxDB[3]

def sendingCom(cog, command, n):
    with InfluxDBClient(url=url, token=token, org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)
            

        #data = "commands,command={} numCalled={} ".format(command, n)
        data = {
            "measurement": "commands",
            "tags": {
                "cog": cog,
                "command": command
            } ,
            "fields": {
                "numCalled": n
            }
        }

        write_api.write(bucket, org, data)

        client.close()
        print("client closed and request send")

def sendingH(array):
    with InfluxDBClient(url=url, token=token, org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)
            

        #data = "commands,command={} numCalled={} ".format(command, n)
        data = {
            "measurement": "commandsH",
            "tags": {
                "cog": array[2],
                "command": array[1]
            } ,
            "fields": {
                "numCalledH": array[0]
            }
        }

        write_api.write(bucket, org, data)

        client.close()
        print("client closed and request send")