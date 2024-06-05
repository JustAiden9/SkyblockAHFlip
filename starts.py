import keyboard
import subprocess
import time

# Define the path to your Python file
python_file_path = r"C:\\Users\\aiden\\OneDrive\\Desktop\\Flipping\\SS.py"

# Flag to track if the action is running
action_running = None

# Function to start or stop the action
def toggle_action():
    global action_running
    if action_running:
        subprocess.Popen(["TASKKILL", "/F", "/T", "/PID", str(action_running.pid)], shell=True)
        action_running = None
    else:
        action_running = subprocess.Popen(["python", python_file_path])

# Function to handle the hotkey event
def hotkey_triggered():
    if keyboard.is_pressed('left ctrl') and keyboard.is_pressed('s'):
        toggle_action()

# Register the hotkey without suppressing the key press
keyboard.add_hotkey('left ctrl+s', hotkey_triggered)

# Run an infinite loop to keep the script running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    if action_running:
        subprocess.Popen(["TASKKILL", "/F", "/T", "/PID", str(action_running.pid)], shell=True)
