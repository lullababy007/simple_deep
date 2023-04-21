import cv2
import numpy as np
import pyautogui
import time
import sys
import os
from tensorflow.keras.models import load_model

# 모델 불러오기
model = load_model("C:\\Users\\a\\Desktop\\pythonworkspace\\icon_recognition_model.h5")


def take_screenshot():
    screenshot = pyautogui.screenshot()
    screen_image = np.array(screenshot)
    screen_image = cv2.cvtColor(screen_image, cv2.COLOR_RGB2BGR)
    return screen_image

def preprocess_image(image):
    # 이미지 크기 조정 및 정규화
    resized_image = cv2.resize(image, (32, 32))
    normalized_image = resized_image / 255.0
    return np.expand_dims(normalized_image, axis=0)

def predict_icon(image):
    processed_image = cv2.resize(image, (128, 128))  # 이미지 크기 변경
    processed_image = np.expand_dims(processed_image, axis=0)
    predictions = model.predict(processed_image)
    icon_id = np.argmax(predictions)
    return icon_id

def find_icon_position(image, icon_id):
    # 이미지 템플릿 불러오기
    icon_path = f"C:\\Users\\a\\Desktop\\Eng\\label{icon_id}\\test{icon_id}.png"
    icon_template = cv2.imread(icon_path, cv2.IMREAD_GRAYSCALE)
    
    if icon_template is None:
        print(f"Failed to load icon template from {icon_path}")
        sys.exit(1)
    
    

    # 이미지와 템플릿을 그레이스케일로 변환
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 템플릿 매칭 실행
    res = cv2.matchTemplate(image_gray, icon_template, cv2.TM_CCOEFF_NORMED)

    # 가장 높은 매칭 점수를 가진 위치 찾기
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # 아이콘 중심 위치 계산
    icon_center = (max_loc[0] + icon_template.shape[1] // 2, max_loc[1] + icon_template.shape[0] // 2)

    return icon_center

def click_icon(icon_position):
    pyautogui.moveTo(icon_position[0], icon_position[1], duration=0.5)
    pyautogui.click()
    pyautogui.click()


def main():
    screen_image = take_screenshot()
    icon_id = predict_icon(screen_image)
    icon_position = find_icon_position(screen_image, icon_id)
    click_icon(icon_position)

if __name__ == "__main__":
    main()

    print("Current working directory:", os.getcwd())
