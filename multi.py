import random
import json
import os
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# ASCII Art Placeholder
ascii_art = """
_____ ____  ____  ____  ____    _      _     _   _____  _ 
/  __//  __\/  __\/  _ \/  __\  / \__/|/ \ /\/ \ /__ __\/ \
|  \  |  \/||  \/|| / \||  \/|  | |\/||| | ||| |   / \  | |
|  /_ |    /|    /| \_/||    /  | |  ||| \_/|| |_/\| |  | |
\____\\_/\_\\_/\_\\____/\_/\_\  \_/  \|\____/\____/\_/  \_/
                                                           
"""

# File for storing to-do list
TODO_FILE = "todo_list.json"

# Sample motivational quotes
QUOTES = [
    "Believe in yourself! You can do it!",
    "Every day is a new opportunity to grow.",
    "Success starts with small, consistent actions.",
    "Don't watch the clock; do what it does. Keep going!",
]

# Load to-do list
def load_todo():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

# Save to-do list
def save_todo(todo_list):
    with open(TODO_FILE, "w") as file:
        json.dump(todo_list, file)

# Calculator
def calculator():
    try:
        expression = input(Fore.YELLOW + "Enter an expression (e.g., 5 + 3 * 2): " + Style.RESET_ALL)
        result = eval(expression)
        print(Fore.GREEN + f"Result: {result}")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

# To-do List
def todo_list():
    tasks = load_todo()
    
    while True:
        print(Fore.CYAN + "\n--- To-Do List ---" + Style.RESET_ALL)
        for i, task in enumerate(tasks, start=1):
            print(Fore.LIGHTMAGENTA_EX + f"{i}. {task}")
        
        print("\nOptions: [A]dd, [R]emove, [C]lear, [E]xit")
        choice = input(Fore.YELLOW + "Choose an option: " + Style.RESET_ALL).strip().lower()
        
        if choice == "a":
            task = input(Fore.GREEN + "Enter a new task: " + Style.RESET_ALL)
            tasks.append(task)
            save_todo(tasks)
        elif choice == "r":
            index = int(input(Fore.RED + "Enter task number to remove: " + Style.RESET_ALL)) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                save_todo(tasks)
            else:
                print(Fore.RED + "Invalid task number.")
        elif choice == "c":
            tasks.clear()
            save_todo(tasks)
            print(Fore.RED + "To-do list cleared.")
        elif choice == "e":
            break
        else:
            print(Fore.RED + "Invalid option.")

# Notes
def notes():
    file_name = "notes.txt"
    
    while True:
        print(Fore.CYAN + "\n--- Notes ---" + Style.RESET_ALL)
        print("[R]ead, [W]rite, [E]xit")
        choice = input(Fore.YELLOW + "Choose an option: " + Style.RESET_ALL).strip().lower()
        
        if choice == "r":
            if os.path.exists(file_name):
                with open(file_name, "r") as file:
                    print(Fore.LIGHTCYAN_EX + "\n--- Your Notes ---")
                    print(file.read())
            else:
                print(Fore.RED + "No notes found.")
        elif choice == "w":
            with open(file_name, "a") as file:
                note = input(Fore.GREEN + "Write your note: " + Style.RESET_ALL)
                file.write(note + "\n")
                print(Fore.GREEN + "Note saved!")
        elif choice == "e":
            break
        else:
            print(Fore.RED + "Invalid option.")

# Motivational Quote
def motivational_quote():
    print(Fore.LIGHTBLUE_EX + "\n" + random.choice(QUOTES) + "\n")

# Main Menu
def main():
    while True:
        print(Fore.MAGENTA + ascii_art + Style.RESET_ALL)  # Display ASCII art
        print(Fore.LIGHTYELLOW_EX + "--- Friendly Multi-Tool ---" + Style.RESET_ALL)
        print(Fore.CYAN + "1. Calculator")
        print(Fore.GREEN + "2. To-Do List")
        print(Fore.BLUE + "3. Notes")
        print(Fore.LIGHTMAGENTA_EX + "4. Motivational Quote")
        print(Fore.RED + "5. Exit")
        
        choice = input(Fore.YELLOW + "Select an option: " + Style.RESET_ALL).strip()
        
        if choice == "1":
            calculator()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            notes()
        elif choice == "4":
            motivational_quote()
        elif choice == "5":
            print(Fore.RED + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
