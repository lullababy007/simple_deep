import cv2
import pytesseract
import pyautogui
import numpy as np
from PIL import ImageGrab

# pytesseract의 실행 파일 경로 설정
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" # Tesseract 설치 경로에 맞게 수정하세요.

def find_icon_on_screen(icon_name):
    screenshot = ImageGrab.grab()  # 화면 스크린샷
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # PIL 이미지를 OpenCV 형식으로 변환
    
    custom_config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 6'  # OCR 엔진 모드 변경 코드
    text = pytesseract.image_to_string(screenshot_cv, config=custom_config)  # 화면의 텍스트 추출
    
    print(f"Extracted text: {text}")  # 추출된 텍스트 출력

    if icon_name in text:
        print(f"Found {icon_name} in text.")  # 아이콘 이름이 텍스트에 있는 경우 출력
        # 아이콘의 위치를 찾습니다.
        icon_coords = pyautogui.locateCenterOnScreen(r"C:\Users\a\Desktop\Eng\test2.png")  # 아이콘 이미지 파일의 절대 경로를 사용합니다.

        if icon_coords is not None:
            print(f"Icon coordinates: {icon_coords}")  # 아이콘 좌표 출력
            return icon_coords
    return None

def click_icon(icon_name):
    icon_coords = find_icon_on_screen(icon_name)

    if icon_coords is not None:
        pyautogui.moveTo(icon_coords)
        pyautogui.click()
        print(f"{icon_name} 아이콘을 클릭했습니다.")
    else:
        print(f"{icon_name} 아이콘을 찾지 못했습니다.")

if __name__ == "__main__":
    icon_name = "LOST ARK"  # 아이콘 이름을 입력하세요.
    click_icon(icon_name)
