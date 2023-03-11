import os
from dotenv import load_dotenv

import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

#from .influxSecrets import influxDB; # importing vars for InfluxDBClient

#defining var's for InfluxDBClient
load_dotenv()
url = os.getenv("INFLUX_URL")
token = os.getenv("INFLUX_TOKEN")
bucket = os.getenv("INFLUX_BUCKET")
org = os.getenv("INFLUX_ORG")

writeClient = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
writeApi = writeClient.write_api(write_options=SYNCHRONOUS)

def sendingCom(cog, command, n):
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
    writeApi.write(bucket=bucket, org=org, record=data)

def sendingH(array):
    data = {
        "measurement": "commands",
        "tags": {
            "cog": array[2],
            "command": array[1]
        } ,
        "fields": {
            "numCalledH": array[0]
        }
    }

    writeApi.write(bucket, org, data)

def sendingServers(serversNum):
    data = {
        "measurement": "servers",
        "tags": {
            "onServers": "onServersNum",
        },
        "fields": {
            "serversNum": serversNum,
        }
    }
    writeApi.write(bucket, org, data)
    return
    

def sendingSYS(array):
    data = {
        "measurement": "system",
        "tags": {
            "spec": array[2],
        } ,
        "fields": {
            array[1]: array[0],
        }
    }

    writeApi.write(bucket, org, data)


def sendingErrors(array):
    data = {
        "measurement": "ERRORS",
        "tags": {
            "type": array[0],
        },
        "fields": {
            "errorsNum": array[1],
        }
    }
    writeApi.write(bucket, org, data)