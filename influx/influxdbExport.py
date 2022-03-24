from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

import datetime

from .influxSecrets import influxDB; # importing vars for InfluxDBClient

#defining var's for InfluxDBClient from secrets.py
url = influxDB[0]
token = influxDB[1]
bucket = influxDB[2]
org = influxDB[3]

def sendingCom(cog, command, n):
    with InfluxDBClient(url=url, token=token, org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)

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

def sendingH(array):
    with InfluxDBClient(url=url, token=token, org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)

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

        write_api.write(bucket, org, data)
        client.close()

def sendingServers(serversNum):
    with InfluxDBClient(url=url, token=token, org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)

        data = {
            "measurement": "servers",
            "tags": {
                "onServers": "onServersNum",
            },
            "fields": {
                "serversNum": serversNum,
            }
        }
        write_api.write(bucket, org, data)
        client.close()

def sendingSYS(array):
    with InfluxDBClient(url=url, token=token, org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)

        data = {
            "measurement": "system",
            "tags": {
                "spec": array[2],
            } ,
            "fields": {
                array[1]: array[0],
            }
        }

        write_api.write(bucket, org, data)
        client.close()

def sendingErrors(array):
    with InfluxDBClient(url=url, token=token, org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)

        data = {
            "measurement": "ERRORS",
            "tags": {
                "type": array[0],
            },
            "fields": {
                "errorsNum": array[1],
            }
        }
        write_api.write(bucket, org, data)
        client.close()