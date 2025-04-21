import uuid
import hashlib

# MQTT Settings
BROKER = "localhost"
PORT = 1883
TOPIC_PREFIX = "slither/players/"
PUBLISH_INTERVAL = 0.1  # seconds

# Game Settings
WINDOW_SIZE = 600
CELL_SIZE = 20
FPS = 10


# Player info
COLORS = [(0, 255, 0), (0, 0, 255), (255, 0, 0), (255, 165, 0), (128, 0, 128)]
PLAYER_ID = str(uuid.uuid4())[:8]


def consistent_color(player_id):
    index = int(hashlib.md5(player_id.encode()).hexdigest(), 16) % len(COLORS)
    return COLORS[index]


COLOR = consistent_color(PLAYER_ID)
