#이미지 인식에 필요한 모듈 가져오기
import cv2
import numpy as np
import pyautogui
import time


def take_screenshot():
    #현재 화면을 캡쳐후 캡쳐된 이미지 객체를 스크린샷변수에 저장하고
    screenshot = pyautogui.screenshot()
    #스크린샷변수의 형식을 numpy 어레이로 변환함(
    #PyAutoGUI의 스크린샷 메서드는 PIL(Python Imaging Library) 모듈을 사용하여 이미지를 
    #반환함. 하지만 OpenCV에서 이미지를 다룰 때는 NumPy 어레이로 변환해주어야함)
    screen_image = np.array(screenshot)
    #어레이 색상 체계를 RGB에서 BGR로 변경함(OpenCV는 기본적으로 BGR 색상 체계를 사용)
    screen_image = cv2.cvtColor(screen_image, cv2.COLOR_RGB2BGR)
    #변경된 어레이를 반환
    return screen_image

def detect_images(image, templates):
    detected_images = []
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    for template in templates:
        if gray_image.shape[0] >= template.shape[0] and gray_image.shape[1] >= template.shape[1]:
            result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)
            threshold = 0.8
            if max_val > threshold:
                detected_images.append((max_val, max_loc))
    return detected_images

def main():
    template_files = [r"C:\Users\a\Desktop\Eng\1414281104.png"]
    image_templates = [cv2.imread(tf, cv2.IMREAD_GRAYSCALE) for tf in template_files]
    
    while True:
        screen_image = take_screenshot()
        detected_images = detect_images(screen_image, image_templates)
        print("Detected images:", detected_images)
        time.sleep(1)

if __name__ == "__main__":
    main()
