#© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Taipy Cheat Sheets [https://github.com/tushar2704/Taipy-Cheat-Sheets] (https://github.com/tushar2704/Taipy-Cheat-Sheets)
#######################################################################################################
## Start with Taipy Application Demo by Tushar Aggarwal
#######################################################################################################
#Run sender.py first
import os 
import pathlib
import socket
from threading import Thread
from taipy.gui import Gui, State, invoke_callback, get_state_id

HOST = "127.0.0.1"  
PORT = 5050

state_id_list = []

def on_init(state: State):
    state_id = get_state_id(state)
    if (state_id := get_state_id(state)) is not None:
        state_id_list.append(state_id)

def client_handler(gui: Gui, state_id_list: list):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    conn, _ = s.accept()
    while True:
        if data := conn.recv(1024):
            location, pollution_level = data.decode().split(",")
            print(f"Data received: Location: {location}, Pollution Level: {pollution_level}")
            if hasattr(gui, "_server") and state_id_list:
                invoke_callback(
                    gui, state_id_list[0], update_received_data, (location, int(pollution_level))
                )
        else:
            print("Connection closed")
            break

def update_received_data(state: State, location, pollution_level):
    state.location = location
    state.pollution_level = pollution_level

location = ""
pollution_level = 0

md = """
# Realtime Pollution for Paris

## Latest Data:
- Location: <|{location}|>  
- Pollution Level: <|{pollution_level}|>

"""

gui = Gui(page=md)

t = Thread(
    target=client_handler,
    args=(
        gui,
        state_id_list,
    ),
)
t.start()

gui.run(title="Realtime Pollution for Paris")