from pypresence import Presence
import time


client_id = "935073585993764864"
RPC = Presence(client_id )
RPC.connect()

while True:
    RPC.update(
        large_image="logo1",
        large_text="Watching Michael media group",
        details="Watching Michael Media Group",
        state="The Vids are free",
        start=int(time.time()),
        buttons= [{"label": "Take a look at the channel","url":"https://www.youtube.com/channel/UCseznP4Qb2DrRcDXcnAx_iw"}, {"label": "We Have a discord","url":"https://discord.gg/n6VsC86uzp"}]
    )
    time.sleep(60)