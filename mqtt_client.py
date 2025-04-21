import json
import time
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

    payload = msg.payload.decode().strip()

    if not payload:
        # Empty payload = player disconnected
        print(f"[MQTT] Player {other_id} disconnected.")
        if other_id in players:
            del players[other_id]
        return

    try:
        msg_json = json.loads(payload)
        snake = msg_json.get("snake")
        timestamp = msg_json.get("time", 0)
        if other_id not in players:
            players[other_id] = {"history": []}

        players[other_id]["history"].append({"time": timestamp, "snake": snake})

        # Keep only the last 2 updates
        players[other_id]["history"] = players[other_id]["history"][-2:]

        # print(f"[MQTT] Received from {other_id} at {timestamp}: {snake}")
    except Exception as e:
        print("[MQTT] Error parsing:", e)


def send_snake_state(snake):
    payload = json.dumps({"snake": snake, "time": time.time()})
    client.publish(f"{TOPIC_PREFIX}{PLAYER_ID}", payload)


def send_disconnect():
    client.publish(f"{TOPIC_PREFIX}{PLAYER_ID}", "")


def start_mqtt():
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.loop_start()  # <-- switch from thread + loop_forever
