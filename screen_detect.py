import cv2
import numpy as np
import pyautogui
import time

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screen_image = np.array(screenshot)
    screen_image = cv2.cvtColor(screen_image, cv2.COLOR_RGB2BGR)
    return screen_image

def detect_images(screen_image, template_paths, min_match_count=10):
    detected_images = []
    gray_screen_image = cv2.cvtColor(screen_image, cv2.COLOR_BGR2GRAY)

    for path in template_paths:
        template = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            print(f"Failed to read template from path: {path}")
            continue

        if gray_screen_image.shape[0] < template.shape[0] or gray_screen_image.shape[1] < template.shape[1]:
            print(f"Screen image is smaller than template: {path}")
            continue

        result = cv2.matchTemplate(gray_screen_image, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        if max_val > 0.8:
            detected_images.append((path, max_val, max_loc))

    return detected_images

def main():
    template_paths = [r"C:\Users\a\Desktop\Eng\1414281104.png"]
    while True:
        screen_image = take_screenshot()
        detected_images = detect_images(screen_image, template_paths, min_match_count=10)
        print("Detected images:", detected_images)
        time.sleep(1)

if __name__ == "__main__":
    main()
