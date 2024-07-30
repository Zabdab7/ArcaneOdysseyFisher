import pyautogui

def is_pixel_red(x, y):
    screen = pyautogui.screenshot()
    pixel_color = screen.getpixel((x, y))
    red_color = (255, 0, 0)

    return pixel_color == red_color

def main():
    x, y = 100, 100

    running = True
    while running:
        if is_pixel_red(x, y):
            print(f"The pixel at ({x}, {y}) is red")
            running = False


if __name__=='__main__':
    main()