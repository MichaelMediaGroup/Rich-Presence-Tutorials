from pypresence import Presence
import time
import random

client_id = "935073585993764864"
RPC = Presence(client_id )
RPC.connect()

quotes =[
    "Michael media group vids are free",
    "Like And Sub",
    "Cake is nice",
    "Allways code with a cup of tea",
    "We have a discord Server. Link in description"
]

while True:
    RPC.update(details="Quote:", state=random.choice(quotes))
    time.sleep(5)