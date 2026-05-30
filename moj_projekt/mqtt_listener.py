import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moj_site.settings")
django.setup()

from sensor.models import Pomiar

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Połączono z MQTT")
    client.subscribe("sensor/distance")


def on_message(client, userdata, msg):

    value = float(msg.payload.decode())

    Pomiar.objects.create(
        distance=value
    )

    print("Zapisano:", value)


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()
