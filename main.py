import pyautogui
import time
import threading
import random as rand

def get_center():
    resolution = pyautogui.size()
    return (resolution.width // 2, resolution.height // 2)

def get_pixel_color(x, y):
    screen = pyautogui.screenshot()
    pixel_color = screen.getpixel(x, y);
    return pixel_color


def main():

    pixel_location = get_center()

    running = True
    while running:
        if get_pixel_color(pixel_location) == (255, 255, 255):
            print(f"The pixel at center is white")
            pyautogui.moveTo(get_center())

            number_of_times = 20

            # Reel in
            for i in range(1, number_of_times):
                pyautogui.click()
                time.sleep(0.5 + rand.random())

        # Cast rod
        pyautogui.click()

        # TODO: Add fail safe to end program via key press
        # TODO: Multi threaded approach, one thread to listen to mouse inputs and one to listen to screen inputs



if __name__=='__main__':
    main()