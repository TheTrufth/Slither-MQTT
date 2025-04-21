import json
import threading
import paho.mqtt.client as mqtt
from config import BROKER, PORT, TOPIC_PREFIX, PLAYER_ID

players = {}

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print(f"[MQTT] Connected with result code {rc}")
    client.subscribe(f"{TOPIC_PREFIX}+")

def on_message(client, userdata, msg):
    topic_parts = msg.topic.split("/")
    other_id = topic_parts[-1]
    if other_id == PLAYER_ID:
        return
    try:
        data = json.loads(msg.payload.decode())
        players[other_id] = data
    except Exception as e:
        print("[MQTT] Error parsing:", e)

def send_snake_state(snake):
    payload = json.dumps(snake)
    client.publish(f"{TOPIC_PREFIX}{PLAYER_ID}", payload)

def start_mqtt():
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    thread = threading.Thread(target=client.loop_forever, daemon=True)
    thread.start()
