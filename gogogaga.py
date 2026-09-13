import random
import string
import time
import streamlit as str
start = input("type 'start' to play: ").lower()

times = []

if start == "start":
    print("game started!")

    while True:
        game_asset = random.choice(string.ascii_lowercase + string.digits)

        print(game_asset)

        start_time = time.perf_counter()

        answer = input("> ")

        end_time = time.perf_counter()

        if answer.lower() == "stop":
            break

        reaction_time = end_time - start_time
        times.append(reaction_time)

        print(reaction_time)

    if times:
        average = sum(times) / len(times)
        print(f"Average time: {average:.2f} seconds")

else:
    print("type 'start'")