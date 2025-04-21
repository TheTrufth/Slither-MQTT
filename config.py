import uuid

# MQTT Settings
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC_PREFIX = "slither/players/"

# Game Settings
WINDOW_SIZE = 600
CELL_SIZE = 20
FPS = 10

# Player info
PLAYER_ID = str(uuid.uuid4())[:8]
COLORS = [(0, 255, 0), (0, 0, 255), (255, 0, 0), (255, 165, 0), (128, 0, 128)]
COLOR = COLORS[hash(PLAYER_ID) % len(COLORS)]
