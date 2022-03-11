from msilib import sequence
from aiohttp import PAYLOAD_REGISTRY, JsonPayload
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


from .influxSecrets import influxDB; # importing vars for InfluxDBClient

#defining var's for InfluxDBClient from secrets.py
url = influxDB[0]
token = influxDB[1]
bucket = influxDB[2]
org = influxDB[3]

def sending(n):
    i = 0
    while i < 5:
        
        with InfluxDBClient(url=url, token=token, org=org) as client:
            write_api = client.write_api(write_options=SYNCHRONOUS)

            data = "test,host=donatello testPayload={}".format(n)

            write_api.write(bucket, org, data)

            client.close()

        i = i + 1