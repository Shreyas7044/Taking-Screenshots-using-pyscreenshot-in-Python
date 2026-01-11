import pyscreenshot as ImageGrab

def capture_full_screen():
    """
    Captures the entire screen and saves it as screenshot.png
    """
    image = ImageGrab.grab()
    image.show()
    image.save("screenshot.png")
    print("Full screen screenshot saved as screenshot.png")


def capture_partial_screen():
    """
    Captures a specific region of the screen and saves it as partial_screenshot.png
    """
    # (x1, y1, x2, y2)
    image = ImageGrab.grab(bbox=(10, 10, 500, 500))
    image.show()
    image.save("partial_screenshot.png")
    print("Partial screen screenshot saved as partial_screenshot.png")


if __name__ == "__main__":
    print("1. Capture Full Screen")
    print("2. Capture Partial Screen")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        capture_full_screen()
    elif choice == "2":
        capture_partial_screen()
    else:
        print("Invalid choice")