import pyautogui
import time
import threading
import keyboard

def check_key_press(stop_event):
    while not stop_event.is_set():
        if keyboard.is_pressed('q'):
            print("You pressed 'q'.")
            stop_event.set()
            break
        time.sleep(0.1)

def fish(stop_event):
    while not stop_event.is_set():
        # Cast Line
        # Wait for exclamation mark
        # Reel Line
        # Continue only after fish is secured i.e. yellow bit on bottom left is gone
        time.sleep(1)  # Placeholder for fishing logic

def main():
    print('Press "q" to end the program.')

    stop_event = threading.Event()

    io_thread = threading.Thread(target=check_key_press, args=(stop_event,))
    fishing_thread = threading.Thread(target=fish, args=(stop_event,))

    io_thread.start()
    fishing_thread.start()

    io_thread.join()
    fishing_thread.join()

    print("Program ended.q")


if __name__=='__main__':
    main()