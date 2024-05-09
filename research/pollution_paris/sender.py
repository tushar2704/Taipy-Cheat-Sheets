#© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
## Realtime Pollution for Paris Demo by Tushar Aggarwal
#######################################################################################################
import time
import socket
import random

HOST = "127.0.0.1"
PORT = 5050

pollution_locations = ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral", "Champs-Élysées", "Montmartre"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        location = random.choice(pollution_locations)
        pollution_level = random.randint(1, 500)
        data = f"{location},{pollution_level}"
        s.sendall(data.encode())
        print(f"Sending: {data}")
        time.sleep(5)