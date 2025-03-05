import os
import time
import random
import json
import socket
import datetime
import platform
import pyttsx3
import wikipedia
import qrcode
import pyshorteners
from colorama import Fore, Style, init
from faker import Faker

# Initialize Colorama
init(autoreset=True)

# ASCII Art Placeholder (Insert Your ASCII Art Here)
ascii_art = """
_____ ____  ____  ____  ____    _      _     _   _____  _ 
/  __//  __\/  __\/  _ \/  __\  / \__/|/ \ /\/ \ /__ __\/ \
|  \  |  \/||  \/|| / \||  \/|  | |\/||| | ||| |   / \  | |
|  /_ |    /|    /| \_/||    /  | |  ||| \_/|| |_/\| |  | |
\____\\_/\_\\_/\_\\____/\_/\_\  \_/  \|\____/\____/\_/  \_/
                                                           
"""

# Clear Screen Function
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# To-do List
TODO_FILE = "todo_list.json"

def load_todo():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_todo(todo_list):
    with open(TODO_FILE, "w") as file:
        json.dump(todo_list, file)

# Calculator
def calculator():
    clear_screen()
    try:
        expression = input("Enter an expression (e.g., 5 + 3 * 2): ")
        result = eval(expression)
        print(Fore.GREEN + f"Result: {result}")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

# Random Joke
def joke():
    clear_screen()
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Parallel lines have so much in common. It’s a shame they’ll never meet."
    ]
    print(Fore.LIGHTCYAN_EX + random.choice(jokes))

# Password Generator
def password_generator():
    clear_screen()
    length = int(input("Enter password length: "))
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
    password = "".join(random.choice(chars) for _ in range(length))
    print(Fore.GREEN + f"Generated Password: {password}")

# Coin Flip
def coin_flip():
    clear_screen()
    print(Fore.YELLOW + f"Coin Flip Result: {random.choice(['Heads', 'Tails'])}")

# Dice Roll
def dice_roll():
    clear_screen()
    print(Fore.CYAN + f"Dice Roll Result: {random.randint(1, 6)}")

# Countdown Timer
def countdown_timer():
    clear_screen()
    seconds = int(input("Enter countdown time in seconds: "))
    for i in range(seconds, 0, -1):
        print(f"Time Left: {i} sec", end="\r")
        time.sleep(1)
    print(Fore.RED + "Time's up!")

# Text-to-Speech
def text_to_speech():
    clear_screen()
    engine = pyttsx3.init()
    text = input("Enter text to speak: ")
    engine.say(text)
    engine.runAndWait()

# Get IP Address
def ip_finder():
    clear_screen()
    print(Fore.LIGHTMAGENTA_EX + f"Your IP Address: {socket.gethostbyname(socket.gethostname())}")

# System Info
def system_info():
    clear_screen()
    print(Fore.YELLOW + f"System: {platform.system()} {platform.release()}")
    print(Fore.CYAN + f"Machine: {platform.machine()}")
    print(Fore.LIGHTMAGENTA_EX + f"Processor: {platform.processor()}")

# File Explorer
def file_explorer():
    clear_screen()
    print(Fore.LIGHTCYAN_EX + "Files in current directory:")
    print("\n".join(os.listdir()))

# Date & Time
def date_time():
    clear_screen()
    print(Fore.GREEN + f"Current Date & Time: {datetime.datetime.now()}")

# Age Calculator
def age_calculator():
    clear_screen()
    birth_year = int(input("Enter your birth year: "))
    print(Fore.LIGHTYELLOW_EX + f"Your Age: {datetime.datetime.now().year - birth_year}")

# Fun Fact
def fun_fact():
    clear_screen()
    facts = ["Honey never spoils.", "Bananas are berries, but strawberries aren't.", "A day on Venus is longer than a year on Venus."]
    print(Fore.CYAN + random.choice(facts))

# QR Code Generator
def qr_generator():
    clear_screen()
    data = input("Enter text or URL for QR Code: ")
    qr = qrcode.make(data)
    qr.save("qrcode.png")
    print(Fore.GREEN + "QR Code saved as 'qrcode.png'!")

# URL Shortener
def url_shortener():
    clear_screen()
    url = input("Enter a long URL: ")
    s = pyshorteners.Shortener()
    print(Fore.YELLOW + f"Shortened URL: {s.tinyurl.short(url)}")

# Wikipedia Search
def wiki_search():
    clear_screen()
    query = input("Enter search term: ")
    print(Fore.LIGHTMAGENTA_EX + wikipedia.summary(query, sentences=2))

# BMI Calculator
def bmi_calculator():
    clear_screen()
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    bmi = weight / (height ** 2)
    print(Fore.LIGHTCYAN_EX + f"Your BMI: {bmi:.2f}")

# Typing Speed Test
def typing_speed():
    clear_screen()
    fake = Faker()
    text = fake.sentence()
    print(Fore.YELLOW + f"Type this: {text}")
    input("Press Enter to start...")
    start = time.time()
    user_input = input()
    end = time.time()
    speed = len(text.split()) / (end - start) * 60
    print(Fore.GREEN + f"Typing Speed: {speed:.2f} WPM")

# Main Menu
def main():
    options = {
        "1": calculator, "2": joke, "3": password_generator, "4": coin_flip,
        "5": dice_roll, "6": countdown_timer, "7": text_to_speech, "8": ip_finder,
        "9": system_info, "10": file_explorer, "11": date_time, "12": age_calculator,
        "13": fun_fact, "14": qr_generator, "15": url_shortener, "16": wiki_search,
        "17": bmi_calculator, "18": typing_speed
    }

    while True:
        clear_screen()
        print(Fore.MAGENTA + ascii_art + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + "--- Friendly Multi-Tool ---" + Style.RESET_ALL)
        for i, feature in enumerate(options.keys(), start=1):
            print(Fore.CYAN + f"{i}. {options[feature].__name__.replace('_', ' ').title()}")
        print(Fore.RED + "0. Exit")

        choice = input(Fore.YELLOW + "Select an option: " + Style.RESET_ALL).strip()
        if choice == "0":
            print(Fore.RED + "Goodbye!")
            break
        elif choice in options:
            options[choice]()
            input(Fore.LIGHTGREEN_EX + "\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()



