# Third party imports
from pynput import mouse, keyboard

# Built-in imports
import os
from pathlib import Path

# Internal imports
from utils._logger import MyLogger
from utils.utils import log_event, create_log_file

file_name = os.path.basename(__file__)

logger = MyLogger(name=file_name, level="debug").logger

root_dir = Path(__file__).resolve().parent
mouse_events_file = root_dir / "data" / "mouse_events.json"
keyboard_events_file = root_dir / "data" / "keyboard_events.json"


create_log_file(mouse_events_file)
create_log_file(keyboard_events_file)

current_activity = "general"


def set_activity(activity):
    global current_activity
    current_activity = activity


def on_click(x, y, button, pressed):
    log_event(
        log_file=mouse_events_file,
        event_type="mouse_click",
        activity=current_activity,
        x=x,
        y=y,
        button=str(button),
        pressed=str(pressed),
    )

    if (
        button == mouse.Button.middle and not pressed
    ):  # middle click to stop the listener
        return False


def on_press(key):
    log_event(
        log_file=keyboard_events_file,
        event_type="key_press",
        activity=current_activity,
        key=str(key),
    )
    if key == keyboard.Key.esc:  # esc to stop the listener
        return False


def on_release(key):
    if key == keyboard.Key.esc:  # esc to stop the listener
        return False


def start_listener():
    # Start the keyboard listener
    keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    keyboard_listener.start()

    # Start the mouse listener
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()

    # Join the listeners to ensure they have stopped properly
    keyboard_listener.join()
    mouse_listener.join()


if __name__ == "__main__":
    activity_list = {
        "1": "general",
        "2": "programming",
        "3": "valorant",
        "4": "gaming",
        "5": "web_browsing",
        "6": "movie",
    }
    while True:
        print("Choose an activity:")
        for key, value in activity_list.items():
            print(f"Type '{key}' for '{value}'")

        choice = input("Enter the activity number: ")
        set_activity(activity_list.get(choice, "general"))
        start_listener()
